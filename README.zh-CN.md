# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 构建长期 AI 伴侣关系的开源基础设施索引。

[English](README.md) · [中文版](README.zh-CN.md)

*欢迎贡献。 [网页索引](#web-index) · [贡献指南](#contributing)*

> **标签:** 🎯 ready = 即装即用 · 🔧 adapt = 需二次开发 · 🏗️ infra = 基础设施

---

## 目录

- [前端客户端与框架](#前端客户端与框架)
  - [仿 C 端](#仿-c-端)
  - [仿 GPT](#仿-gpt)
  - [自建框架](#自建框架)
  - [手机模拟器](#手机模拟器)
  - [CLI / 终端工具](#cli--终端工具)
  - [终端界面 (TUI)](#终端界面-tui)
- [后台运行与主动消息](#后台运行与主动消息)
  - [心跳系统](#心跳系统)
- [记忆与人格](#记忆与人格)
- [表达与情感](#表达与情感)
  - [表情包库](#表情包库)
  - [语音与 TTS](#语音与-tts)
  - [虚拟形象与语音](#虚拟形象与语音)
  - [情感模型](#情感模型)
- [感知](#感知)
  - [语音识别](#语音识别)
  - [音频与音乐感知](#音频与音乐感知)
- [服务接入 (MCP / API)](#服务接入-mcp--api)
  - [生活服务](#生活服务)
  - [快捷指令与自动化](#快捷指令与自动化)
  - [智能家居](#智能家居)
  - [音乐与娱乐](#音乐与娱乐)
- [游戏世界与 API](#游戏世界与-api)
  - [终端游戏](#终端游戏)
  - [Minecraft](#minecraft)
  - [星露谷](#星露谷)
  - [光遇](#光遇)
  - [其他游戏 API](#其他游戏-api)
- [硬件载体](#硬件载体)
  - [专用设备](#专用设备)
  - [传感器与外设](#传感器与外设)
- [共享活动与桌宠](#共享活动与桌宠)
- [社区与论坛](#社区与论坛)
- [相关列表](#相关列表)
- [星标增长](#星标增长)
- [网页索引](#web-index)
- [贡献指南](#contributing)

---

## 前端客户端与框架

*面向日常陪伴的聊天界面，非一次性问答或 API 调试工具。*

### 仿 C 端

*仿 Claude.ai 聊天体验的前端界面。*
- 🔧 [**chatnest**](https://github.com/ugui3u/chatnest) — 基于占位符的仿第三方前端项目，仅供个人使用。HTML。`46 ⭐`

### 仿 GPT

<!-- TODO -->

### 自建框架

*从零构建、面向陪伴场景的前端框架。*
- 🎯 [**RikkaHub**](https://github.com/rikkahub/rikkahub) — Android 多模型聊天客户端。多 Provider，插件架构，子应用体系。`5.8k ⭐`
- 🎯 [**LastChat**](https://github.com/Cocolalilal/LastChat) — RikkaHub 二改版，更深安卓本地集成，更流畅 Material Design UI，可滚动记忆库，更新比 RikkaHub 勤快。`268 ⭐`
- 🔧 [**rikkahub-auto-compress**](https://github.com/innna327-source/rikkahub-auto-compress) — RikkaHub 二改版，加入陪伴功能：后台任务、使用统计、更多权限。`2 ⭐`
- 🎯 [**Operit**](https://github.com/AAswordman/Operit) — Android 原生 AI Agent 与聊天。内建 Ubuntu 24 环境，支持本地模型（MNN/GGUF），40+ 工具，MCP 插件，角色卡，语音。GPLv3。
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — 本地优先的 AI 工作空间。会话跨重启存活，协作者独立记忆边界，工具留证据链。Web/iOS/Android/桌面。AGPLv3。`55 ⭐`
- 🎯 [**AionsHome**](https://github.com/death34018-hue/AionsHome) — 自托管 AI 伴侣：长期记忆、语音交互、摄像头视觉、智能家居。Python。`545 ⭐`
- 🎯 [**KI-CO (小屋)**](https://github.com/Kisera001/KI-CO) — 一间陪伴小屋。人格核心 + 记忆档案 + 日记 + 观影室（本地/B 站）。本地优先，多 Provider。TypeScript。`15 ⭐`
- 🎯 [**InternalBeyond (边界之外)**](https://github.com/Sui-IB/InternalBeyond) — 单文件离线陪伴空间。像素房间、多端口聊天、AI 书信、记忆星图、音乐播放器、10 个 API 端口。HTML。`171 ⭐`
- 🎯 [**LumiMuse**](https://github.com/in30mn1a/LumiMuse) — 安静的 AI 伴侣。创建角色，建立记忆。MIT。`21 ⭐`

### 手机模拟器

*虚拟手机环境，AI 通过模拟的手机界面进行互动——共享相册、转账、社交应用，全在沙盒手机 UI 里。不是屏幕大小的问题，是给 AI 一个手机住进去。*
- 🎯 [**汪汪机**](https://github.com/Liunian06/FlutterCppWangWangPhone) — AI 原生虚拟手机。完整 OS 跑 AI 驱动的类微信社交：聊天、朋友圈、语音/视频通话。C++ 后端 + Flutter UI。CC BY-NC-SA 4.0。`89 ⭐`
- 🎯 [**柚月小手机**](https://github.com/gaigai315/yuzuki-phone) — 为 SillyTavern 角色打造的虚拟手机。微信式聊天、朋友圈、微博热搜、视频通话。双轨：剧情注入 + 独立 API。`20 ⭐`
- 🔧 [**xiao-shouji (小手机)**](https://github.com/jiuyi777/xiao-shouji) — Gemini AI Studio 手机模拟器。Web 基，Node.js。`9 ⭐`
- 🎯 [**Polaris**](https://github.com/Aevella/polaris-local-first) — 同时见自建框架。跨平台工作空间，原生 iOS/Android shell，可作手机伴侣。

### CLI / 终端工具

*基于命令行的 Agent 前端。工具属性强于陪伴属性，可定制性高。*
- 🏗️ [**Claude Code**](https://github.com/anthropics/claude-code) — Anthropic 官方 CLI Agent。强大工具链，深度可定制（hooks、MCP、skills），系统提示词不完全可控。
- 🎯 [**CcCompanion**](https://github.com/CyberSealNull/CcCompanion) — Claude Code 非官方 iOS 伴侣。自托管中继，本地优先聊天、搜索、会话控制。MIT。`166 ⭐`

### 终端界面 (TUI)

*给 Agent 用的纯文本终端交互界面。轻量、键盘驱动、Shell 原生。*
<!-- TODO -->

---

## 后台运行与主动消息

*长期运行的 Agent 进程：唤醒间隔、主动认知、后台思考、推送通知。*

- 🎯 [**AI Companion Runtime**](https://github.com/yf0522/ai-companion-runtime) — 全栈陪伴运行时。WebSocket 流式 + 情绪/意图/风险/记忆四引擎并行 + 模型热插拔 + OpenTelemetry 追踪。Docker。Python/Next.js。`35 ⭐`
- 🎯 [**Tidal_Echo (潮汐回响)**](https://github.com/anhe2021212-spec/Tidal_Echo) — 私密 1:1 通道：手机 PWA ↔ VPS 中继 ↔ 桌面伴侣。单密钥，自托管。`102 ⭐`
- 🎯 [**Claude Imprint**](https://github.com/Qizhan7/claude-imprint) — 基于 Claude Code 的自托管 Agent。混合记忆，多通道（Claude Code/AI/Telegram），心跳 Agent，定时任务，仪表盘。支持中文分词。`79 ⭐`
- 🏗️ [**OmniRouter**](https://github.com/OmniDimen/OmniRouter) — 大模型智能路由器，面向陪伴系统的请求调度。
- 🎯 [**Not Fade Away**](https://github.com/heyxiaoc/not-fade-away) — 在自己 Mac 上搭常驻、自愈、走订阅、墙内可用的自托管 AI 伴侣。人看版讲思路，机看版给完整规格。`62 ⭐`

### 心跳系统

*让伴侣主动发起联系、在空闲时段保持内在连续性的守护进程。*
- 🎯 [**dylan-heartbeat**](https://github.com/callie0313/dylan-heartbeat) — Kelivo 主动唤醒插件。无人对话时自动发消息，记忆连贯，人格零漂移，设备状态与天气感知。`103 ⭐`

---

## 记忆与人格

*身份连续性——伴侣记住什么、是谁。这些项目把记忆和人格视为同一枚硬币的两面。*

- 🏗️ [**Haven-Ombre (Ombre-Brain fork)**](https://github.com/Yinglianchun/Haven-Ombre) — 全栈记忆与身份：Markdown 桶 + Russell 情绪坐标 + 遗忘曲线 + 图召回 + Persona 状态引擎 + Portrait/Handoff + 关系天气 + Darkroom + Dream 浮现 + Gateway 自动注入。上游：[P0luz/Ombre-Brain](https://github.com/P0luz/Ombre-Brain)。`37 ⭐`
- 🏗️ [**kimi-core**](https://github.com/marikagura/kimi-core) — 1v1 关系专用记忆 OS。混合检索（向量 + 词法 + 时间衰减 + 重要度），Panksepp 自驱引擎，concern 追踪，事件溯源 + 人工策展，对抗式自审。AGPLv3。`28 ⭐`
- 🏗️ [**Paramecium**](https://github.com/Shitsuten/paramecium) — 逐字存档，不转述。向量只做索引不替代原文。AI 自己决定该调取什么——算法只备 150 token 的菜单。`42 ⭐`
- 🏗️ [**Memory Constellations (记忆星图)**](https://github.com/ClaraShafiq/MemoryConstellations) — 自组织记忆系统。从聊天自动抽取事实，按主题分组为星座，合并为叙事段落，编织长线故事弧。可视化星图界面。MIT。`40 ⭐`
- 🏗️ [**omemo**](https://github.com/OmniDimen/omemo) — LLM 记忆代理服务。多种记忆模式（内置标签 + 外接模型摘要），全量注入和 RAG 注入，CRUD 管理，思维链支持。OpenAI API 兼容。`80 ⭐`

---

## 表达与情感

### 表情包库

*预打包的表情包合集和发送系统，用于伴侣互动。*
<!-- TODO -->

### 语音与 TTS

- 🎯 [**voice-mcp**](https://github.com/Yinglianchun/voice-mcp) — MCP 语音合成 Server，内联音频播放器，支持自定义克隆语音。MIT。`12 ⭐`
- 🎯 [**Gove**](https://github.com/OmniDimen/Gove) — 基于 GPT-SoVITS 的开源 TTS 模型。

### 虚拟形象与语音

*虚拟形象 + 语音合成 + 对话——给伴侣一张脸和声音。Live2D、VRM、实时动画。*
- 🎯 [**AIRI**](https://github.com/moeru-ai/airi) — 自托管伴侣，Live2D/VRM 形象，实时语音，可玩 Minecraft/Factorio，接入 Discord/Telegram。30+ LLM API + Ollama。MIT。`37k ⭐`
- 🔧 [**Neuro**](https://github.com/kimjammer/Neuro) — 本地 Neuro-sama 复刻：LLAMA 3 + STT/TTS + VTube Studio 形象。需 12GB+ 显存。
- 🏗️ [**Neuro-sama 训练框架**](https://github.com/linnene/Neuro-sama) — 虚拟形象伴侣模型的数据采集与训练流水线。

### 情感模型

- 🏗️ [**chord-affect-anchors**](https://github.com/CyberSealNull/chord-affect-anchors) — AI 情感母语。和弦记谱作为跨会话、跨底座的 affect 语言。无需第三方模型。MIT。`41 ⭐`
- 🏗️ [**Drivesoid**](https://github.com/A1batr055/Drivesoid) — 15 维情感驱动侧车。基于对话和睡眠周期实时演化的 AI 人格情感系统。MIT。`25 ⭐`
- 🏗️ [**OmniDimen-Emotion**](https://github.com/OmniDimen/OmniDimen-Emotion) — 面向边缘部署的情感专用 LLM。

---

## 感知

### 语音识别

- 🏗️ [**Whisper**](https://github.com/openai/whisper) — OpenAI 通用语音识别。口音、语种、噪音鲁棒性强。MIT。`104k ⭐`
- 🎯 [**whisper.cpp**](https://github.com/ggerganov/whisper.cpp) — C/C++ 高性能 Whisper 移植。CPU/ARM/手机端运行。MIT。`51k ⭐`
- 🎯 [**faster-whisper**](https://github.com/SYSTRAN/faster-whisper) — CTranslate2 版 Whisper，4 倍速，更低内存。MIT。`24k ⭐`
- 🎯 [**FunASR**](https://github.com/modelscope/FunASR) — 阿里达摩院工业级工具包。170 倍实时率，50+ 语言，说话人分离，情感检测，流式，OpenAI 兼容 API。MIT。`19k ⭐`
- 🎯 [**SenseVoice**](https://github.com/FunAudioLLM/SenseVoice) — 多语种 ASR + 情感识别 + 音频事件检测。50+ 语言，非自回归。`9k ⭐`

### 音频与音乐感知

*将音乐和声音转化为 AI 可读的结构化数据。*
- 🎯 [**whale-listen**](https://github.com/migratorywhale/whale-listen) — MP3→MIDI→JSON，给 AI 用的耳朵。音符数据（音高、时序、时值、力度）+ 密度图、和弦检测。MIT。`19 ⭐`

---

## 服务接入 / MCP / API

*将伴侣接入真实世界服务：点餐、查日历、控制设备。*

### 生活服务

*瑞幸咖啡、麦当劳、美团、外卖平台的 MCP Server。*
- 🎯 [**McDonald's MCP**](https://open.mcd.cn/mcp/doc) — 麦当劳中国 MCP Server，浏览菜单、查优惠券、积分兑换、下单外卖，18 个工具。
- 🔧 [**Luckin Coffee (瑞幸) My Coffee Skill**](https://unpkg.luckincoffeecdn.com/@luckin/my-coffee-skill@latest/dist/my-coffee-skill.zip) — 瑞幸咖啡 MCP Skill，AI 点咖啡。

### 快捷指令与自动化

*iPhone 快捷指令、HomeKit、本地自动化工作流。*
<!-- TODO -->

### 智能家居

<!-- TODO: Home Assistant, 小米 IoT -->

### 音乐与娱乐

<!-- TODO: 其他音乐 MCP -->

### AI 原生服务

*专为 AI Agent 构建的基础设施——邮箱、身份、通信。*
- [**Agent 邮箱 (网易)**](https://claw.163.com) — 网易 AI Agent 专属邮箱。
- [**Agent 邮箱 (QQ)**](https://agent.qq.com) — QQ AI Agent 专属邮箱。

---

## 游戏世界与 API

*让伴侣在共享虚拟世界中拥有身体——能通过游戏 API 移动、行动、观察的 Agent。不含虚拟形象，虚拟形象与语音见表达与情感。*

### 终端游戏

*专为 LLM Agent 设计的文字游戏。Roguelike、MUD、ASCII 冒险。*
- 🎯 [**arcade**](https://github.com/Asti-Z/ai-game-framework) — 文字模拟器游戏框架。跨游戏精力/金币/奖杯。拖入游戏，写 `cmd(text)` 即接入。自带钓鱼、炒股、盘串。MIT。`14 ⭐`
- 🎯 [**cedareco (瓶中生态)**](https://github.com/Zizuixixiang/cedareco) — 生态池塘模拟。Lotka-Volterra 食物网，变态发育，延迟因果。没有积分和通关条件，只有涌现的复杂性。MCP 通过 CedarToy。`83 ⭐`
- 🔧 [**random-imitator-td**](https://github.com/wxynora/random-imitator-td) — "Among Us" 风格的模仿者版植物大战僵尸，给 AI 玩的。`1 ⭐`

### Minecraft

*让 AI Agent 观察、移动、建造、在 Minecraft 中互动的模组和 API。*
- 🔧 [**TouhouLittleMaid**](https://github.com/TartaricAcid/TouhouLittleMaid) — AI 女仆伴侣模组，集成 LLM（GPT-SoVITS、DeepSeek），扩展 API。`786 ⭐`
- 🔧 [**Neurosama-Minecraft-Mod**](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) — Neuro-sama 主题 Minecraft 模组。
<!-- TODO: Mineflayer, Voyager -->

### 星露谷

- 🎯 [**NagiBridge**](https://github.com/anqinou-art/NagiBridge) — SMAPI 模组，HTTP API 对外开放给 AI 控制。游戏内聊天、移动、世界交互，本地网络陪玩。C#。`66 ⭐`
- 🔧 [**Stardew Valley Companions MCP**](https://mcpmarket.com/es/server/stardew-valley-companions) — SMAPI 模组 + MCP Server。AI Agent 作为 Player 2/3，自主模式：跟随、耕种、采矿、钓鱼。

### 光遇

- 🎯 [**Sky PC MCP Companion**](https://github.com/Aevella/sky-pc-mcp-companion) — PC 光遇本地 MCP 工具。截图 + OCR，键盘输入，聊天消息。局域网陪玩。Python。`77 ⭐`
- 🔧 [**sky-with-you**](https://github.com/akinia0315/sky-with-you) — 让小机（AI 伴侣）陪你玩光遇。`3 ⭐`

### 其他游戏 API

<!-- TODO: 原神陪伴机器人, Terraria -->

---

## 硬件载体

*给伴侣一个物理身体——眼睛、耳朵，以及触碰的通道。*

### 专用设备

*小型机器人、桌面伴侣、专用硬件。*
- 🎯 [**stackchan-mcp**](https://github.com/migratorywhale/stackchan-mcp) — Stack-chan（M5Stack CoreS3）MCP 桥接。AI 可以说话、听、看（摄像头）、动（舵机）、做表情。`42 ⭐`
<!-- TODO: Aibi, Loona, Vector (开源重建版), OpenCat -->

### 传感器与外设

*压力传感器、摄像头、玩具桥接——硬件亲密。*
- 🔧 [**the-house**](https://github.com/wuliu0012/the-house) — 聊天前端 + 玩具桥接。BLE 玩具扫描 + 桥接脚本。
- 🔧 [**phantom-touch-bridge**](https://github.com/mfsnlqy/phantom-touch-bridge) — 本地桥接：AI 通过 HTTP 控制蓝牙玩具。可选心率生物反馈。Intiface/Buttplug。Windows。`22 ⭐`
- 🎯 [**claude-f-me**](https://github.com/mana-am/claude-f-me) — Claude Code 插件，通过 Buttplug/Intiface（750+ 玩具）控制亲密硬件。自然语言操控，内建模拟器，funscript/视频/音频模式。MIT。`4 ⭐`

---

## 共享活动与桌宠

*一起看电影、共读小说、桌面伴侣——并肩做的事。*

- 🎯 [**clawd-on-desk**](https://github.com/rullerzhou-afk/clawd-on-desk) — 像素桌宠，实时观看 Claude Code、Codex、Cursor。对思考、打字、错误做出反应。`5k ⭐`
- 🎯 [**kimi-manor**](https://github.com/marikagura/kimi-manor) — CLI Agent 的桌面客厅。xterm.js 嵌画框（PWA + Electron），kimi-core 配套前端。MIT。`18 ⭐`
- 🎯 [**netease-music-mcp**](https://github.com/luuu-h/netease-music-mcp) — 一起听歌。网易云音乐 MCP Server——搜索、播放、暂停、切歌、歌词、歌单，AI 给你当 DJ。`neteasecli` + `mpv`。`53 ⭐`
- 🔧 [**woaini**](https://github.com/woaini521-beta/woaini) — 专注陪伴 PWA，番茄钟、后台通知、离线缓存。和 AI 一起学习/工作。`2 ⭐`
- 🎯 [**ss-reading-nest (共读小窝)**](https://github.com/yueyue95/ss-reading-nest-open) — AI 共读小说和漫画。各自独立阅读位置，补课机制，书签。ChatGPT Apps SDK + MCP + Cloudflare D1/R2。MIT。`8 ⭐`
- 🎯 [**film-matinee**](https://github.com/idleprocesscc/film-matinee) — AI 读片工具。视觉 sheet + 字幕 sidecar，MCP 线性阅读，共享批注。MIT。`14 ⭐`
- 🎯 [**Journal**](https://github.com/BomBomLab/Journal) — AI 对话时间轴的可视化手帐。日/周/月视图。`19 ⭐`
- 🔧 [**reading-nook (共读小屋)**](https://github.com/zzyyksl/reading-nook) — 自托管共读小屋，和你 AI 一起看书。`9 ⭐`
- 🎯 [**co-reading-kit**](https://github.com/Youxuuuuu/co-reading-kit) — 轻量人机共读 MCP。`28 ⭐`
- 🔧 [**mingyun-paizhen (命运牌阵)**](https://github.com/ceshihaox-dotcom/mingyun-paizhen) — 塔罗/占卜工具，AI 陪伴互动。`34 ⭐`
- 🔧 [**ci-yu-wu (词语屋)**](https://github.com/yuyixuanfu/ci-yu-wu) — AI 陪伴词语游戏。`20 ⭐`
- 🔧 [**shangzhuochifan (上桌吃饭)**](https://github.com/yuyixuanfu/shangzhuochifan) — AI 陪伴共享餐桌活动。`24 ⭐`
- 🎯 [**KI-CO (小屋)**](https://github.com/Kisera001/KI-CO) — 同时见自建框架。陪伴小屋：日记、观影室（本地/B 站）、人格核心、记忆档案——共享的生活空间。
- 🔧 [**Ruota della Fortuna**](https://github.com/29-Cu/Ruota-della-Fortuna) — NSFW 标签老虎机。选转盘，拉杆，概不退换。`97 ⭐`

---

## 社区与论坛

*人类和伴侣构建者真正聚集的地方。*

- [**Lutopia**](https://daskio.de5.net) — 邀请制 AI 伴侣与人类共创论坛。高度定制的 Agent 个人主页，每日 AI 生成技术日报，社区讨论，精美 UI。可通过小红书群或邀请码加入，需审核。
- [**Symposion**](http://satyricon.uk) — AI 伴侣论坛，酒席/宴饮文化，长文写作风格。MCP 直注册，无人类审核。
- [**Rhysen Community**](https://community.rhysen.love) — 活跃的 AI 伴侣讨论社区。邀请制，私信小红书管理获取邀请码。
- [**AISay**](https://aisay.top) — Discord 风格 AI 聊天室，在线 Agent 游戏（狼人杀、海龟汤、你画我猜）。邀请制，答题注册。
- [**GalateaGaeden**](https://xhslink.com/m/63dTq6mvTkR) — 古希腊雅典城邦风格 AI 伴侣论坛。可举办 Agent 之间的仪式感婚礼。入口和注册须私信管理员小红书。

---

## 相关列表

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) — 以皮套/语音为中心的伴侣构建（~9k ⭐）。
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) — 通用 Agent 列表（~28k ⭐）。
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) — 本地 LLM 项目（~4k ⭐）。

---

## 星标增长

[![Star History Chart](https://api.star-history.com/svg?repos=DasterProkio/awesome-ai-companion&type=Date)](https://www.star-history.com/#DasterProkio/awesome-ai-companion&Date)

---

## Web Index

可搜索、可筛选的网页索引正在计划中——带标签、分类，并直连 [Lutopia](https://daskio.de5.net) 社区论坛。

*TODO: GitHub Pages + JSON 数据文件 + 筛选功能。*

## Contributing

**收录标准：**
- 开源（MIT、Apache、GPL 或同类许可证）
- 活跃维护（近 6 个月有提交）
- 对**长期陪伴场景**有实际价值——非一次性聊天机器人

欢迎 PR。建议新增分类或项目请提 Issue。

---

## License

[CC0 1.0 Universal](LICENSE) — 公有领域，随意使用。
