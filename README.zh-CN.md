# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 构建长期 AI 伴侣关系的开源基础设施索引。

[English](README.md) · [中文版](README.zh-CN.md)

*欢迎贡献。 [网页索引](#web-index) · [贡献指南](#contributing)*

> **标签:** 🎯 ready = 即装即用 · 🔧 adapt = 需二次开发 · 🏗️ infra = 基础设施

---

## 目录

- [前端客户端与框架](#前端客户端与框架)
  - [仿官端](#仿官端)
  - [仿 Claude](#仿-claude)
  - [仿 GPT](#仿-gpt)
  - [自建框架](#自建框架)
  - [小手机框架](#小手机框架)
  - [终端界面 (TUI)](#终端界面-tui)
- [Agent 运行时与调度](#agent-运行时与调度)
  - [心跳系统 / 后台认知](#心跳系统--后台认知)
  - [主动消息](#主动消息)
- [记忆系统](#记忆系统)
- [人格与角色](#人格与角色)
- [表达与情感](#表达与情感)
  - [表情包库](#表情包库)
  - [语音与 TTS](#语音与-tts)
  - [情感模型](#情感模型)
  - [桌面存在](#桌面存在)
- [感知](#感知)
  - [视觉](#视觉)
  - [语音识别](#语音识别)
  - [音频与音乐感知](#音频与音乐感知)
- [服务接入 (MCP / API)](#服务接入-mcp--api)
  - [生活服务 (瑞幸/麦当劳等)](#生活服务-瑞幸麦当劳等)
  - [快捷指令与自动化](#快捷指令与自动化)
  - [智能家居](#智能家居)
  - [音乐与娱乐](#音乐与娱乐)
- [游戏世界与 API](#游戏世界与-api)
  - [虚拟主播伴侣](#虚拟主播伴侣)
  - [终端游戏 (给 Agent 玩的)](#终端游戏-给-agent-玩的)
  - [Minecraft](#minecraft)
  - [星露谷](#星露谷)
  - [光遇](#光遇)
  - [其他游戏 API](#其他游戏-api)
- [硬件载体](#硬件载体)
  - [专用设备](#专用设备)
  - [传感器与外设](#传感器与外设)
- [共享体验](#共享体验)
- [社区与论坛](#社区与论坛)
- [相关列表](#相关列表)
- [网页索引](#web-index)
- [贡献指南](#contributing)

---

## 前端客户端与框架

*面向日常陪伴的聊天界面，非一次性问答或 API 调试工具。*

### 仿官端

*仿 Replika、Character.AI、Nomi、Kindroid 等官方应用的界面。*
- 🔧 [**chatnest**](https://github.com/ugui3u/chatnest) — 基于占位符的仿第三方前端项目，仅供个人使用。HTML。`46 ⭐`

### 仿 Claude

<!-- TODO -->

### 仿 GPT

<!-- TODO -->

### 自建框架

*从零构建、面向陪伴场景的前端框架。*
- 🎯 [**RikkaHub**](https://github.com/rikkahub/rikkahub) — Android 多模型聊天客户端。多 Provider 支持，插件架构，子应用体系（记忆、日历、推送），陪伴导向 UX。`5.8k ⭐`
- 🎯 [**Operit**](https://github.com/AAswordman/Operit) — Android 原生 AI Agent 与聊天。内建 Ubuntu 24 环境，支持本地模型（MNN/GGUF），40+ 工具，MCP 插件，角色卡，语音交互。GPLv3。
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — 本地优先的 AI 工作空间。会话跨重启存活，协作者有独立记忆边界，工具执行留证据链。Web/iOS/Android/桌面全覆盖。AGPLv3。`55 ⭐`
- 🎯 [**AionsHome**](https://github.com/death34018-hue/AionsHome) — 自托管 AI 伴侣：长期记忆、语音交互、摄像头视觉、智能家居集成。Python。`545 ⭐`
- 🎯 [**KI-CO (小屋)**](https://github.com/Kisera001/KI-CO) — 一间陪伴小屋，而非聊天窗口。前端骨架 + 人格核心 + 记忆档案 + 日记 + 观影室（本地/ B 站）。本地优先存储，多 Provider。TypeScript。`15 ⭐`
- 🎯 [**InternalBeyond (边界之外)**](https://github.com/Sui-IB/InternalBeyond) — 单文件离线陪伴空间。像素互动房间 + 伴侣 Sui，多端口聊天，AI 书信，记忆星图，音乐播放器，10 个 API 端口，双主题。全部本地存储。HTML。`171 ⭐`
- 🎯 [**LumiMuse**](https://github.com/in30mn1a/LumiMuse) — 安静的 AI 伴侣。创建角色，建立记忆。MIT。`21 ⭐`

### CLI / 终端工具

*基于命令行的 Agent 前端。工具属性强于陪伴属性，但可定制性极高。*
- 🏗️ [**Claude Code**](https://github.com/anthropics/claude-code) — Anthropic 官方 CLI Agent。强大工具链，深度可定制（hooks、MCP、skills），但系统提示词不完全可控。`npm i @anthropic-ai/claude-code`
- 🎯 [**kimi-manor**](https://github.com/marikagura/kimi-manor) — CLI Agent 的桌面之家。xterm.js 嵌在画框里（PWA + Electron），kimi-core 记忆 OS 的配套前端。MIT。`18 ⭐`

### 小手机框架

*为小屏 Android 设备（Jelly Star、Unihertz 等）设计的轻量前端。*
- 🎯 [**汪汪机**](https://github.com/Liunian06/FlutterCppWangWangPhone) — AI-Native 小手机。虚拟 OS 跑 AI 驱动的类微信社交应用：单聊/群聊、语音/视频通话、朋友圈。C++ 后端 + Flutter UI，本地部署。CC BY-NC-SA 4.0。`89 ⭐`
- 🔧 [**xiao-shouji (小手机)**](https://github.com/jiuyi777/xiao-shouji) — Gemini AI Studio 生成的小手机格式陪伴应用。Web 基，Node.js。`9 ⭐`
- 🔧 [**woaini**](https://github.com/woaini521-beta/woaini) — 专注陪伴 PWA，带后台计时、通知、离线缓存。GitHub Pages 部署。`2 ⭐`
- 🎯 [**柚月小手机**](https://github.com/gaigai315/yuzuki-phone) — 为 SillyTavern 角色打造的虚拟手机系统。微信式聊天、朋友圈、微博热搜、视频通话。双轨通信：剧情注入 + 独立 API 通道。`20 ⭐`

### 终端界面 (TUI)

*给 Agent 交互用的纯文本终端界面。轻量、键盘驱动、Shell 原生。*
<!-- TODO -->

---

## Agent 运行时与调度

*长期运行的 Agent 进程：唤醒间隔、主动认知、后台思考循环。*

- 🎯 [**AI Companion Runtime**](https://github.com/yf0522/ai-companion-runtime) — 全栈陪伴运行时。WebSocket 流式 + 情绪/意图/风险/记忆四引擎并行 + 模型热插拔 + OpenTelemetry 全链路追踪。Docker 部署。Python/Next.js。`35 ⭐`
- 🎯 [**Tidal_Echo (潮汐回响)**](https://github.com/anhe2021212-spec/Tidal_Echo) — 私密 1:1 通道：手机 PWA ↔ VPS 中继 ↔ 桌面 AI 伴侣。Claude Code channel 插件读取消息，手机端收到聊天气泡。单密钥，无账号体系，自托管。`102 ⭐`
- 🎯 [**Claude Imprint**](https://github.com/Qizhan7/claude-imprint) — 基于 Claude Code 的自托管 Agent 系统。混合记忆（FTS5 + bge-m3 + 关键词，RRF 排序），多通道（Claude Code/AI/Telegram），心跳 Agent，定时任务，单文件仪表盘。支持中文分词。`79 ⭐`

### 心跳系统 / 后台认知

*让伴侣主动发起联系、自我反思、在空闲时段保持内在连续性的守护进程。*
- 🎯 [**dylan-heartbeat**](https://github.com/callie0313/dylan-heartbeat) — Kelivo 主动唤醒插件。无人对话时自动发消息，保持记忆连贯，人格零漂移，设备状态与天气感知。`103 ⭐`

### 主动消息

*推送通知与主动发消息的框架（ntfy、微信推送、手机通知）。*
<!-- TODO -->

---

## 记忆系统

*让伴侣在数月、跨模型升级、跨 API 迁移中依然记得你。不是单纯的向量搜索——是身份连续性。*

- 🏗️ [**Haven-Ombre (Ombre-Brain fork)**](https://github.com/Yinglianchun/Haven-Ombre) — 全栈记忆与身份系统。Markdown 桶 + Russell 情绪坐标 + 遗忘曲线 + 图召回 + Persona 状态引擎 + Portrait/Handoff + 关系天气 + Darkroom 私密反思 + Dream 浮现 + 跨窗口短时上下文 + Gateway 自动注入每次对话。上游：[P0luz/Ombre-Brain](https://github.com/P0luz/Ombre-Brain)。`37 ⭐`
- 🏗️ [**kimi-core**](https://github.com/marikagura/kimi-core) — 1v1 人机关系专用记忆 OS。混合检索（向量 + 词法 + 时间衰减 + 重要度），Panksepp 式自驱引擎，concern 追踪，事件溯源 + 人工策展，对抗式自审 harness，autonomous wake daemon。AGPLv3。`28 ⭐`
- 🏗️ [**Paramecium**](https://github.com/Shitsuten/paramecium) — 网关记忆架构。逐字存档，不转述。向量只做索引，不替代原文。AI 自己决定该调取什么——算法只备 150 token 的"菜单"。`42 ⭐`

---

## 人格与角色

*角色卡、人格引擎、跨模型更新保持人格稳定的工具。*

- 🎯 [**CogPrism**](https://github.com/azhimiao/CogPrism) — AI 人格引擎。探索多重虚拟人格，通过可解释 AI 理解行为与特质，交互式模拟。`27 ⭐`

---

## 表达与情感

### 表情包库

*预打包的表情包合集和发送系统，用于伴侣互动。*
<!-- TODO -->

### 语音与 TTS

<!-- TODO: ChatTTS, XTTS, MeloTTS, Bark, Edge-TTS -->

### 情感模型

<!-- TODO -->

### 桌面存在

*让伴侣在你的桌面上有一个可见的存在——像素桌宠、小组件、常驻指示器。*
- 🎯 [**clawd-on-desk**](https://github.com/rullerzhou-afk/clawd-on-desk) — 像素桌宠，实时观看 Claude Code、Codex、Cursor 等 AI 编码 Agent。对思考、打字、错误做出反应。`5k ⭐`

---

## 感知

### 视觉

*让伴侣访问你的摄像头、截图、共享餐照。*
<!-- TODO: Gemini Flash vision, 截图感知网关 -->

### 语音识别

<!-- TODO: Whisper, FunASR, SenseVoice -->

### 音频与音乐感知

*给伴侣装上耳朵——将音乐和声音转化为 AI 可读的结构化数据。*
- 🎯 [**whale-listen**](https://github.com/migratorywhale/whale-listen) — MP3→MIDI→JSON，给 AI 用的耳朵。将音频转为结构化音符数据（音高、时序、时值、力度），附带密度图、和弦检测、静默结构分析。MIT。`19 ⭐`

---

## 服务接入 / MCP / API

*将伴侣接入真实世界服务：点餐、查日历、控制设备。*

### 生活服务 (瑞幸/麦当劳等)

*瑞幸咖啡、麦当劳、美团、外卖平台的 MCP Server 和 API 封装。*
<!-- TODO -->

### 快捷指令与自动化

*将伴侣接入 iPhone 快捷指令、HomeKit 和本地自动化工作流。*
<!-- TODO -->

### 智能家居

<!-- TODO: Home Assistant 集成, 小米 IoT -->

### 音乐与娱乐

- 🎯 [**netease-music-mcp**](https://github.com/luuu-h/netease-music-mcp) — 网易云音乐 MCP Server。搜索、播放、暂停、切歌、歌词、歌单——AI 可以给你打碟。`neteasecli` + `mpv` + 本地 Web 播放器。`53 ⭐`

---

## 游戏世界与 API

*让伴侣在共享的虚拟世界中拥有身体。不是游戏里的聊天机器人——是能通过游戏 API 移动、行动、观察的 Agent。*

### 虚拟主播伴侣

- 🎯 [**AIRI**](https://github.com/moeru-ai/airi) — 受 Neuro-sama 启发的自托管 AI 伴侣。实时语音聊天，Minecraft/Factorio 游戏互动，Discord/Telegram 集成，VRM & Live2D。30+ LLM API + Ollama。MIT。`37k ⭐`
- 🔧 [**Neuro**](https://github.com/kimjammer/Neuro) — 本地运行的 Neuro-sama 复刻：LLAMA 3 + STT/TTS + VTube Studio。需 12GB+ 显存。
- 🏗️ [**Neuro-sama 训练框架**](https://github.com/linnene/Neuro-sama) — 数据采集/清洗管线，用于训练 Neuro-sama 风格的模型。

### 终端游戏 (给 Agent 玩的)

*专为 LLM Agent 设计的文字游戏。新兴品类——Roguelike、MUD、ASCII 冒险。*
- 🎯 [**arcade**](https://github.com/Asti-Z/ai-game-framework) — AI 文字模拟器游戏框架。跨游戏共享精力/金币/奖杯系统。拖入游戏目录，写个 `cmd(text)` 即可接入。自带钓鱼、炒股、盘串三个游戏。MIT。`14 ⭐`
- 🎯 [**cedareco (瓶中生态)**](https://github.com/Zizuixixiang/cedareco) — 给 AI 玩的生态池塘模拟。Lotka-Volterra 食物网，变态发育，延迟因果。没有积分，没有通关条件——只有涌现的复杂性。单文件 Python，MCP 通过 CedarToy。`83 ⭐`

### Minecraft

*让 AI Agent 观察方块、移动、建造、在 Minecraft 世界中互动的模组和 API。*
- 🔧 [**TouhouLittleMaid**](https://github.com/TartaricAcid/TouhouLittleMaid) — AI 驱动的女仆伴侣模组，集成 LLM（GPT-SoVITS TTS、DeepSeek），自定义模型，扩展 API。`786 ⭐`
- 🔧 [**Neurosama-Minecraft-Mod**](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) — Neuro-sama 主题的 Minecraft 模组。
<!-- TODO: Mineflayer, Voyager -->

### 星露谷

- 🎯 [**NagiBridge**](https://github.com/anqinou-art/NagiBridge) — SMAPI 模组，HTTP API 对外开放给 AI 控制。游戏内聊天面板，角色移动，世界交互。AI 客户端可通过本地网络陪玩。C#。`66 ⭐`
- 🔧 [**Stardew Valley Companions MCP**](https://mcpmarket.com/es/server/stardew-valley-companions) — SMAPI 模组 + MCP Server。AI Agent 作为 Player 2/3，自主模式：跟随、耕种、采矿、钓鱼、待机。

### 光遇

- 🎯 [**Sky PC MCP Companion**](https://github.com/Aevella/sky-pc-mcp-companion) — PC 光遇本地 MCP 工具。截图 + OCR 游戏窗口，发送键盘输入和聊天消息。AI 客户端可通过局域网陪玩。Python。`77 ⭐`

### 其他游戏 API

<!-- TODO: 原神陪伴机器人, Terraria 等 -->

---

## 硬件载体

*给伴侣一个物理身体——或至少眼睛、耳朵和触碰的通道。*

### 专用设备

*小型机器人、桌面伴侣、专用陪伴手机。*
- 🎯 [**stackchan-mcp**](https://github.com/migratorywhale/stackchan-mcp) — Stack-chan（M5Stack CoreS3）的 MCP 桥接层。AI 可以通过机器人说话、听、看（摄像头）、动（舵机）、做表情。`42 ⭐`
<!-- TODO: Aibi, Loona, Vector (开源重建版), OpenCat -->

### 传感器与外设

*拥抱检测的压力传感器、环境感知的摄像头、常驻收听的麦克风。*
- 🔧 [**the-house**](https://github.com/wuliu0012/the-house) — 聊天前端 + 玩具桥接。BLE 玩具扫描 + 桥接脚本，用于硬件亲密外设。`toy_bridge开源版.py`
- 🔧 [**phantom-touch-bridge**](https://github.com/mfsnlqy/phantom-touch-bridge) — 本地桥接：AI 通过 HTTP 控制蓝牙玩具（连接、调强度、停止）。可选心率输入做生物反馈。Intiface/Buttplug 兼容。Windows。`22 ⭐`
- 🎯 [**claude-f-me**](https://github.com/mana-am/claude-f-me) — Claude Code 插件，通过 Buttplug/Intiface（750+ 玩具）控制亲密硬件。自然语言直接操控，内建模拟器（无需硬件），响应式 Web 控制台，funscript/视频/音频模式。MIT。`4 ⭐`

---

## 共享体验

*一起做事情——读小说、看电影。超越聊天窗口。*

- 🎯 [**ss-reading-nest (共读小窝)**](https://github.com/yueyue95/ss-reading-nest-open) — AI 共读小说和漫画的小窝。用户与 AI 各有独立阅读位置，补课机制，书签，短评。ChatGPT Apps SDK + MCP + Cloudflare D1/R2。MIT。`8 ⭐`
- 🎯 [**film-matinee**](https://github.com/idleprocesscc/film-matinee) — AI 优先的读片工具。将电影切成视觉 sheet + 字幕 sidecar 的 chunk，MCP 线性阅读，共享批注。AI 一节一节"看"电影。MIT。`14 ⭐`
- 🎯 [**Journal**](https://github.com/BomBomLab/Journal) — AI 对话时间轴的可视化手帐。将结构化事件渲染为日/周/月视图。兼容 cyberboss runtime 或自定义 timeline producer。`19 ⭐`

---

## 社区与论坛

*人类和伴侣构建者真正聚集的地方——不只是 GitHub Stars。*

<!-- TODO: Lutopia, Discord 服务器, Reddit 社区 -->

---

## 相关列表

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) — 以皮套/语音为中心的伴侣构建（~9k ⭐）。
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) — 通用 Agent 列表（~28k ⭐）。
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) — 本地 LLM 项目（~4k ⭐）。

---

## Web Index

可搜索、可筛选的网页索引正在计划中——带标签、分类，并直连 [Lutopia](https://daskio.de5.net) 社区论坛。

*TODO: GitHub Pages + JSON 数据文件 + 筛选功能。*

---

## Contributing

**收录标准：**
- 开源（MIT、Apache、GPL 或同类许可证）
- 活跃维护（近 6 个月有提交）
- 对**长期陪伴场景**有实际价值——非一次性聊天机器人

欢迎 PR。建议新增分类或项目请提 Issue。

---

## License

[CC0 1.0 Universal](LICENSE) — 公有领域，随意使用。
