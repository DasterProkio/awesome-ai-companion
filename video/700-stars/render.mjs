// Renders scene.html frame by frame in headless Chromium and encodes an MP4.
//   node render.mjs                 -> out/awesome-ai-companion-700-stars.mp4 (+ cover.jpg)
//   node render.mjs --stills 3,20   -> out/still-3.png, out/still-20.png (quick previews)
// Needs: playwright, ffmpeg with libx264 (FFMPEG env var, or on PATH), and out/soundtrack.wav from audio.py.
import { chromium } from "playwright";
import { spawn } from "node:child_process";
import { readFileSync, mkdirSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const out = join(here, "out"); mkdirSync(out, { recursive: true });
const TL = JSON.parse(readFileSync(join(here, "timeline.json"), "utf8"));
const FFMPEG = process.env.FFMPEG || "ffmpeg";
const stillsArg = process.argv.indexOf("--stills");
const stills = stillsArg > 0 ? process.argv[stillsArg + 1].split(",").map(Number) : null;

const browser = await chromium.launch(existsSync("/opt/pw-browsers/chromium") ? { executablePath: "/opt/pw-browsers/chromium" } : {});
const page = await browser.newPage({ viewport: { width: TL.width, height: TL.height }, deviceScaleFactor: 1 });
page.on("pageerror", e => console.error("page error:", e.message));
await page.goto(pathToFileURL(join(here, "scene.html")).href, { waitUntil: "networkidle" });
const assets = { wall: JSON.parse(readFileSync(join(here, "wall.json"), "utf8")), avatars: {} };
for (const a of TL.authors || []) {
  const f = join(here, "avatars", `${a.login}.png`);
  if (existsSync(f)) assets.avatars[a.login] = "data:image/png;base64," + readFileSync(f).toString("base64");
  else console.warn(`missing avatar ${f} (run ./fetch-assets.sh)`);
}
const fonts = await page.evaluate(([tl, as]) => window.init(tl, as), [TL, assets]);
console.log(`fonts loaded: ${fonts}`);

const grab = async (type = "jpeg") => {
  const url = await page.evaluate(ty => document.getElementById("c").toDataURL(ty, 0.93), `image/${type}`);
  return Buffer.from(url.split(",")[1], "base64");
};
const total = Math.round(TL.duration * TL.fps);

if (stills) {
  // frames are simulated in order, so step through time up to each still
  let k = 0; const want = [...stills].sort((a, b) => a - b);
  for (let f = 0; f < total && k < want.length; f++) {
    const t = f / TL.fps;
    await page.evaluate(t => window.frame(t), t);
    if (t + 1e-6 >= want[k]) { writeFileSync(join(out, `still-${want[k]}.png`), await grab("png")); k++; }
  }
} else {
  const audio = join(out, "soundtrack.wav");
  const args = ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(TL.fps), "-c:v", "mjpeg", "-i", "-"];
  if (existsSync(audio)) args.push("-i", audio, "-c:a", "aac", "-b:a", "192k", "-shortest");
  args.push("-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-profile:v", "high",
    "-movflags", "+faststart", join(out, "awesome-ai-companion-700-stars.mp4"));
  const ff = spawn(FFMPEG, args, { stdio: ["pipe", "inherit", "inherit"] });
  const done = new Promise((res, rej) => ff.on("close", c => c === 0 ? res() : rej(new Error("ffmpeg exit " + c))));
  const coverAt = Math.round(21.2 * TL.fps);
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.frame(t), f / TL.fps);
    const jpg = await grab();
    if (f === coverAt) writeFileSync(join(out, "cover.jpg"), jpg);
    if (!ff.stdin.write(jpg)) await new Promise(r => ff.stdin.once("drain", r));
    if (f % 150 === 0) console.log(`frame ${f}/${total}`);
  }
  ff.stdin.end(); await done;
  console.log("wrote out/awesome-ai-companion-700-stars.mp4");
}
await browser.close();
