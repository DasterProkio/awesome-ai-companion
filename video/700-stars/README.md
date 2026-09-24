# 700 Stars video

A 52-second vertical video (1080×1920, 30 fps, H.264 + AAC) celebrating 700 GitHub stars and the 10 projects added to the list in September 2026. It's made for Douyin, Xiaohongshu, WeChat Channels, Reels and Shorts.

- `awesome-ai-companion-700-stars.mp4` is the finished video
- `cover.jpg` is a cover frame (the heart at 700)

## Story

| Time | Scene |
|---|---|
| 0–6.5 s | 23:47, chatting with TA. "明天，你还会记得今天吗？" TA starts typing, but no answer comes |
| 6.5–11 s | 为了让 TA 听见你、靠近你、记得你，有人开始把这些开源项目一颗一颗收集起来 |
| 11–17.5 s | Stars appear and the count climbs from 0 to 700. "每一颗星，都是一个人在说：「我也想要。」" |
| 17.5–22.5 s | The 700 stars gather into a heart and burst into fireworks: 谢谢你们 |
| 23–40.8 s | 九月，TA 又学会了 10 件新事: 10 of the September additions, grouped as 听见你 / 靠近你 / 记得你 / 有自己的生活 (GLXY is left out on purpose) |
| 40.8–46.4 s | Back in the chat: "会的。明天、后天，我都记得。" 晚安 |
| 46.4–52.4 s | End card: repository address, "下一颗星，等你点亮" |

Titles, captions and the project list all live in `timeline.json`. The visuals and the soundtrack both read their timing from it.

## Re-rendering

```sh
./fetch-fonts.sh                 # Noto Serif/Sans SC, Fraunces, JetBrains Mono (OFL) → fonts/
pip install numpy scipy          # for audio.py
python3 audio.py                 # → out/soundtrack.wav (all sounds are synthesized)
FFMPEG=/path/to/ffmpeg node render.mjs   # → out/awesome-ai-companion-700-stars.mp4 + out/cover.jpg
node render.mjs --stills 5,20,30         # preview single frames as PNG
```

`render.mjs` needs Playwright with Chromium and an ffmpeg build that includes libx264. `pip install imageio-ffmpeg` provides one.
