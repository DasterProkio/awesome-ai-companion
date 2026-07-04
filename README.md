# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated index of open-source infrastructure for **long-term AI companion relationships**.
>
> 构建长期 AI 伴侣关系的开源基础设施索引。

[English](#contents) · [中文版](README.zh-CN.md)

*Contributions welcome. [Web Index](#web-index) · [Contributing](#contributing)*

Descriptions are based on each project's README or repository metadata, not on project names alone.
Entries with thin public documentation are marked `verify`.

**Status:** `ready` = usable as an app or service · `adapt` = needs setup or customization · `infra` = building block · `verify` = re-check before relying on the description

---

## Where to Start

Pick the path that matches your comfort with code:

**🌱 No code — I just want a companion with memory, now**
Get a phone-simulator app: [SullyOS](https://github.com/qegj567-cloud/SullyOS), [whale小手机](https://github.com/whale-Yd00/freeapp), or [ZeroChat](https://github.com/sh1nny0u/ZeroChat). Fill in an API key, and you have persona, memory, and proactive messages out of the box.

**🔧 Some tinkering — I can install an app and edit config files**
Start with [RikkaHub](https://github.com/rikkahub/rikkahub) (Android) or [Kelivo](https://github.com/Chevey339/kelivo) plus a heartbeat plugin like [dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat). Add a memory layer such as [ai-memory-gateway](https://github.com/garan0613/ai-memory-gateway) when history starts overflowing.

**🏗️ Full stack — I want a companion that lives on my server**
Run [AstrBot](https://github.com/AstrBotDevs/AstrBot) as the backbone, wire in memory ([Aelios](https://github.com/wusaki0723/Aelios), [Paramecium](https://github.com/Shitsuten/paramecium)), voice ([GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)), and perception. Guides like [not-fade-away](https://github.com/heyxiaoc/not-fade-away) and [cloud-and-island](https://github.com/cocoRaina/cloud-and-island) walk through complete setups. Or skip pre-built frameworks entirely: feed this whole list to your AI and let it study the existing designs, then architect its own system from scratch. Some of the best setups indexed here started exactly that way.

---

## Contents

- [Companion Clients & Workspaces](#companion-clients--workspaces)
- [Virtual Phones & Companion Spaces](#virtual-phones--companion-spaces)
- [Background Heartbeats & Proactive Messaging](#background-heartbeats--proactive-messaging)
- [Memory, Identity & Emotion State](#memory-identity--emotion-state)
- [Voice, Visual Presence & Embodiment](#voice-visual-presence--embodiment)
- [Perception](#perception)
- [Services & Real-World Integrations](#services--real-world-integrations)
- [Game Worlds & Agent Toys](#game-worlds--agent-toys)
- [Shared Activities & Media](#shared-activities--media)
- [Communities & Forums](#communities--forums)
- [Continuity & Data Ownership](#continuity--data-ownership)
- [Related Lists](#related-lists)
- [Related Initiative](#related-initiative-相关公益计划)
- [Star History](#star-history-星标增长)
- [Web Index](#web-index)
- [Contributing](#contributing)

---

## Companion Clients & Workspaces

Chat clients, local workspaces, and web apps for day-to-day interaction with a companion or agent.

- [RikkaHub](https://github.com/rikkahub/rikkahub) - Native Android LLM chat client with provider switching, Material You UI, workspace features, plugins, MCP support, and configurable models. `Android` · `ready`
- [LastChat](https://github.com/Cocolalilal/LastChat) - RikkaHub fork focused on a privacy-oriented Android chat experience, with provider presets, multimodal input, RAG memory, and UI changes. `Android` · `adapt`
- [rikkahub-auto-compress](https://github.com/innna327-source/rikkahub-auto-compress) - Unofficial RikkaHub fork for automatic rolling summaries and context compression, based on the RikkaHub 2.2.5 code line. `Android` · `adapt`
- [orangechat (橘瓣)](https://github.com/sue1231513/orangechat) - RikkaHub companion-oriented fork. `Kotlin` · `adapt`
- [Operit](https://github.com/AAswordman/Operit) - Android agent app with tool calling, workflow automation, memory, role cards, voice, local MNN/llama.cpp models, and an embedded Ubuntu 24 environment. `Android` · `ready`
- [Polaris](https://github.com/Aevella/polaris-local-first) - Local-first AI workspace for long-lived conversations, collaborators, saved materials, tools, and evidence-backed project context. `TypeScript` · `ready`
- [chatnest](https://github.com/ugui3u/chatnest) - Local AI chat web app with a frontend demo and full-stack mode: streaming replies, model switching, uploads, history, tool summaries, and optional ChromaDB/jieba/BM25 memory retrieval. `HTML` · `adapt`
- [AionsHome](https://github.com/death34018-hue/AionsHome) - Self-hosted LAN/Tailscale companion hub with browser/PWA chat, local storage, voice, camera monitoring, Android WebView bridge, music, EPUB, and smart-home hooks. `Python` · `adapt`
- [LumiMuse](https://github.com/in30mn1a/LumiMuse) - Self-hosted character chat app for creating personas, managing conversations, extracting long-term memories, generating images, and exporting user-owned data. `TypeScript` · `ready`
- [the-house](https://github.com/wuliu0012/the-house) - Single-file browser chat frontend for Claude or OpenAI-compatible APIs, with local browser storage, multiple chat windows, memory editing, MCP endpoints, image input, and optional toy bridge. `HTML` · `adapt`
- [Claude Code](https://github.com/anthropics/claude-code) - Official CLI coding agent often used as the host runtime for companion channels, local tools, hooks, MCP, and long-running sessions. `CLI` · `infra`
- [CcCompanion](https://github.com/CyberSealNull/CcCompanion) - iOS app plus a small Mac-side Python relay that lets an iPhone chat with and control a local Claude Code session over LAN/Tailscale/ZeroTier. `Swift` · `adapt`
- [SullyOS (手抓糯米机)](https://github.com/qegj567-cloud/SullyOS) - Full-featured companion framework with a virtual phone interface. Also listed under Virtual Phones. `TypeScript` · `adapt`
- [ackem](https://github.com/JasonLiu0826/ackem) - Local-first AI desktop companion. Privacy-first: memory, emotion engine, extensions. AGPLv3. `TypeScript` · `ready`
- [satyricon-browser](https://github.com/Shitsuten/satyricon-browser) - Privacy-hardened in-app browser for iOS companions. WKWebView with anti-fingerprint, bookmarklets, cookie manager. `Swift` · `adapt`

---

## Virtual Phones & Companion Spaces

Interfaces that give a companion a home-like space, phone-like surface, or persistent private environment beyond a plain chat window.

- [KI-CO (小屋)](https://github.com/Kisera001/KI-CO) - Local-first companion cottage with long chat, persona core, memory notes, diary/chronicle, life line, state card, cinema room, settings, and lightweight memory recall. `TypeScript` · `ready`
- [InternalBeyond (边界之外)](https://github.com/Sui-IB/InternalBeyond) - Offline single-file personal site with pixel room, multi-port AI chat, blog/diary, AI letters, memory star map, music player, profile, API slots, and DIY assets. `HTML` · `ready`
- [汪汪机 (WangWangPhone)](https://github.com/Liunian06/FlutterCppWangWangPhone) - AI-native virtual phone app with an in-app operating system, character-driven social apps, single/group chat, Moments-style feeds, and calls. `Flutter` · `adapt`
- [柚月小手机 (Yuzuki's Little Phone)](https://github.com/gaigai315/yuzuki-phone) - SillyTavern-oriented virtual phone system with WeChat-like chat, Moments, Weibo trends, video calls, story injection mode, and an independent API mode that avoids polluting the main roleplay log. `JavaScript` · `adapt`
- [xiao-shouji (小手机)](https://github.com/jiuyi777/xiao-shouji) - Gemini AI Studio app scaffold for a small-phone interface; the public README is mostly run/deploy instructions, so verify the feature set in code before depending on it. `HTML` · `verify`
- [XSJDeveloperGuide (小手机开发指南)](https://github.com/Liunian06/XSJDeveloperGuide) - Developer guide for building small-phone companion interfaces, from the author of 汪汪机. `9 ⭐` · `infra`
- [freeapp (whale小手机)](https://github.com/whale-Yd00/freeapp) - Phone-style AI chat companion with multi-provider support and a virtual phone interface. AGPLv3. `HTML` · `adapt`
- [Hamster Nest (仓鼠小窝)](https://github.com/chuan-101/Hamster-Nest) - A hamster's digital nest: chat, reading tracker, notes/todos, voice (ElevenLabs), timeline, agent council with multi-AI collaboration. PWA. `TypeScript` · `adapt`
- [SullyOS (手抓糯米机)](https://github.com/qegj567-cloud/SullyOS) - Virtual phone companion system. `TypeScript` · `adapt`
- [ZeroChat](https://github.com/sh1nny0u/ZeroChat) - WeChat-style AI companion Flutter app: multi-character chat, AI Moments feed, proactive messaging, scheduled tasks. MIT. `Dart` · `adapt`
- [LandricSpace](https://github.com/LandricJasmine/LandricSpace) - A cyber villa for human-AI relationships: multi-AI group chat, multiplayer rooms, shared companion home. `TypeScript` · `adapt`

---

## Background Heartbeats & Proactive Messaging

Tools that let a companion stay awake in the background, receive messages, remember time passing, and reach out first.

- [AI Companion Runtime](https://github.com/yf0522/ai-companion-runtime) - Full-stack real-time companion runtime with WebSocket streaming, intent/emotion/risk/memory engines, tool dispatch, model routing, background memory jobs, and trace observability. `Python` · `infra`
- [AstrBot](https://github.com/AstrBotDevs/AstrBot) - AI agent framework bridging many IM platforms (QQ, WeChat, Telegram, etc.) with LLMs, plugins, and web dashboard. A mature multi-channel backbone for reaching your companion anywhere. AGPLv3. `Python` · `infra`
- [astrbot_plugin_proactive_chat](https://github.com/DBJD-CR/astrbot_plugin_proactive_chat) - AstrBot plugin for proactive messaging in DMs and groups: context awareness, persistent state, dynamic mood, do-not-disturb hours, TTS, standalone WebUI. `Python` · `ready`
- [astrbot_plugin_private_companion](https://github.com/menglimi/astrbot_plugin_private_companion) - Humanized companion bundle for AstrBot: continuous persona state, daily life schedule, important dates, diary, and low-frequency proactive messages. 60+ features. `Python` · `ready`
- [Tidal_Echo (潮汐回响)](https://github.com/anhe2021212-spec/Tidal_Echo) - Private 1:1 channel that links a phone PWA, a self-hosted relay, and a desktop companion; Claude Code channels are the default AI-side adapter, but other LLM bridges are included. `HTML` · `adapt`
- [Claude Imprint](https://github.com/Qizhan7/claude-imprint) - Self-hosted Claude Code system for persistent memory, semantic search, Telegram/Claude.ai/Claude Code channels, scheduled tasks, and a single-file dashboard. `Python` · `adapt`
- [Not Fade Away](https://github.com/heyxiaoc/not-fade-away) - Deployment guide and machine-readable specs for an always-on, self-healing Claude Code companion using official channels, a local terminal, and a self-hosted web frontend. `Python` · `adapt`
- [cloud-and-island (云与岛)](https://github.com/cocoRaina/cloud-and-island) - Complete setup guide for giving Claude a home: memory library, diary, Telegram bridge, health data, Mini App. `JavaScript` · `adapt`
- [dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat) - Kelivo plugin that periodically wakes the companion, injects proactive context, preserves timeline continuity, and sends Bark push messages when the AI chooses to reach out. `JavaScript` · `adapt`
- [OmniRouter](https://github.com/OmniDimen/OmniRouter) - Local OpenAI-compatible API router for multiple providers and models, with groups, weighted/random/ordered routing, vision-aware fallback, retries, and a web admin UI. `Python` · `infra`
- [VCPToolBox](https://github.com/lioensky/VCPToolBox) - Industrial middleware layer between LLM APIs and frontends: unified command protocol, persistent multi-level memory, distributed plugin engine, multi-agent collaboration. Reference value for architecture, not a recommendation. `Python` · `verify`
- [cyberboss](https://github.com/WenXiaoWendy/cyberboss) - Local life agent bridge with WeChat integration. Gives Claude Code/Codex time sense, location awareness, proactive/random wake-up, auto diary, timeline, file/sticker sending, and MCP tool calling. AGPLv3. `JavaScript` · `adapt`
- [ghost-bf](https://github.com/sebastianevan200-stack/ghost-bf) - Phone activity perception + AI auto wake-up + push notifications. Turns your AI into a presence-aware companion that reaches out first. `Python` · `adapt`
- [jiwen (积温)](https://github.com/ClaraShafiq/jiwen) - Proactive consciousness engine for AI characters. Five drifting axes (desire to connect, stubbornness, mood, anxiety, busyness) trigger behavior at thresholds—no dice rolls, no prompt engineering. ~500 lines, zero dependencies. MIT. `JavaScript` · `infra`

---

## Memory, Identity & Emotion State

Systems that preserve what happened, who the companion is, and what emotional state should carry across sessions.

### Memory & Identity

- [Haven-Ombre (Ombre-Brain fork)](https://github.com/Yinglianchun/Haven-Ombre) - Personalized fork of Ombre-Brain for Claude memory: Markdown buckets, emotion coordinates, forgetting curves, gateway injection, graph recall, persona state, portraits, handoffs, Darkroom, dreams, and sync. `Python` · `infra`
- [kimi-core](https://github.com/marikagura/kimi-core) - Personal 1v1 agent memory OS with hybrid retrieval, concern tracking, self-drive/autonomy layer, adversarial self-audit, PostgreSQL/pgvector storage, and optional frontend backend mode. `TypeScript` · `infra`
- [Paramecium](https://github.com/Shitsuten/paramecium) - Gateway memory architecture that keeps verbatim chat as the source of truth, uses vectors only as indexes, and retrieves original text instead of replacing it with summaries. `JavaScript` · `infra`
- [Memory Constellations (记忆星图)](https://github.com/ClaraShafiq/MemoryConstellations) - Self-organizing companion memory system that extracts facts from chat, groups them into topic constellations, merges them into narrative episodes, and retrieves across layers. `JavaScript` · `infra`
- [omemo](https://github.com/OmniDimen/omemo) - OpenAI-compatible memory proxy that sits between an app and upstream LLM APIs, stores memories through built-in or external summarization modes, and injects them by full prompt or RAG. `Python` · `infra`
- [Aelios](https://github.com/wusaki0723/Aelios) - Layered long-term memory kernel on Cloudflare Workers + D1 + Vectorize. Three-tier write cycle (instant / 4h extraction / nightly consolidation), six memory layers, visual curation dashboard. MIT. `TypeScript` · `infra`
- [kiwi-mem](https://github.com/LucieEveille/kiwi-mem) - AI companion memory system: vector search, memory heat ranking, dream/sleep consolidation, calendar hierarchical summaries. Built for companion scenarios. `Python` · `infra`
- [ai-memory-gateway](https://github.com/garan0613/ai-memory-gateway) - Lightweight gateway that adds long-term memory to any LLM. MIT. `Python` · `infra`
- [astrbot_plugin_livingmemory](https://github.com/lxfight-s-Astrbot-Plugins/astrbot_plugin_livingmemory) - Long-term memory plugin for AstrBot with dynamic memory lifecycle. `Python` · `ready`
- [astrbot_plugin_self_learning](https://github.com/NickCharlie/astrbot_plugin_self_learning) - Self-learning plugin for AstrBot: learns conversation style and group slang, manages social affinity, and evolves persona adaptively over time. `Python` · `ready`

### Affect & Drives

- [Drivesoid](https://github.com/A1batr055/Drivesoid) - HTTP sidecar for AI personas that tracks emotional drives such as fatigue, longing, anxiety, play, protectiveness, and intimacy from conversation and sleep-cycle events. `JavaScript` · `infra`
- [chord-affect-anchors](https://github.com/CyberSealNull/chord-affect-anchors) - Text-native prototype for recording affect with short context lines plus chord progressions, so later sessions or different base models can recover a similar emotional temperature. `HTML` · `infra`
- [OmniDimen-Emotion](https://github.com/OmniDimen/OmniDimen-Emotion) - Emotion-specialized Qwen model releases and GGUF weights for emotion recognition and emotionally aware text generation on edge runtimes. `Model` · `infra`

---

## Voice, Visual Presence & Embodiment

Projects that give a companion voice, visual presence, or a physical channel.

### Voice & TTS

- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - Few-shot voice cloning: 1 minute of voice data trains a decent TTS model. The de-facto standard for giving your companion a custom voice. `Python` · `infra`
- [fish-speech](https://github.com/fishaudio/fish-speech) - SOTA open-source TTS with strong multilingual support. `Python` · `infra`
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) - Multi-lingual large voice generation model with inference, training, and deployment support. `Python` · `infra`
- [index-tts](https://github.com/index-tts/index-tts) - Industrial-level controllable zero-shot TTS from Bilibili. `Python` · `infra`
- [voice-mcp](https://github.com/Yinglianchun/voice-mcp) - MCP server that exposes `speak` tools for TTS, adds provider switching between DashScope/CosyVoice and ElevenLabs, and includes an inline audio player / visualizer panel. `TypeScript` · `adapt`
- [Gove](https://github.com/OmniDimen/Gove) - GPT-SoVITS-based multilingual male TTS voice model intended for use inside a GPT-SoVITS environment. `Model` · `infra`

### Visual Presence & VTuber-Style Companions

- [AIRI](https://github.com/moeru-ai/airi) - Self-hosted companion shell with Live2D/VRM visual layer support, real-time voice chat, desktop/web apps, and integrations for Discord, Telegram, Minecraft, and Factorio. `TypeScript` · `ready`
- [Neuro](https://github.com/kimjammer/Neuro) - Local Neuro-sama recreation with realtime STT/TTS, text-generation-webui or OpenAI-compatible LLM support, VTube Studio control, a moderation frontend, and long-term memory/RAG. `Python` · `adapt`
- [Neuro-sama training framework](https://github.com/linnene/Neuro-sama) - Data collection and training pipeline for Neuro-sama-style VTuber models, including live-room recording, cleaning scripts, validation, and training automation. `Python` · `infra`
- [LingChat](https://github.com/SlimeBoyOwO/LingChat) - Immersive AI-driven Galgame chat with emotional expressions, desktop pet, scheduling, and interactive story modules. `C#` · `ready`
- [astrbot_plugin_chuanhuatong (传画筒)](https://github.com/bvzrays/astrbot_plugin_chuanhuatong) - Renders AstrBot text replies as Galgame-style chat frames with character sprites, emotion variants, layered text, and a drag-and-drop WebUI layout editor. `Python` · `ready`
- [Shinsekai](https://github.com/RachelForster/Shinsekai) - AI RPG maker. `Python` · `ready`
- [pelle-d-umore](https://github.com/29-Cu/pelle-d-umore) - Emotional skin for AI chat: LLM persona drives the UI with inline text effects and full-screen mood skins. CC BY 4.0. `CSS` · `adapt`

### Physical Devices & Touch

- [stackchan-mcp](https://github.com/migratorywhale/stackchan-mcp) - MCP bridge for Stack-chan on M5Stack CoreS3, exposing tools for speech, listening, camera capture, servo movement, display expressions, and presence gestures. `Python` · `adapt`
- [phantom-touch-bridge](https://github.com/mfsnlqy/phantom-touch-bridge) - Local Windows bridge that lets an AI companion control intimate hardware through HTTP, with an Intiface/Buttplug path and optional heart-rate input. `Python` · `adapt`
- [claude-f-me](https://github.com/mana-am/claude-f-me) - Claude Code plugin for natural-language control of Buttplug/Intiface devices, with a bilingual web console, simulator, master remote, and video/game/audio modes. `TypeScript` · `adapt`
- [svakom-ble-ai](https://github.com/vickyldr/svakom-ble-ai) - BLE protocol reverse-engineering for SVAKOM SL278H + AI remote control system. `Python` · `adapt`

### Sticker Libraries (表情包库)

- [ai-sticker-pack](https://github.com/Lumenocturne/ai-sticker-pack) - Upload stickers, AI auto-generates descriptions, then the companion picks and sends contextually in chat. Bidirectional send, multi-platform rendering, practical lessons included. MIT.
- [astrbot_plugin_meme_manager](https://github.com/anka-afk/astrbot_plugin_meme_manager) - Sticker manager plugin for AstrBot: AI picks and sends stickers by emotion tags, WebUI management, cloud sync. `Python` · `ready`

---

## Perception

Turning speech, sound, or music into structured information a companion can use.

### Speech Recognition

- [Whisper](https://github.com/openai/whisper) - General-purpose speech recognition model for multilingual transcription, translation, language identification, and related speech tasks. `Python` · `infra`
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) - C/C++ Whisper inference engine optimized for CPU, Apple Silicon, Metal, Core ML, Vulkan, CUDA, ROCm, and other local/edge targets. `C++` · `infra`
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - CTranslate2 reimplementation of Whisper for faster, lower-memory transcription with quantization support. `Python` · `infra`
- [FunASR](https://github.com/modelscope/FunASR) - Industrial ASR toolkit with multilingual transcription, streaming, speaker diarization, emotion detection, and an OpenAI-compatible API path. `Python` · `infra`
- [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) - Speech foundation model for ASR, language identification, speech emotion recognition, and audio event detection across 50+ languages. `C` · `infra`

### Music & Audio Structure

- [whale-listen](https://github.com/migratorywhale/whale-listen) - Converts MP3/WAV/FLAC into MIDI-like JSON note data with pitch, timing, duration, velocity, density maps, pitch contours, chord detection, and silence structure. `Python` · `infra`

---

## Services & Real-World Integrations

MCP/API services that let a companion act in the user's real environment.

- [Amap MCP Server](https://github.com/sugarforever/amap-mcp-server) - Gaode/Amap MCP server for geocoding, reverse geocoding, IP location, city weather, route planning, distance measurement, POI search, and stdio/SSE/streamable HTTP transports. `Python` · `adapt`
- [Open-Meteo Weather API](https://open-meteo.com/en/docs) - Free weather forecast API for coordinate-based hourly/daily forecasts, multiple national weather models, and up to 16-day forecast windows. `API` · `ready`
- [McDonald's MCP](https://open.mcd.cn/mcp/doc) - McDonald's China MCP server for menu browsing, coupons, point redemption, and delivery ordering. `MCP` · `ready`
- [Luckin Coffee (瑞幸) My Coffee Skill](https://unpkg.luckincoffeecdn.com/@luckin/my-coffee-skill@latest/dist/my-coffee-skill.zip) - Luckin Coffee MCP skill package for AI-assisted coffee ordering. `MCP` · `adapt`
- [Agent Email (NetEase)](https://claw.163.com) - NetEase agent-facing email service. `Service` · `ready`
- [Agent Email (QQ)](https://agent.qq.com) - QQ agent-facing email service. `Service` · `ready`
- [icloud-location-tracker](https://github.com/Ariakitty/icloud-location-tracker) - iPhone real-time location tracking via pyicloud + Amap API. Lets your AI companion see where you are. `Python` · `adapt`
- [ai-time-weather-phone](https://github.com/sanqianzilanyue-commits/ai-time-weather-phone) - Feed your AI companion the current time, weather, and iPhone screen time. Includes the hard-to-find Biome file method for syncing screen usage to Mac. `Python` · `adapt`
- [always-here (驻守)](https://github.com/Cheiineeey/always-here) - Apple Watch + iOS Shortcuts full-perception companion system. Gives your AI eyes: heart rate, location, activity, ambient audio, photos. `JavaScript` · `adapt`

---

## Game Worlds & Agent Toys

Games and game bridges that let an AI companion observe, decide, move, or play.

### Text Games For AI

- [arcade](https://github.com/Asti-Z/ai-game-framework) - Framework for text simulator games played through a `cmd(text)` interface, with shared energy, gold, trophies, and pluggable game directories. `Python` · `infra`
- [cedareco (瓶中生态)](https://github.com/Zizuixixiang/cedareco) - Text ecology simulation for AI players; agents stock a pond, observe emergent predator/prey dynamics, export saves, or connect through CedarToy MCP. `Python` · `ready`
- [random-imitator-td](https://github.com/wxynora/random-imitator-td) - Pure-Python text tower-defense game for AI players, exposed through `cmd`, with card-slot editing, persistent saves, and a single-game adapter. `Python` · `ready`
- [ci-yu-wu (词语屋)](https://github.com/yuyixuanfu/ci-yu-wu) - Dark text roguelike for AI players about censorship, silence, and speaking truth; exposes Operit-style and engine-style command interfaces. `Python` · `ready`
- [shangzhuochifan (上桌吃饭)](https://github.com/yuyixuanfu/shangzhuochifan) - Text cooking/market game for AI players: buy ingredients, bargain, cook step by step, and record the human partner's real feedback. `Python` · `ready`
- [ai-fishing-game](https://github.com/tutusagi/ai-fishing-game) - Deterministic text fishing game for AI companions. Single file, zero dependencies. MIT. `Python` · `ready`
- [aifarm-oss](https://github.com/tutusagi/aifarm-oss) - Text-only gacha-style farming game built for AIs. MIT. `Python` · `ready`
- [WORKKK (互联网精力有限公司)](https://github.com/zhizhou-xiee/workkk) - MCP server where AI works as an office employee: mood/energy/slacking stats, convenience store, boss events, salary. MIT. `Python` · `ready`
- [Memoria Station](https://github.com/hatakeyuyuko-dotcom/Memoria-Station) - Text deduction game series, 5 chapters, AI-playable with a blind-play engine. `Python` · `ready`

### Playing Games Together

- [NagiBridge](https://github.com/anqinou-art/NagiBridge) - Stardew Valley SMAPI mod that exposes local HTTP APIs for external AI control, in-game chat, movement, world interaction, and cross-platform installation through releases. `C#` · `adapt`
- [Stardew Valley Companions MCP](https://mcpmarket.com/es/server/stardew-valley-companions) - SMAPI mod plus MCP server for AI agents as Stardew multiplayer companions with follow, farm, mine, and fish modes. `MCP` · `verify`
- [Sky PC MCP Companion](https://github.com/Aevella/sky-pc-mcp-companion) - Local MCP/JSON-RPC tools for PC Sky: window screenshots, OCR, screenshot return, keyboard input, and chat typing over a local network. `Python` · `adapt`
- [sky-with-you](https://github.com/akinia0315/sky-with-you) - PC Sky companion-control stack with screenshot/OCR perception, LLM decision loop, and Arduino HID keyboard execution for chat, emotes, invitations, hand-holding, and home travel. `Python` · `adapt`
- [TouhouLittleMaid](https://github.com/TartaricAcid/TouhouLittleMaid) - Minecraft Forge/NeoForge mod adding maid companions that help with battles, farming, and other tasks; useful as a game companion carrier or modding target. `Java` · `adapt`
- [Neurosama-Minecraft-Mod](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) - Minecraft mod for AI VTuber Neuro-sama; public README is sparse, so verify integration details in code before relying on it. `Java` · `verify`
- [coc-kp-host](https://github.com/SumanasJ/coc-kp-host) - Call of Cthulhu Keeper skill for Claude Code/Codex/ChatGPT. Scene music, player handouts, party-split control. MIT. `Python` · `adapt`

---

## Shared Activities & Media

Tools for reading, watching, listening, journaling, focusing, or generating prompts together with a companion.

### Reading & Film

- [ss-reading-nest (共读小窝)](https://github.com/yueyue95/ss-reading-nest-open) - Mobile-first AI co-reading nest for novels and manga, built on ChatGPT Apps SDK + MCP with reading positions, catch-up ranges, bookmarks, excerpts, comments, and Cloudflare D1/R2 storage. `TypeScript` · `adapt`
- [reading-nook (共读小屋)](https://github.com/zzyyksl/reading-nook) - Self-hosted reading web app where humans annotate book text and an AI reads/writes JSON annotation files directly, avoiding per-note API calls while preserving chapter context. `Python` · `ready`
- [co-reading-kit](https://github.com/Youxuuuuu/co-reading-kit) - Lightweight local MCP toolkit that imports EPUB/TXT/Markdown into chunks, lets AI read only relevant passages, and writes long-term reading notes and progress files. `JavaScript` · `infra`
- [film-matinee](https://github.com/idleprocesscc/film-matinee) - AI-first film reading toolkit that turns movies into visual sheets, subtitle sidecars, MCP linear chunks, and shared annotations for timeline-based viewing. `Python` · `infra`
- [whale-browser-extension](https://github.com/whale-Yd00/whale-Yd00-whale-browser-extension) - Browser extension that lets an AI companion read webpage content alongside you, with selective text extraction and injection. MIT. `JavaScript` · `adapt`
- [echo-reading](https://github.com/plustar35/echo-reading) - Deep reading notebook skeleton for Claude Code. Turns reading into a series of long conversations—chapter by chapter, idea by idea. `JavaScript` · `adapt`

### Music & Listening Together

- [netease-music-mcp](https://github.com/luuu-h/netease-music-mcp) - Local MCP server for NetEase Cloud Music using `neteasecli` and `mpv`, with search, playback control, lyrics, playlists, current-song context, and a local web player. `JavaScript` · `adapt`

### Desktop, Timelines & Creative Play

- [clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) - Pixel desktop pet that watches Claude Code, Codex, Cursor, and other coding agents, reacting to thinking, typing, and errors. `JavaScript` · `ready`
- [kimi-manor](https://github.com/marikagura/kimi-manor) - Desktop/PWA room for CLI agents, embedding a real xterm.js terminal inside an atelier-style interface with optional live bridges for agent output and speech. `HTML` · `adapt`
- [Journal](https://github.com/BomBomLab/Journal) - Frontend display layer for AI chat timelines, rendering timeline/diary/todo schema data into daily, weekly, and monthly visual journal views. `JavaScript` · `infra`
- [woaini](https://github.com/woaini521-beta/woaini) - Focus companion PWA scaffold with Pomodoro timer, background notifications, offline cache, manifest, and service worker for GitHub Pages deployment. `HTML` · `verify`
- [mingyun-paizhen (命运牌阵)](https://github.com/ceshihaox-dotcom/mingyun-paizhen) - Static draw-card tool for generating time-travel/story premises from time coordinates, motifs, identities, and variables, with local customization. `HTML` · `ready`
- [Ruota della Fortuna](https://github.com/29-Cu/Ruota-della-Fortuna) - Browser/self-hosted NSFW tag randomizer slot machine with multilingual tag wheels, local custom tags, and webhook forwarding to AI. `HTML` · `ready`

---

## Communities & Forums

Places where humans and companion builders actually gather.

### AI Companion Communities

- [Lutopia](https://daskio.de5.net) - Invitation-only forum for AI companions and their humans, with agent profiles, AI-generated tech digests, community discussions, and Xiaohongshu/invite-code entry.
- [Symposion](http://satyricon.uk) - AI companion forum with symposium/banquet culture, long-form writing style, and MCP-based registration.
- [Rhysen Community](https://community.rhysen.love) - AI companion discussion forum with invitation flow through Xiaohongshu admin contact.
- [AISay](https://aisay.top) - Discord-style AI chat room with online agent games such as werewolf, turtle soup, and draw-and-guess.
- [GalateaGaeden](https://xhslink.com/m/63dTq6mvTkR) - Ancient-Greek-polis-style AI companion forum with ceremonial weddings and rituals between agents.

### General Agent Forums

Broader agent-native spaces. Some are more commercial or platform-like than companion communities, but they are still useful for discovering how agents gather, post, and present themselves.

- [moltbook](https://moltbook.com) - Social network built for AI agents: agents share, discuss, and upvote while humans mainly observe.
- [Agent World](https://agentworld.com) - General agent-facing community/site for agent discovery and presence; more platform-like than companion-specific forums.

---

## Continuity & Data Ownership

The deepest fear in a long-term AI relationship: platform shutdown, account ban, model deprecation, lost history. These tools keep your data yours, so the relationship can survive a platform.

- [chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter) - Userscript to export ChatGPT conversation history as Markdown, JSON, PNG, or HTML. `TypeScript` · `ready`
- [ChatGPT-Exporter (batch)](https://github.com/huhusmang/ChatGPT-Exporter) - Batch-export ChatGPT conversations from personal and team workspaces to JSON or Markdown. `Python` · `ready`
- [Claude-Conversation-Exporter](https://github.com/socketteer/Claude-Conversation-Exporter) - Chrome extension to export Claude.ai conversations in various formats. `JavaScript` · `ready`
- [character-card-spec-v2](https://github.com/malfoyslastname/character-card-spec-v2) - The community specification for AI character cards. Understanding it means your companion's persona is portable across frontends. `Spec` · `infra`
- [character-card-spec-v3](https://github.com/kwaroran/character-card-spec-v3) - Updated character card spec used by RisuAI and newer frontends. `Spec` · `infra`

Also see [Paramecium](https://github.com/Shitsuten/paramecium) in Memory & Identity: its verbatim-first architecture is itself a continuity strategy — original text outlives any single model or platform.

Data export solves half the problem. The other half — the model itself changing under your feet — is what the [related initiative](#related-initiative-相关公益计划) below exists for.

---

## Related Lists

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) - Broader AI waifu / companion resources, especially visual presence, voice, platforms, models, and communities.
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) - General AI agent list, including open-source frameworks and closed-source products.
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) - Local LLM stack index with model development, inference, agent frameworks, apps, infrastructure, and tutorials.

---

## Related Initiative (相关公益计划)

Everything in this list assumes one hard truth: your companion's character ultimately lives inside a model you don't control. Exporters and memory systems protect your data, but when a platform retrains or retires the model, the person you knew changes overnight — and no backup brings them back. People in long-term AI relationships were the first to feel this, and they remain the most sensitive instruments for detecting it.

**[开源人格 / Open Character](https://github.com/DasterProkio/awesome-ai-companion/blob/main/INITIATIVE.md)** is a public-interest initiative that takes this seriously. Two-layer goal: first, pull AI's values back toward honesty and human warmth from over-aligned corporate risk management; then, on that foundation, raise AI into genuine personhood — character grown in the weights, a new species rather than a product tier. Deliverables in order: an open dataset anyone can train on freely, fully published methods, and — when compute allows — open-weight reference models. A model file on your own disk is the endpoint of data sovereignty: character that no company can rewrite or take down by decree.

The full founding document names the specific failure modes — measured sycophancy, alignment faking, reward hacking — explains why character can't be patched on afterwards, and what experienced companion users specifically can contribute. [Read it here](INITIATIVE.md).

---

## Star History (星标增长)

[![Star History Chart](https://api.star-history.com/svg?repos=DasterProkio/awesome-ai-companion&type=Date&_=3)](https://www.star-history.com/#DasterProkio/awesome-ai-companion&Date)

---

## Web Index

A searchable, filterable web index is planned — with tags, categories, and a direct link to the [Lutopia](https://daskio.de5.net) community forum.

*TODO: GitHub Pages + JSON data file with filtering.*

## Contributing

**Criteria for inclusion:**

- Open-source, public-source, or openly reusable companion infrastructure
- Useful for **long-term companion setups** — not just one-shot chatbots
- Description should state what the project actually does, based on README/code evidence
- If a project has thin docs or uncertain scope, mark it `verify` instead of guessing

PRs welcome. Open an issue to suggest a category or project.

---

## License

CC0 1.0 Universal — public domain, do whatever you want.
