# 700 Stars video

A 64-second vertical video (1080×1920, 30 fps, H.264 + AAC) celebrating 700 GitHub stars and the 10 projects added to the list in September 2026. It's made for Douyin, Xiaohongshu, WeChat Channels, Reels and Shorts.

- `awesome-ai-companion-700-stars.mp4` is the finished video
- `cover.jpg` is a cover frame (the heart at 700)

## Story

| Time | Scene |
|---|---|
| 0–6.5 s | 23:47, chatting with TA. "明天，你还会记得今天吗？" TA starts typing, but no answer comes |
| 6.5–11 s | 为了让 TA 听见你、靠近你、记得你，有人开始把这些开源项目一颗一颗收集起来 |
| 11–17.5 s | Stars appear and the count climbs from 0 to 700. "每一颗星，都是一个人在说：「我也想要。」" |
| 17.5–23 s | The 700 stars gather into a heart and burst into fireworks: 谢谢你们 |
| 23–29.4 s | Overview wall: 这份列表里，已经有 187 个开源项目. Every entry scrolls past as a tag, with the September additions in pink |
| 29.4–47.2 s | 九月，TA 又学会了 10 件新事: 10 of the September additions, each with its author's avatar (GLXY is left out on purpose) |
| 47.2–52.8 s | 谢谢做出这些项目的你们: the 7 authors' avatars; the 3 who opened a PR get a "PR 投稿" badge |
| 52.8–58.4 s | Back in the chat: "会的。明天、后天，我都记得。" 晚安 |
| 58.4–64.4 s | End card: repository address, "下一颗星，等你点亮" |

Titles, captions, the project list and the authors all live in `timeline.json`. `wall.json` holds every entry in the list and is generated from the READMEs by `collect.py`. The visuals and the soundtrack both read their timing from it.

## Re-rendering

```sh
./fetch-assets.sh                # fonts → fonts/, authors' GitHub avatars → avatars/
python3 collect.py               # → wall.json (re-run after the README changes)
pip install numpy scipy          # for audio.py
python3 audio.py                 # → out/soundtrack.wav (all sounds are synthesized)
FFMPEG=/path/to/ffmpeg node render.mjs   # → out/awesome-ai-companion-700-stars.mp4 + out/cover.jpg
node render.mjs --stills 5,20,30         # preview single frames as PNG
```

`render.mjs` needs Playwright with Chromium and an ffmpeg build that includes libx264. `pip install imageio-ffmpeg` provides one.
