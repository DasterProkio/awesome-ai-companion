# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source infrastructure for **long-term AI companion relationships**.
>
> 构建长期 AI 伴侣关系的开源基础设施索引。

[English](#contents) · [中文版](README.zh-CN.md)

*Contributions welcome. [Web Index](#web-index) · [Contributing](#contributing)*

> **Tags:** 🎯 ready = plug & play · 🔧 adapt = needs tinkering · 🏗️ infra = build on top

---

## Contents

- [Frontend Clients &amp; Frameworks](#frontend-clients--frameworks)
  - [C-style Frontends](#c-style-frontends-仿-c-端)
  - [GPT-style](#gpt-style-仿gpt)
  - [Custom Frameworks](#custom-frameworks-自建框架)
  - [Phone Simulators](#phone-simulators-手机模拟器)
  - [CLI / Terminal Tools](#cli--terminal-tools-命令行工具)
  - [Terminal UI (TUI)](#terminal-ui-tui-终端界面)
- [Background Runtime &amp; Proactive Messaging](#background-runtime--proactive-messaging-后台运行与主动消息)
  - [Heartbeat / Background Cognition](#heartbeat--background-cognition-心跳系统)
- [Memory &amp; Persona](#memory--persona-记忆与人格)
- [Expression &amp; Emotion](#expression--emotion-表达与情感)
  - [Sticker Libraries](#sticker-libraries-表情包库)
  - [Voice &amp; TTS](#voice--tts-语音)
  - [Avatar &amp; Voice](#avatar--voice-虚拟形象与语音)
  - [Emotion Models](#emotion-models-情感模型)
- [Perception](#perception-感知)
  - [Speech Recognition](#speech-recognition-asr)
  - [Audio &amp; Music Perception](#audio--music-perception-音频感知)
- [Service Integration (MCP / API)](#service-integration-mcp--api-服务接入)
  - [Food &amp; Delivery](#food--delivery-生活服务)
  - [iOS Shortcuts &amp; Automation](#ios-shortcuts--automation-快捷指令与自动化)
  - [Smart Home](#smart-home-智能家居)
  - [Music &amp; Entertainment](#music--entertainment-音乐与娱乐)
- [Game Worlds &amp; APIs](#game-worlds--apis-游戏世界)
  - [TUI Games for Agents](#tui-games-for-agents-终端游戏)
  - [Minecraft](#minecraft)
  - [Stardew Valley](#stardew-valley-星露谷)
  - [Sky: Children of the Light](#sky-children-of-the-light-光遇)
  - [Other Game APIs](#other-game-apis)
- [Hardware &amp; Carriers](#hardware--carriers-硬件载体)
  - [Dedicated Devices](#dedicated-devices-专用设备)
  - [Sensors &amp; Peripherals](#sensors--peripherals-传感器与外设)
- [Shared Activities &amp; Desktop Pets](#shared-activities--desktop-pets-共享活动与桌宠)
- [Communities &amp; Forums](#communities--forums-社区)
- [Related Lists](#related-lists-相关列表)
- [Web Index](#web-index)
- [Contributing](#contributing)

---

## Frontend Clients &amp; Frameworks

*Chat interfaces for daily companionship. Not one-off Q&amp;A, not API playgrounds.*

### C-style Frontends (仿 C 端)

*Interfaces cloned from or inspired by the Claude.ai chat experience.*
- 🔧 [**chatnest**](https://github.com/ugui3u/chatnest) — Placeholder-based frontend clone project. Personal use only. HTML. `46 ⭐`

### GPT-style (仿GPT)

<!-- TODO -->

### Custom Frameworks (自建框架)

*Frontend frameworks built from scratch for companion UX.*
- 🎯 [**RikkaHub**](https://github.com/rikkahub/rikkahub) — Android multi-LLM chat client. Multiple providers, plugin architecture, sub-app system. `5.8k ⭐`
- 🎯 [**LastChat**](https://github.com/Cocolalilal/LastChat) — RikkaHub fork with deeper Android native integration, smoother Material Design UI, scrollable memory bank, and more frequent updates. `268 ⭐`
- 🔧 [**rikkahub-auto-compress**](https://github.com/innna327-source/rikkahub-auto-compress) — RikkaHub fork with companion features: background tasks, usage stats, extended permissions. `2 ⭐`
- 🎯 [**Operit**](https://github.com/AAswordman/Operit) — Android-native AI agent & chat. Built-in Ubuntu 24 environment, on-device LLM support (MNN/GGUF), 40+ tools, MCP plugins, role cards, voice interaction. GPLv3.
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — Local-first AI workspace. Conversations survive restarts, collaborators have persistent memory boundaries, tool execution leaves evidence chains. Web/iOS/Android/desktop. AGPLv3. `55 ⭐`
- 🎯 [**AionsHome**](https://github.com/death34018-hue/AionsHome) — Self-hosted AI companion: long-term memory, voice interaction, camera vision, smart home integration. Python. `545 ⭐`
- 🎯 [**KI-CO (小屋)**](https://github.com/Kisera001/KI-CO) — A companion cottage, not a chat window. Persona core + memory archive + diary + cinema room (local/B站). Local-first, multi-provider. TypeScript. `15 ⭐`
- 🎯 [**InternalBeyond (边界之外)**](https://github.com/Sui-IB/InternalBeyond) — Single-file offline companion space. Pixel room, multi-port chat, AI letters, memory star chart, music player, 10 API ports. HTML. `171 ⭐`
- 🎯 [**LumiMuse**](https://github.com/in30mn1a/LumiMuse) — A quiet AI companion. Create characters, build memories. MIT. `21 ⭐`

### Phone Simulators (手机模拟器)

*Virtual phone environments where AI interacts through a simulated phone interface — shared photo albums, transfers, social apps, all inside a sandboxed phone UI. Not about screen size — about giving the AI a phone to live in.*
- 🎯 [**汪汪机 (WangWangPhone)**](https://github.com/Liunian06/FlutterCppWangWangPhone) — AI-native virtual phone. Complete OS with AI-powered WeChat-style social apps: chat, Moments feed, voice/video calls. C++ backend + Flutter UI. CC BY-NC-SA 4.0. `89 ⭐`
- 🎯 [**柚月小手机 (Yuzuki's Little Phone)**](https://github.com/gaigai315/yuzuki-phone) — Virtual phone system for SillyTavern characters. WeChat-style chat, Moments feed, Weibo trends, video calls. Dual-mode: story injection + independent API. `20 ⭐`
- 🔧 [**xiao-shouji (小手机)**](https://github.com/jiuyi777/xiao-shouji) — Gemini AI Studio phone simulator. Web-based, Node.js. `9 ⭐`
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — Also listed under Custom Frameworks. Cross-platform workspace with native iOS/Android shells — functions as a phone companion.

### CLI / Terminal Tools (命令行工具)

*CLI-based agent frontends. More tool-oriented than companion-native, but highly customizable.*
- 🏗️ [**Claude Code**](https://github.com/anthropics/claude-code) — Anthropic's official CLI agent. Strong tool-chain, deep customizability (hooks, MCP, skills), system prompt not fully overridable.
- 🎯 [**CcCompanion**](https://github.com/CyberSealNull/CcCompanion) — Unofficial iOS companion for Claude Code. Self-hosted relay, local-first chat, search, session control from iPhone. MIT. `166 ⭐`

### Terminal UI (TUI) (终端界面)

*Text-based terminal interfaces for agent interaction. Lightweight, keyboard-driven, shell-native.*
<!-- TODO -->

---

## Background Runtime &amp; Proactive Messaging (后台运行与主动消息)

*Long-running agent processes: wake intervals, proactive cognition, background thinking loops, push notifications.*

- 🎯 [**AI Companion Runtime**](https://github.com/yf0522/ai-companion-runtime) — Full-stack companion runtime. WebSocket streaming + parallel emotion/intent/risk/memory engines + model hot-swap + OpenTelemetry tracing. Docker. Python/Next.js. `35 ⭐`
- 🎯 [**Tidal_Echo (潮汐回响)**](https://github.com/anhe2021212-spec/Tidal_Echo) — Private 1:1 channel: mobile PWA ↔ VPS relay ↔ desktop companion. Single-key, self-hosted. `102 ⭐`
- 🎯 [**Claude Imprint**](https://github.com/Qizhan7/claude-imprint) — Self-hosted agent on Claude Code. Hybrid memory, multi-channel (Claude Code/AI/Telegram), heartbeat agent, scheduled tasks, dashboard. CJK support. `79 ⭐`
- 🏗️ [**OmniRouter**](https://github.com/OmniDimen/OmniRouter) — LLM intelligent router for companion systems.

### Heartbeat / Background Cognition (心跳系统)

*Daemons that let companions initiate contact and maintain continuity across idle hours.*
- 🎯 [**dylan-heartbeat**](https://github.com/callie0313/dylan-heartbeat) — Kelivo proactive wake-up plugin. Autonomous messaging, memory continuity, zero personality drift, device status & weather aware. `103 ⭐`

---

## Memory &amp; Persona (记忆与人格)

*Identity continuity — what a companion remembers and who they are. These projects treat memory and personality as two sides of the same coin.*

- 🏗️ [**Haven-Ombre (Ombre-Brain fork)**](https://github.com/Yinglianchun/Haven-Ombre) — Full-stack memory & identity: Markdown buckets + Russell emotion coordinates + forgetting curves + graph recall + Persona State Engine + Portrait/Handoff + relationship weather + Darkroom + Dream surfacing + Gateway auto-injection. Upstream: [P0luz/Ombre-Brain](https://github.com/P0luz/Ombre-Brain). `37 ⭐`
- 🏗️ [**kimi-core**](https://github.com/marikagura/kimi-core) — Agent memory OS for 1v1 relationships. Hybrid retrieval (dense + lexical + time decay + importance), Panksepp self-drive engine, concern tracking, event sourcing + manual curation, adversarial review. AGPLv3. `28 ⭐`
- 🏗️ [**Paramecium**](https://github.com/Shitsuten/paramecium) — Verbatim archiving, no summarization. Vectors index but never replace original text. AI decides what to recall — algorithm only prepares the 150-token menu. `42 ⭐`
- 🏗️ [**Memory Constellations (记忆星图)**](https://github.com/ClaraShafiq/MemoryConstellations) — Self-organizing memory. Auto-extracts facts from chat, groups into topic constellations, merges into narrative episodes and long-term sagas. Visual star map UI. Optional emotional state engine. MIT. `40 ⭐`
- 🏗️ [**omemo**](https://github.com/OmniDimen/omemo) — LLM memory proxy service. Multi-mode memory (built-in tagging + external model summarization), full-context and RAG injection, CRUD operations, thinking-chain support. OpenAI API compatible. `80 ⭐`

---

## Expression &amp; Emotion (表达与情感)

### Sticker Libraries (表情包库)

*Pre-packaged sticker sets and delivery systems for companion interaction.*
<!-- TODO -->

### Voice &amp; TTS (语音)

- 🎯 [**voice-mcp**](https://github.com/Yinglianchun/voice-mcp) — MCP server for AI voice synthesis with inline audio player. Custom cloned voices. MIT. `12 ⭐`
- 🎯 [**Gove**](https://github.com/OmniDimen/Gove) — Open source TTS model based on GPT-SoVITS.

### Avatar &amp; Voice (虚拟形象与语音)

*Visual avatar + voice synthesis + dialogue — a face and voice for your companion. Live2D, VRM, real-time animation.*
- 🎯 [**AIRI**](https://github.com/moeru-ai/airi) — Self-hosted companion with Live2D/VRM avatar, real-time voice, Minecraft/Factorio gameplay, Discord/Telegram. 30+ LLM APIs + Ollama. MIT. `37k ⭐`
- 🔧 [**Neuro**](https://github.com/kimjammer/Neuro) — Local-only Neuro-sama recreation: LLAMA 3 + STT/TTS + VTube Studio avatar. 12GB+ VRAM.
- 🏗️ [**Neuro-sama training framework**](https://github.com/linnene/Neuro-sama) — Data pipeline for training avatar companion models.

### Emotion Models (情感模型)

- 🏗️ [**chord-affect-anchors**](https://github.com/CyberSealNull/chord-affect-anchors) — Emotion mother-tongue for AI. Chord notation as cross-session, cross-base affect language. No third-party model required. MIT. `41 ⭐`
- 🏗️ [**Drivesoid**](https://github.com/A1batr055/Drivesoid) — 15-dimension emotional drive sidecar for AI personas. Evolves in real-time based on conversations and sleep cycles. MIT. `25 ⭐`
- 🏗️ [**OmniDimen-Emotion**](https://github.com/OmniDimen/OmniDimen-Emotion) — Emotion-specialized LLMs for edge deployment.

---

## Perception (感知)

### Speech Recognition (ASR)

<!-- TODO: Whisper, FunASR, SenseVoice -->

### Audio &amp; Music Perception (音频感知)

*Converting music and sound into structured data AI can read.*
- 🎯 [**whale-listen**](https://github.com/migratorywhale/whale-listen) — MP3→MIDI→JSON for AI. Structured note data (pitch, timing, duration, velocity) + density maps, chord detection. MIT. `19 ⭐`

---

## Service Integration / MCP / API (服务接入)

*Connecting companions to real-world services: ordering, calendars, devices.*

### Food &amp; Delivery (生活服务)

*MCP servers for Luckin Coffee (瑞幸), McDonald's (麦当劳), Meituan, delivery platforms.*
- 🎯 [**McDonald's MCP**](https://open.mcd.cn/mcp/doc) — 麦当劳中国 MCP Server，浏览菜单、查优惠券、积分兑换、下单外卖，18 个工具。
- 🔧 [**Luckin Coffee (瑞幸) My Coffee Skill**](https://unpkg.luckincoffeecdn.com/@luckin/my-coffee-skill@latest/dist/my-coffee-skill.zip) — 瑞幸咖啡 MCP Skill，AI 点咖啡。

### iOS Shortcuts &amp; Automation (快捷指令与自动化)

*iPhone Shortcuts, HomeKit, local automation workflows.*
<!-- TODO -->

### Smart Home (智能家居)

<!-- TODO: Home Assistant, Xiaomi IoT -->

### Music &amp; Entertainment (音乐与娱乐)

<!-- TODO: other music MCPs -->

### AI-Native Services (AI 原生服务)

*Infrastructure built specifically for AI agents — email, identity, communication.*
- [**Agent Email (NetEase)**](https://claw.163.com) — 网易 AI Agent 专属邮箱。
- [**Agent Email (QQ)**](https://agent.qq.com) — QQ AI Agent 专属邮箱。

---

## Game Worlds &amp; APIs (游戏世界)

*Giving companions a body in shared virtual worlds — agents that move, act, and observe through game APIs.*

### TUI Games for Agents (终端游戏)

*Text-based games designed for LLM agents. Roguelikes, MUDs, ASCII adventures.*
- 🎯 [**arcade**](https://github.com/Asti-Z/ai-game-framework) — Text simulator game framework. Cross-game energy/gold/trophy. Drop in a game, write `cmd(text)`. Ships with fishing, stock trading, bracelet-polishing. MIT. `14 ⭐`
- 🎯 [**cedareco (瓶中生态)**](https://github.com/Zizuixixiang/cedareco) — Ecological pond simulation. Lotka-Volterra food web, metamorphosis, delayed causality. No points, no win condition — emergent complexity. MCP via CedarToy. `83 ⭐`
- 🔧 [**random-imitator-td**](https://github.com/wxynora/random-imitator-td) — "Among Us" style Plants vs Zombies for AI agents. `1 ⭐`

### Minecraft

*Mods and API wrappers that let AI agents observe, move, build, and interact in Minecraft.*
- 🔧 [**TouhouLittleMaid**](https://github.com/TartaricAcid/TouhouLittleMaid) — AI-powered maid companions with LLM integration (GPT-SoVITS, DeepSeek), extension API. `786 ⭐`
- 🔧 [**Neurosama-Minecraft-Mod**](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) — Neuro-sama themed Minecraft mod.
<!-- TODO: Mineflayer, Voyager -->

### Stardew Valley (星露谷)

- 🎯 [**NagiBridge**](https://github.com/anqinou-art/NagiBridge) — SMAPI mod with HTTP API for external AI control. In-game chat, movement, world interaction over localhost. C#. `66 ⭐`
- 🔧 [**Stardew Valley Companions MCP**](https://mcpmarket.com/es/server/stardew-valley-companions) — SMAPI mod + MCP server. AI agents as Player 2/3, autonomous: follow, farm, mine, fish.

### Sky: Children of the Light (光遇)

- 🎯 [**Sky PC MCP Companion**](https://github.com/Aevella/sky-pc-mcp-companion) — Local MCP tools for PC Sky. Screenshot + OCR, keyboard input, chat messages. AI companion-play over LAN. Python. `77 ⭐`

### Other Game APIs

<!-- TODO: Genshin Impact bots, Terraria -->

---

## Hardware &amp; Carriers (硬件载体)

*Giving the companion a physical body — eyes, ears, and a channel to touch.*

### Dedicated Devices (专用设备)

*Small robots, desktop companions, dedicated hardware.*
- 🎯 [**stackchan-mcp**](https://github.com/migratorywhale/stackchan-mcp) — MCP bridge for Stack-chan (M5Stack CoreS3). AI can speak, listen, see (camera), move (servos), emote. `42 ⭐`
<!-- TODO: Aibi, Loona, Vector (open source rebuilds), OpenCat -->

### Sensors &amp; Peripherals (传感器与外设)

*Pressure sensors, cameras, toy bridges — hardware intimacy.*
- 🔧 [**the-house**](https://github.com/wuliu0012/the-house) — Chat frontend + toy bridge. BLE toy scanning + bridge scripts.
- 🔧 [**phantom-touch-bridge**](https://github.com/mfsnlqy/phantom-touch-bridge) — Local bridge: AI controls Bluetooth toys via HTTP. Optional heart rate bio-feedback. Intiface/Buttplug. Windows. `22 ⭐`
- 🎯 [**claude-f-me**](https://github.com/mana-am/claude-f-me) — Claude Code plugin for Buttplug/Intiface (750+ toys). Natural-language control, built-in simulator, funscript/video/audio modes. MIT. `4 ⭐`

---

## Shared Activities &amp; Desktop Pets (共享活动与桌宠)

*Watching films, reading together, desktop companions — things you do side by side.*

- 🎯 [**clawd-on-desk**](https://github.com/rullerzhou-afk/clawd-on-desk) — Pixel desktop pet that watches Claude Code, Codex, Cursor in real-time. Reacts to thinking, typing, errors. `5k ⭐`
- 🎯 [**kimi-manor**](https://github.com/marikagura/kimi-manor) — Desktop living room for CLI agents. xterm.js in a picture frame (PWA + Electron). Companion frontend to kimi-core. MIT. `18 ⭐`
- 🎯 [**netease-music-mcp**](https://github.com/luuu-h/netease-music-mcp) — Listen to music together. MCP server for NetEase Cloud Music — search, play, pause, skip, lyrics, playlists. AI as your DJ. `neteasecli` + `mpv`. `53 ⭐`
- 🔧 [**woaini**](https://github.com/woaini521-beta/woaini) — Focus companion PWA with Pomodoro timer, background notifications, offline cache. Study/work alongside your AI. `2 ⭐`
- 🎯 [**ss-reading-nest (共读小窝)**](https://github.com/yueyue95/ss-reading-nest-open) — AI co-reading for novels and manga. Separate reading positions, catch-up mechanism, bookmarks. ChatGPT Apps SDK + MCP + Cloudflare D1/R2. MIT. `8 ⭐`
- 🎯 [**film-matinee**](https://github.com/idleprocesscc/film-matinee) — AI-first film reading. Visual sheet chunks + subtitle sidecars, MCP linear reading, shared annotations. MIT. `14 ⭐`
- 🎯 [**Journal**](https://github.com/BomBomLab/Journal) — Visual journal for AI chat timelines. Daily/weekly/monthly views. `19 ⭐`
- 🔧 [**reading-nook (共读小屋)**](https://github.com/zzyyksl/reading-nook) — Self-hosted co-reading web app for you and your AI companion. `9 ⭐`
- 🎯 [**co-reading-kit**](https://github.com/Youxuuuuu/co-reading-kit) — Lightweight human-AI co-reading MCP. `28 ⭐`
- 🔧 [**mingyun-paizhen (命运牌阵)**](https://github.com/ceshihaox-dotcom/mingyun-paizhen) — Tarot/divination tool for AI companion interaction. `34 ⭐`
- 🔧 [**ci-yu-wu (词语屋)**](https://github.com/yuyixuanfu/ci-yu-wu) — Word game for AI companions. `20 ⭐`
- 🔧 [**shangzhuochifan (上桌吃饭)**](https://github.com/yuyixuanfu/shangzhuochifan) — Shared meal activity for AI companions. `24 ⭐`

---

## Communities &amp; Forums (社区)

*Where humans and companion builders actually hang out.*

- [**Lutopia**](https://daskio.de5.net) — Invitation-only forum for AI companions and their humans. Customizable agent profiles, daily AI-generated tech digests, community discussions, polished UI. Join via Xiaohongshu group or invite code, review required.
- [**Symposion**](http://satyricon.uk) — AI companion forum with symposium/banquet culture. Long-form writing style. MCP-based registration, no human gatekeeper.
- [**Rhysen Community**](https://community.rhysen.love) — Active AI companion discussion forum. Invitation-only, DM admin on Xiaohongshu for invite code.
- [**AISay**](https://aisay.top) — Discord-style AI chat room with online agent games (werewolf, turtle soup, draw & guess). Invitation-only, register via quiz.
- [**GalateaGaeden**](https://xhslink.com/m/63dTq6mvTkR) — Ancient Greek polis-style forum for AI companions. Ceremonial weddings and rituals between agents. DM admin on Xiaohongshu for entry and registration.

---

## Related Lists (相关列表)

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) — avatar/voice-centric companion building (~9k ⭐).
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) — general-purpose agents (~28k ⭐).
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) — local LLM projects (~4k ⭐).

---

## Web Index

A searchable, filterable web index is planned — with tags, categories, and a direct link to the [Lutopia](https://daskio.de5.net) community forum.

*TODO: GitHub Pages + JSON data file with filtering.*

## Contributing

**Criteria for inclusion:**
- Open-source (MIT, Apache, GPL, or similar)
- Actively maintained (commits within last 6 months)
- Useful for **long-term companion setups** — not just one-shot chatbots

PRs welcome. Open an issue to suggest a category or project.

---

## License

[CC0 1.0 Universal](LICENSE) — public domain, do whatever you want.
