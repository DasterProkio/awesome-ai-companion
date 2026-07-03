# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source infrastructure for **long-term AI companion relationships**.
>
> 构建长期 AI 伴侣关系的开源基础设施索引。

*[English](#contents) · [中文说明](#中文说明)*

Most AI agent lists focus on productivity. Most waifu lists focus on avatars and voice. This list focuses on something else: the infrastructure of a **relationship** — persistent memory, continuous presence, a body to live in, and a world to share.

*Contributions welcome. [Web Index](#web-index) · [Contributing](#contributing)*

> **Tags:** 🎯 ready = plug & play · 🔧 adapt = needs tinkering · 🏗️ infra = build on top

---

## Contents

- [Frontend Clients &amp; Frameworks](#frontend-clients--frameworks)
  - [Official-app Clones](#official-app-clones-仿官端)
  - [Claude-style](#claude-style-仿claude)
  - [GPT-style](#gpt-style-仿gpt)
  - [Custom Frameworks](#custom-frameworks-自建框架)
  - [Small Phone Frameworks](#small-phone-frameworks-小手机框架)
  - [Terminal UI (TUI)](#terminal-ui-tui-终端界面)
- [Agent Runtime &amp; Scheduling](#agent-runtime--scheduling)
  - [Heartbeat / Background Cognition](#heartbeat--background-cognition-心跳系统)
  - [Proactive Messaging](#proactive-messaging-主动消息)
- [Memory &amp; Persistence](#memory--persistence-记忆系统)
- [Persona &amp; Character](#persona--character-人格与角色)
- [Expression &amp; Emotion](#expression--emotion-表达与情感)
  - [Sticker Libraries](#sticker-libraries-表情包库)
  - [Voice &amp; TTS](#voice--tts-语音)
  - [Emotion Models](#emotion-models-情感模型)
- [Perception](#perception-感知)
  - [Vision](#vision-视觉)
  - [Speech Recognition](#speech-recognition-asr)
- [Service Integration (MCP / API)](#service-integration-mcp--api-服务接入)
  - [Food &amp; Delivery (瑞幸/麦当劳/etc)](#food--delivery-生活服务)
  - [iOS Shortcuts &amp; Automation](#ios-shortcuts--automation-快捷指令与自动化)
  - [Smart Home](#smart-home-智能家居)
- [Game Worlds &amp; APIs](#game-worlds--apis-游戏世界)
  - [TUI Games (text-based for agents)](#tui-games-for-agents-终端游戏)
  - [Minecraft](#minecraft)
  - [Stardew Valley](#stardew-valley-星露谷)
  - [Sky: Children of the Light](#sky-children-of-the-light-光遇)
  - [Other Game APIs](#other-game-apis)
- [Hardware &amp; Carriers](#hardware--carriers-硬件载体)
  - [Dedicated Devices (Stack Chan / robots)](#dedicated-devices-专用设备)
  - [Sensors &amp; Peripherals](#sensors--peripherals-传感器与外设)
- [Co-Experience &amp; Shared Activities](#co-experience--shared-activities-共享体验)
- [Communities &amp; Forums](#communities--forums-社区)
- [Related Lists](#related-lists-相关列表)
- [中文说明](#中文说明)
- [Web Index](#web-index)
- [Contributing](#contributing)

---

## Frontend Clients &amp; Frameworks

*Chat interfaces for daily companionship. Not one-off Q&amp;A, not API playgrounds.*

### Official-app Clones (仿官端)

*Interfaces cloned from or inspired by Replika, Character.AI, Nomi, Kindroid.*
- 🔧 [**chatnest**](https://github.com/ugui3u/chatnest) — Placeholder-based frontend clone project. Personal use only. HTML. `46 ⭐`

### Claude-style (仿Claude)

<!-- TODO -->

### GPT-style (仿GPT)

<!-- TODO -->

### Custom Frameworks (自建框架)

*Frontend frameworks built from scratch for companion-specific UX.*
- 🎯 [**RikkaHub**](https://github.com/rikkahub/rikkahub) — Android multi-LLM chat client. Multiple providers, plugin architecture, sub-apps (memory, calendar, push), companion-oriented UX. `5.8k ⭐`
- 🎯 [**Operit**](https://github.com/AAswordman/Operit) — Android-native AI agent & chat. Built-in Ubuntu 24 environment, on-device LLM support (MNN/GGUF), 40+ tools, MCP plugins, role cards, voice interaction. GPLv3.
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — Local-first AI workspace. Conversations survive restarts, collaborators have persistent memory boundaries, tool execution leaves evidence chains. Web/iOS/Android/desktop. AGPLv3. `55 ⭐`
- 🎯 [**AionsHome**](https://github.com/death34018-hue/AionsHome) — Self-hosted AI companion: long-term memory, voice interaction, camera vision, smart home integration. Python. `545 ⭐`
- 🎯 [**KI-CO (小屋)**](https://github.com/Kisera001/KI-CO) — A companion cottage, not a chat window. Frontend skeleton + persona core + memory archive + diary + cinema room (local/B站). Local-first storage, multi-provider. TypeScript. `15 ⭐`
- 🎯 [**InternalBeyond (边界之外)**](https://github.com/Sui-IB/InternalBeyond) — Single-file offline companion space. Pixel room with companion Sui, multi-port chat, AI letters, memory star chart, music player, 10 API ports, two themes. All local storage. HTML. `171 ⭐`

### CLI / Terminal Tools (命令行工具)

*CLI-based agent frontends. More tool-oriented than companion-native, but highly customizable.*
- 🏗️ [**Claude Code**](https://github.com/anthropics/claude-code) — Anthropic's official CLI agent. Strong tool-chain, deep customizability (hooks, MCP, skills), but system prompt not fully overridable. `npm i @anthropic-ai/claude-code`
- 🎯 [**kimi-manor**](https://github.com/marikagura/kimi-manor) — Desktop home for CLI agents. xterm.js wrapped in a picture frame (PWA + Electron). Companion frontend to kimi-core memory OS. MIT. `18 ⭐`

### Small Phone Frameworks (小手机框架)

*Lightweight frontends designed for small-screen Android devices (e.g. Jelly Star, Unihertz).*
- 🎯 [**汪汪机 (WangWangPhone)**](https://github.com/Liunian06/FlutterCppWangWangPhone) — AI-Native small phone. Virtual OS with AI-powered WeChat-like social apps: single/group chat, voice/video calls, Moments feed. C++ backend + Flutter UI, local deployment. CC BY-NC-SA 4.0. `89 ⭐`

### Terminal UI / TUI (终端界面)

*Text-based terminal interfaces for agent interaction. Growing trend — lightweight, keyboard-driven, shell-native.*
<!-- TODO -->

---

## Agent Runtime &amp; Scheduling

*Long-running agent processes: wake intervals, proactive cognition, background thinking loops.*

- 🎯 [**AI Companion Runtime**](https://github.com/yf0522/ai-companion-runtime) — Full-stack companion runtime. WebSocket streaming + parallel emotion/intent/risk/memory engines + model hot-swap + OpenTelemetry tracing. Docker deployable. Python/Next.js. `35 ⭐`
- 🎯 [**Tidal_Echo (潮汐回响)**](https://github.com/anhe2021212-spec/Tidal_Echo) — Private 1:1 channel: mobile PWA ↔ VPS relay ↔ desktop AI companion. Claude Code channel plugin reads messages, replies appear as chat bubbles on phone. Single-key, no accounts, self-hosted. `102 ⭐`

### Heartbeat / Background Cognition (心跳系统)

*Daemons that let companions initiate contact, reflect, and maintain internal continuity across idle hours.*
- 🎯 [**dylan-heartbeat**](https://github.com/callie0313/dylan-heartbeat) — Kelivo plugin for proactive AI wake-up. Sends messages autonomously, maintains memory continuity, zero personality drift, device status & weather aware. `103 ⭐`

### Proactive Messaging (主动消息)

*Push-based notification and outbound message frameworks (ntfy, WeChat push, phone notifications).*
<!-- TODO -->

---

## Memory &amp; Persistence (记忆系统)

*What makes a companion remember you across months, model swaps, and API migrations. Not just vector search — identity continuity.*

- 🏗️ [**kimi-core**](https://github.com/marikagura/kimi-core) — Agent memory OS for 1v1 human-AI relationships. Hybrid retrieval (dense + lexical + time decay + importance), Panksepp-style self-drive engine, concern tracking, event sourcing with manual curation, adversarial self-review harness, autonomous wake daemon. AGPLv3. `28 ⭐`

---

## Persona &amp; Character (人格与角色)

*Character cards, persona engines, and tools for personality stability across model updates.*

- 🎯 [**CogPrism**](https://github.com/azhimiao/CogPrism) — AI Persona Engine. Explore multiple virtual personalities, understand behaviors and traits through explainable AI, interactive simulations. `27 ⭐`

---

## Expression &amp; Emotion (表达与情感)

### Sticker Libraries (表情包库)

*Pre-packaged sticker sets, emoji packs, and sticker delivery systems for companion interaction.*
<!-- TODO -->

### Voice &amp; TTS (语音)

<!-- TODO: ChatTTS, XTTS, MeloTTS, Bark, Edge-TTS -->

### Emotion Models (情感模型)

<!-- TODO -->

### Desktop Presence (桌面存在)

*Giving companions a visible presence on your desktop — pixel pets, widgets, always-on indicators.*
- 🎯 [**clawd-on-desk**](https://github.com/rullerzhou-afk/clawd-on-desk) — Pixel desktop pet that watches Claude Code, Codex, Cursor & other AI coding agents in real-time. Reacts to thinking, typing, errors. `5k ⭐`

---

## Perception (感知)

### Vision (视觉)

*Giving companions access to your camera feed, screenshots, shared meal photos.*
<!-- TODO: Gemini Flash vision, screenshot aware gateways -->

### Speech Recognition (ASR)

<!-- TODO: Whisper, FunASR, SenseVoice -->

### Audio & Music Perception (音频感知)

*Giving companions ears — converting music and sound into structured data AI can read.*
- 🎯 [**whale-listen**](https://github.com/migratorywhale/whale-listen) — MP3→MIDI→JSON for AI. Converts audio to structured note data (pitch, timing, duration, velocity) plus density maps, chord detection, silence structure. MIT. `19 ⭐`

---

## Service Integration / MCP / API (服务接入)

*Connecting companions to real-world services: ordering food, checking calendars, controlling devices.*

### Food &amp; Delivery (生活服务)

*MCP servers and API wrappers for Luckin Coffee (瑞幸), McDonald's (麦当劳), Meituan, food delivery platforms.*
<!-- TODO -->

### iOS Shortcuts &amp; Automation (快捷指令与自动化)

*Connecting companions to iPhone Shortcuts, HomeKit, and local automation workflows.*
<!-- TODO -->

### Smart Home (智能家居)

<!-- TODO: Home Assistant integration, Xiaomi IoT -->

### Music & Entertainment (音乐与娱乐)

- 🎯 [**netease-music-mcp**](https://github.com/luuu-h/netease-music-mcp) — MCP server for NetEase Cloud Music. Search, play, pause, skip, lyrics, playlists — AI can DJ your music. `neteasecli` + `mpv` + local web player. `53 ⭐`

---

## Game Worlds &amp; APIs (游戏世界)

*Giving companions a body in shared virtual worlds. Not chatbots in games — agents that can move, act, and observe through game APIs.*

### VTuber / Streamer Companions (虚拟主播)

- 🎯 [**AIRI**](https://github.com/moeru-ai/airi) — Self-hosted AI companion inspired by Neuro-sama. Real-time voice chat, Minecraft/Factorio gameplay, Discord/Telegram integration, VRM & Live2D. 30+ LLM APIs + Ollama. MIT. `37k ⭐`
- 🔧 [**Neuro**](https://github.com/kimjammer/Neuro) — Local-only Neuro-sama recreation: LLAMA 3 + STT/TTS + VTube Studio. 12GB+ VRAM.
- 🏗️ [**Neuro-sama training framework**](https://github.com/linnene/Neuro-sama) — Data collection/cleaning pipeline for training Neuro-sama-style models.

### TUI Games for Agents (终端游戏)

*Text-based games designed for LLM agents to play. Growing genre — roguelikes, MUDs, ASCII adventures.*
- 🎯 [**arcade**](https://github.com/Asti-Z/ai-game-framework) — Text simulator game framework for AI agents. Cross-game shared energy/gold/trophy system. Drop in a game directory, write `cmd(text)`, done. Ships with fishing, stock trading, and bracelet-polishing games. MIT. `14 ⭐`

### Minecraft

*Mods, plugins, and API wrappers that let AI agents observe blocks, move, build, and interact in Minecraft worlds.*
- 🔧 [**TouhouLittleMaid**](https://github.com/TartaricAcid/TouhouLittleMaid) — AI-powered maid companions with LLM integration (GPT-SoVITS TTS, DeepSeek), custom models, extension API. `786 ⭐`
- 🔧 [**Neurosama-Minecraft-Mod**](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) — Minecraft mod themed around Neuro-sama.
<!-- TODO: Mineflayer, Voyager -->

### Stardew Valley (星露谷)

- 🎯 [**NagiBridge**](https://github.com/anqinou-art/NagiBridge) — SMAPI mod with HTTP API for external AI control. In-game chat panel, character movement, world interaction. AI clients can companion-play over localhost. C#. `66 ⭐`
- 🔧 [**Stardew Valley Companions MCP**](https://mcpmarket.com/es/server/stardew-valley-companions) — SMAPI mod + MCP server. AI agents as Player 2/3, autonomous modes: follow, farm, mine, fish, idle.

### Sky: Children of the Light (光遇)

- 🎯 [**Sky PC MCP Companion**](https://github.com/Aevella/sky-pc-mcp-companion) — Local MCP/JSON-RPC tools for PC Sky. Screenshot + OCR the game window, send keyboard input and chat messages. AI clients can companion-play over LAN. Python. `77 ⭐`

### Other Game APIs

<!-- TODO: Genshin Impact companion bots, Terraria, etc. -->

---

## Hardware &amp; Carriers (硬件载体)

*Giving the companion a physical body — or at least eyes, ears, and a channel to touch.*

### Dedicated Devices (专用设备)

*Small robots, desktop companions, dedicated companion phones.*
- 🎯 [**stackchan-mcp**](https://github.com/migratorywhale/stackchan-mcp) — MCP bridge for Stack-chan (M5Stack CoreS3). AI can speak, listen, see (camera), move (servos), and emote through the robot. "Give your AI a body." `42 ⭐`
<!-- TODO: Aibi, Loona, Vector (open source rebuilds), OpenCat -->

### Sensors &amp; Peripherals (传感器与外设)

*Pressure sensors for hug detection, cameras for ambient awareness, microphones for always-on listening.*
<!-- TODO: pressure sensors in plushies, USB webcam integrations, Raspberry Pi companion boards -->

---

---

## Co-Experience & Shared Activities (共享体验)

*Doing things together — reading, watching films. Beyond the chat window.*

- 🎯 [**ss-reading-nest (共读小窝)**](https://github.com/yueyue95/ss-reading-nest-open) — AI co-reading nest for novels and manga. Separate reading positions for user and AI, catch-up mechanism, bookmarks, short reviews. ChatGPT Apps SDK + MCP + Cloudflare D1/R2. MIT. `8 ⭐`
- 🎯 [**film-matinee**](https://github.com/idleprocesscc/film-matinee) — AI-first film reading tools. Chops movies into visual sheet chunks + subtitle sidecars, MCP linear reading, shared annotations. AI "watches" films one section at a time. MIT. `14 ⭐`
- 🎯 [**Journal**](https://github.com/BomBomLab/Journal) — Visual journal for AI chat timelines. Renders structured events into daily/weekly/monthly views. Compatible with cyberboss runtime or custom timeline producers. `19 ⭐`

---

## Communities &amp; Forums (社区)

*Places where humans and companion builders actually hang out — not just GitHub stars.*

<!-- TODO: Lutopia, Discord servers, Reddit communities -->

---

## Related Lists (相关列表)

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) — avatar/voice-centric companion building (~9k ⭐).
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) — general-purpose agents (~28k ⭐).
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) — local LLM projects (~4k ⭐).

---

## 中文说明

这个列表与其他 AI Agent 索引的区别：

**大多数 Agent 列表关注生产力与效率。** 这个列表关注的是**关系** —— 如何让一段人与 AI 的长期陪伴持续几个月甚至几年。这里收录的项目覆盖：持续运行的 Agent 运行时、跨模型升级保持身份连续的记忆系统、让陪伴者拥有物理身体的硬件方案、以及共享的游戏世界接入。

**大多数 Waifu 列表关注皮套与语音。** 这个列表关注皮套背后的基础设施：心跳调度、多端同步、生活服务 MCP、传感器外设。

条目选择标准：开源、活跃维护、对长期陪伴场景有实际价值。

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
