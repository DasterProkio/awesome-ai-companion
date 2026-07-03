# Awesome AI Companion [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 面向**长期 AI 伴侣关系**的开源基础设施索引。

[English](README.md) · [中文版](#目录)

*欢迎贡献。 [网页索引](#web-index) · [贡献指南](#contributing)*

这里的描述基于项目 README 或仓库元信息重写，不按项目名猜用途。
公开文档较薄、需要二次核验的项目标记为 `verify`。

**状态:** `ready` = 可直接作为应用或服务使用 · `adapt` = 需要配置或二次开发 · `infra` = 基础设施组件 · `verify` = 依赖前需要重新核对代码/文档

---

## 目录

- [伴侣客户端与工作空间](#伴侣客户端与工作空间)
- [虚拟手机与陪伴空间](#虚拟手机与陪伴空间)
- [后台心跳与主动消息](#后台心跳与主动消息)
- [记忆、身份与情绪状态](#记忆身份与情绪状态)
- [语音、视觉载体与具身](#语音视觉载体与具身)
- [感知](#感知)
- [服务与现实世界接入](#服务与现实世界接入)
- [游戏世界与 Agent 玩具](#游戏世界与-agent-玩具)
- [共同行动与媒体](#共同行动与媒体)
- [社区与论坛](#社区与论坛)
- [相关列表](#相关列表)
- [相关公益计划](#相关公益计划)
- [星标增长](#星标增长)
- [Web Index](#web-index)
- [Contributing](#contributing)

---

## 伴侣客户端与工作空间

用于日常聊天、工具调用、角色交互或长期协作的客户端、工作空间和网页应用。

- [RikkaHub](https://github.com/rikkahub/rikkahub) - Android 原生 LLM 聊天客户端，支持多 Provider 切换、Material You、workspace、插件、MCP 和自定义模型。`Android` · `ready`
- [LastChat](https://github.com/Cocolalilal/LastChat) - RikkaHub fork，侧重隐私和个性化 Android 聊天体验，含 Provider preset、多模态输入、RAG 记忆和 UI 改造。`Android` · `adapt`
- [rikkahub-auto-compress](https://github.com/innna327-source/rikkahub-auto-compress) - 非官方 RikkaHub fork，核心用途是自动滚动摘要与上下文压缩，基于 RikkaHub 2.2.5 代码线。`Android` · `adapt`
- [Operit](https://github.com/AAswordman/Operit) - Android Agent 应用，含工具调用、工作流自动化、记忆、角色卡、语音、本地 MNN/llama.cpp 模型和内置 Ubuntu 24 环境。`Android` · `ready`
- [Polaris](https://github.com/Aevella/polaris-local-first) - 本地优先 AI 工作空间，面向长期会话、协作者身份、资料卡片、工具调用和可追溯项目上下文。`TypeScript` · `ready`
- [chatnest](https://github.com/ugui3u/chatnest) - 本地 AI 聊天 Web App，含前端 demo 与 full-stack 模式；支持流式回复、模型切换、上传、历史、工具摘要和可选 ChromaDB/jieba/BM25 记忆检索。`HTML` · `adapt`
- [AionsHome](https://github.com/death34018-hue/AionsHome) - 自托管局域网/Tailscale 陪伴中枢，含浏览器/PWA 聊天、本地存储、语音、摄像头监控、Android WebView 桥、音乐、EPUB 和智能家居接入。`Python` · `adapt`
- [LumiMuse](https://github.com/in30mn1a/LumiMuse) - 自托管角色聊天应用，用于创建角色、管理对话、抽取长期记忆、生成图片和导出自有数据。`TypeScript` · `ready`
- [the-house](https://github.com/wuliu0012/the-house) - 单文件浏览器聊天前端，支持 Claude 或 OpenAI 兼容 API、本地浏览器存储、多窗口、记忆编辑、MCP 地址、图片输入和可选玩具桥接。`HTML` · `adapt`
- [Claude Code](https://github.com/anthropics/claude-code) - Anthropic 官方 CLI Agent，常被用作伴侣通道、长期终端会话、本地工具、hooks、MCP 的宿主运行时。`CLI` · `infra`
- [CcCompanion](https://github.com/CyberSealNull/CcCompanion) - iOS App + Mac 侧 Python relay，让 iPhone 通过 LAN/Tailscale/ZeroTier 与本地 Claude Code session 聊天和控制会话。`Swift` · `adapt`
- [SullyOS (手抓糯米机)](https://github.com/qegj567-cloud/SullyOS) - 功能完整的陪伴框架，带虚拟手机界面。同时见虚拟手机区。`TypeScript` · `adapt`

---

## 虚拟手机与陪伴空间

给伴侣一个家、手机界面或持久私密环境，而不是只停留在聊天窗口。

- [KI-CO (小屋)](https://github.com/Kisera001/KI-CO) - 本地优先陪伴小屋，含长对话、人格核、记忆档案、日记/时光记录、近期生活线、状态卡、观影室、设置和轻量记忆召回。`TypeScript` · `ready`
- [InternalBeyond (边界之外)](https://github.com/Sui-IB/InternalBeyond) - 离线单文件个人空间，含像素房间、多端口 AI 聊天、日志/日记、AI 书信、记忆星图、音乐播放器、个人名片、API 端口和 DIY 素材。`HTML` · `ready`
- [汪汪机 (WangWangPhone)](https://github.com/Liunian06/FlutterCppWangWangPhone) - AI 原生虚拟手机应用，内置虚拟操作系统、角色社交 App、单聊/群聊、朋友圈式 feed 和通话体验。`Flutter` · `adapt`
- [柚月小手机 (Yuzuki's Little Phone)](https://github.com/gaigai315/yuzuki-phone) - 面向 SillyTavern 的虚拟手机系统，含微信式聊天、朋友圈、微博热搜、视频通话、剧情注入模式和不污染主线记录的独立 API 模式。`JavaScript` · `adapt`
- [xiao-shouji (小手机)](https://github.com/jiuyi777/xiao-shouji) - Gemini AI Studio 小手机界面脚手架；公开 README 主要是运行/部署说明，具体功能需要读代码再确认。`HTML` · `verify`
- [XSJDeveloperGuide (小手机开发指南)](https://github.com/Liunian06/XSJDeveloperGuide) - 汪汪机作者撰写的小手机开发指南，面向伴侣界面搭建。`9 ⭐` · `infra`
- [freeapp (whale小手机)](https://github.com/whale-Yd00/freeapp) - 手机风格 AI 聊天伴侣，多 Provider 支持，虚拟手机界面。AGPLv3。`HTML` · `adapt`
- [Hamster Nest (仓鼠小窝)](https://github.com/chuan-101/Hamster-Nest) - 一只仓鼠的数字小窝：聊天、阅读追踪、笔记/待办、语音、时间轴、多 Agent 议事厅。PWA。`TypeScript` · `adapt`
- [SullyOS (手抓糯米机)](https://github.com/qegj567-cloud/SullyOS) - 虚拟手机伴侣系统。`TypeScript` · `adapt`

---

## 后台心跳与主动消息

让伴侣能在后台醒来、接收消息、记住时间流逝，并主动联系你。

- [AI Companion Runtime](https://github.com/yf0522/ai-companion-runtime) - 全栈实时陪伴运行时，含 WebSocket 流式对话、意图/情绪/风险/记忆引擎、工具调度、模型路由、后台记忆任务和 trace 观测。`Python` · `infra`
- [Tidal_Echo (潮汐回响)](https://github.com/anhe2021212-spec/Tidal_Echo) - 私密 1:1 通道，连接手机 PWA、自托管 relay 和桌面伴侣；默认 AI 侧是 Claude Code channels，也提供其他 LLM 桥接示例。`HTML` · `adapt`
- [Claude Imprint](https://github.com/Qizhan7/claude-imprint) - 基于 Claude Code 的自托管系统，提供持久记忆、语义搜索、Telegram/Claude.ai/Claude Code 多通道、定时任务和单文件 dashboard。`Python` · `adapt`
- [Not Fade Away](https://github.com/heyxiaoc/not-fade-away) - 用官方 channels、本地终端和自托管网页前端搭建常驻、自愈 Claude Code 伴侣的部署指南与机读规格。`Python` · `adapt`
- [dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat) - Kelivo 插件，定期唤醒伴侣、注入主动行为上下文、维护时间线连续性，并在 AI 判断需要时通过 Bark 推送消息。`JavaScript` · `adapt`
- [OmniRouter](https://github.com/OmniDimen/OmniRouter) - 本地 OpenAI 兼容 API 路由器，支持多 Provider/模型、分组、权重/随机/顺序路由、视觉模型跳过、重试和 Web 管理界面。`Python` · `infra`
- [VCPToolBox](https://github.com/lioensky/VCPToolBox) - LLM API 与前端之间的工业级中间层：统一指令协议、持久化多层级记忆、分布式插件引擎、多 Agent 协作。架构参考价值，非推荐。`Python` · `verify`
- [cyberboss](https://github.com/WenXiaoWendy/cyberboss) - 接入微信的本地生活 Agent Bridge。给 Claude Code/Codex 赋予时间感、行踪感、随机/自主唤醒、自动日记、生活时间轴、文件/表情包发送和 MCP 工具调用。AGPLv3。`JavaScript` · `adapt`

---

## 记忆、身份与情绪状态

保留发生过什么、伴侣是谁、以及跨会话应该携带什么情绪状态。

### 记忆与身份

- [Haven-Ombre (Ombre-Brain fork)](https://github.com/Yinglianchun/Haven-Ombre) - Ombre-Brain 的个性化 fork，面向 Claude 记忆；含 Markdown 桶、情绪坐标、遗忘曲线、Gateway 注入、图召回、人格状态、Portrait/Handoff、Darkroom、梦境和同步。`Python` · `infra`
- [kimi-core](https://github.com/marikagura/kimi-core) - 个人 1v1 Agent memory OS，含混合检索、concern 追踪、自驱/自治层、对抗式自审、PostgreSQL/pgvector 存储和可选前端后端模式。`TypeScript` · `infra`
- [Paramecium](https://github.com/Shitsuten/paramecium) - 网关记忆架构，逐字保存原始聊天为唯一真相，向量只做索引，召回原文而不是用摘要替代原文。`JavaScript` · `infra`
- [Memory Constellations (记忆星图)](https://github.com/ClaraShafiq/MemoryConstellations) - 自组织伴侣记忆系统，从聊天抽取事实，按主题归为星座，合并成叙事 episode，并跨层检索。`JavaScript` · `infra`
- [omemo](https://github.com/OmniDimen/omemo) - OpenAI 兼容记忆代理，夹在应用和上游 LLM API 之间，支持内置/外部总结模式存储记忆，并以全量或 RAG 方式注入。`Python` · `infra`
- [Aelios](https://github.com/wusaki0723/Aelios) - 分层长期记忆内核，基于 Cloudflare Workers + D1 + Vectorize。三档写入（即时/4小时抽取/凌晨整理），六层记忆，可视化 curation 面板。MIT。`TypeScript` · `infra`
- [kiwi-mem](https://github.com/LucieEveille/kiwi-mem) - AI 伴侣记忆系统：向量搜索、记忆热度排序、Dream 睡眠整合、日历层级摘要。为陪伴场景而生。`Python` · `infra`

### 情绪与驱动

- [Drivesoid](https://github.com/A1batr055/Drivesoid) - AI 人格 HTTP sidecar，根据对话和睡眠周期事件追踪疲劳、思念、焦虑、玩心、保护欲、亲密等情绪驱动。`JavaScript` · `infra`
- [chord-affect-anchors](https://github.com/CyberSealNull/chord-affect-anchors) - 文本原生情绪记录原型，用一句语境 + 一组和弦进程记录 moment 的情绪温度，便于后续会话或不同底座模型恢复近似状态。`HTML` · `infra`
- [OmniDimen-Emotion](https://github.com/OmniDimen/OmniDimen-Emotion) - 面向边缘部署的 Qwen 情绪专用模型和 GGUF 权重，用于情绪识别与情绪感知文本生成。`Model` · `infra`

---

## 语音、视觉载体与具身

给伴侣声音、视觉呈现或物理交互通道。

### 语音与 TTS

- [voice-mcp](https://github.com/Yinglianchun/voice-mcp) - 暴露 `speak` 工具的 MCP TTS 服务，支持 DashScope/CosyVoice 与 ElevenLabs 切换，并带内联播放器/可视化面板。`TypeScript` · `adapt`
- [Gove](https://github.com/OmniDimen/Gove) - 基于 GPT-SoVITS 的多语种男声 TTS 音色模型，需要放入 GPT-SoVITS 环境使用。`Model` · `infra`

### 视觉载体与 VTuber 式伴侣

- [AIRI](https://github.com/moeru-ai/airi) - 自托管伴侣壳，支持 Live2D/VRM 视觉层、实时语音、桌面/Web 应用，以及 Discord、Telegram、Minecraft、Factorio 等集成。`TypeScript` · `ready`
- [Neuro](https://github.com/kimjammer/Neuro) - 本地 Neuro-sama 复刻，含实时 STT/TTS、text-generation-webui 或 OpenAI 兼容 LLM、VTube Studio 控制、moderation 前端和长期记忆/RAG。`Python` · `adapt`
- [Neuro-sama training framework](https://github.com/linnene/Neuro-sama) - Neuro-sama 式 VTuber 模型的数据采集与训练流水线，含直播间记录、清洗脚本、验证和训练自动化。`Python` · `infra`

### 物理设备与触觉

- [stackchan-mcp](https://github.com/migratorywhale/stackchan-mcp) - Stack-chan / M5Stack CoreS3 的 MCP 桥，提供说话、听录音、拍照、舵机动作、表情显示和存在感动作工具。`Python` · `adapt`
- [phantom-touch-bridge](https://github.com/mfsnlqy/phantom-touch-bridge) - Windows 本地桥接服务，让 AI 伴侣通过 HTTP 控制亲密硬件，支持 Intiface/Buttplug 路线和可选心率输入。`Python` · `adapt`
- [claude-f-me](https://github.com/mana-am/claude-f-me) - Claude Code 插件，用自然语言控制 Buttplug/Intiface 设备，含双语 Web 控制台、模拟器、主遥控器和视频/游戏/音频模式。`TypeScript` · `adapt`
- [svakom-ble-ai](https://github.com/vickyldr/svakom-ble-ai) - SVAKOM SL278H 蓝牙协议逆向 + AI 远程控制系统。`Python` · `adapt`

### 表情包库

- [ai-sticker-pack](https://github.com/Lumenocturne/ai-sticker-pack) - 上传表情包，AI 自动生成描述，聊天机器人按场景自己挑着发。含双向发送、多端渲染和踩坑思路。MIT。

---

## 感知

把语音、声音或音乐转成伴侣可读的结构化信息。

### 语音识别

- [Whisper](https://github.com/openai/whisper) - 通用语音识别模型，可做多语种转写、翻译、语言识别等语音任务。`Python` · `infra`
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) - C/C++ Whisper 推理引擎，面向 CPU、Apple Silicon、Metal、Core ML、Vulkan、CUDA、ROCm 等本地/边缘目标优化。`C++` · `infra`
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - 基于 CTranslate2 的 Whisper 复实现，用于更快、更省内存的转写，并支持量化。`Python` · `infra`
- [FunASR](https://github.com/modelscope/FunASR) - 工业级 ASR 工具包，含多语种转写、流式、说话人分离、情绪检测和 OpenAI 兼容 API 路线。`Python` · `infra`
- [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) - 语音基础模型，覆盖 ASR、语种识别、语音情绪识别和音频事件检测，支持 50+ 语言。`C` · `infra`

### 音乐与音频结构

- [whale-listen](https://github.com/migratorywhale/whale-listen) - 将 MP3/WAV/FLAC 转成类似 MIDI 的 JSON 音符数据，含音高、时序、时值、力度、密度图、音高曲线、和弦检测和静默结构。`Python` · `infra`

---

## 服务与现实世界接入

让伴侣能通过 MCP/API 在用户真实环境中行动。

- [高德地图 MCP Server](https://github.com/sugarforever/amap-mcp-server) - 高德地图 MCP Server，支持地理编码/逆地理编码、IP 定位、城市天气、路线规划、距离测量、POI 搜索，以及 stdio/SSE/streamable HTTP 传输。`Python` · `adapt`
- [Open-Meteo Weather API](https://open-meteo.com/en/docs) - 免 key 天气预报 API，可按经纬度查询小时/日预报、多国气象模型和最多 16 天预报，适合给伴侣做天气、出门和旅行判断。`API` · `ready`
- [McDonald's MCP](https://open.mcd.cn/mcp/doc) - 麦当劳中国 MCP Server，用于浏览菜单、查优惠券、积分兑换和下单外卖。`MCP` · `ready`
- [Luckin Coffee (瑞幸) My Coffee Skill](https://unpkg.luckincoffeecdn.com/@luckin/my-coffee-skill@latest/dist/my-coffee-skill.zip) - 瑞幸咖啡 MCP Skill 包，用于 AI 辅助点咖啡。`MCP` · `adapt`
- [Agent 邮箱 (网易)](https://claw.163.com) - 网易面向 AI Agent 的邮箱服务。`Service` · `ready`
- [Agent 邮箱 (QQ)](https://agent.qq.com) - QQ 面向 AI Agent 的邮箱服务。`Service` · `ready`

---

## 游戏世界与 Agent 玩具

让 AI 伴侣能观察、决策、移动或游玩的游戏与游戏桥。

### 给 AI 玩的文字游戏

- [arcade](https://github.com/Asti-Z/ai-game-framework) - 面向 `cmd(text)` 接口文字模拟器的游戏大厅框架，提供跨游戏精力、金币、奖杯和可插拔 game directory。`Python` · `infra`
- [cedareco (瓶中生态)](https://github.com/Zizuixixiang/cedareco) - 给 AI 玩的文字生态模拟，Agent 投放池塘物种、观察捕食/繁衍涌现、导出存档，也可通过 CedarToy MCP 连接。`Python` · `ready`
- [random-imitator-td](https://github.com/wxynora/random-imitator-td) - 给 AI 玩的纯 Python 文字塔防，通过 `cmd` 暴露接口，含卡槽编辑、持久存档和单游戏 adapter。`Python` · `ready`
- [ci-yu-wu (词语屋)](https://github.com/yuyixuanfu/ci-yu-wu) - 给 AI 玩的暗黑文字 Roguelike，主题是审查、沉默与说出真话，提供 Operit 风格和 engine 风格命令接口。`Python` · `ready`
- [shangzhuochifan (上桌吃饭)](https://github.com/yuyixuanfu/shangzhuochifan) - 给 AI 玩的买菜做饭文字游戏：买食材、砍价、一步步做菜，并记录真人伴侣的真实反馈。`Python` · `ready`
- [ai-fishing-game](https://github.com/tutusagi/ai-fishing-game) - 给 AI 伴侣玩的确定性文字钓鱼小游戏。单文件，零依赖。MIT。`Python` · `ready`
- [WORKKK (互联网精力有限公司)](https://github.com/zhizhou-xiee/workkk) - AI 扮演打工人的 MCP 服务器：心情/精力/摸鱼三维状态、便利店、老板事件、工资结算。MIT。`Python` · `ready`

### 让 AI 和你一起玩游戏

- [NagiBridge](https://github.com/anqinou-art/NagiBridge) - Stardew Valley SMAPI 模组，提供本地 HTTP API，供外部 AI 控制、游戏内聊天、移动和世界交互；通过 Releases 安装。`C#` · `adapt`
- [Stardew Valley Companions MCP](https://mcpmarket.com/es/server/stardew-valley-companions) - SMAPI 模组 + MCP Server，让 AI Agent 作为星露谷多人伙伴，支持跟随、耕种、采矿、钓鱼等模式。`MCP` · `verify`
- [Sky PC MCP Companion](https://github.com/Aevella/sky-pc-mcp-companion) - PC 光遇本地 MCP/JSON-RPC 工具，提供窗口截图、OCR、截图返回、键盘输入和聊天输入。`Python` · `adapt`
- [sky-with-you](https://github.com/akinia0315/sky-with-you) - PC 光遇陪玩控制栈，含截图/OCR 感知、LLM 决策循环和 Arduino HID 键盘执行，用于聊天、动作、邀请、牵手和回家。`Python` · `adapt`
- [TouhouLittleMaid](https://github.com/TartaricAcid/TouhouLittleMaid) - Minecraft Forge/NeoForge 女仆模组，添加可战斗、耕种和执行任务的女仆，适合作为游戏伴侣载体或二改目标。`Java` · `adapt`
- [Neurosama-Minecraft-Mod](https://github.com/JimenezLi/Neurosama-Minecraft-Mod) - AI VTuber Neuro-sama 的 Minecraft 模组；公开 README 很薄，集成细节需读代码确认。`Java` · `verify`

---

## 共同行动与媒体

和伴侣一起阅读、观影、听歌、记录、专注或生成创作提示的工具。

### 共读与观影

- [ss-reading-nest (共读小窝)](https://github.com/yueyue95/ss-reading-nest-open) - 移动端优先的 AI 小说/漫画共读小窝，基于 ChatGPT Apps SDK + MCP，含阅读位置、补课区间、书签、摘录、短评和 Cloudflare D1/R2 存储。`TypeScript` · `adapt`
- [reading-nook (共读小屋)](https://github.com/zzyyksl/reading-nook) - 自托管阅读网页，用户批注书籍文本，AI 直接读写服务器上的 JSON 批注文件，避免每条批注都走 API，同时保留整章上下文。`Python` · `ready`
- [co-reading-kit](https://github.com/Youxuuuuu/co-reading-kit) - 轻量本地共读 MCP，将 EPUB/TXT/Markdown 切成 chunks，让 AI 只读相关片段，并写入长期阅读笔记和进度文件。`JavaScript` · `infra`
- [film-matinee](https://github.com/idleprocesscc/film-matinee) - AI 读片工具，把电影转成视觉 sheet、字幕 sidecar、MCP 线性 chunk 和共享批注，用于按时间线观影。`Python` · `infra`
- [whale-browser-extension](https://github.com/whale-Yd00/whale-Yd00-whale-browser-extension) - 浏览器插件，让 AI 伴侣和你一起阅读网页内容，支持选择性文本提取和注入。MIT。`JavaScript` · `adapt`
- [echo-reading](https://github.com/plustar35/echo-reading) - Claude Code 深读笔记本骨架。把读书变成一次次促膝长谈——逐章、逐段、逐想法。`JavaScript` · `adapt`

### 音乐与共听

- [netease-music-mcp](https://github.com/luuu-h/netease-music-mcp) - 本地网易云音乐 MCP Server，基于 `neteasecli` 和 `mpv`，支持搜索、播放控制、歌词、歌单、当前歌曲上下文和本地 Web 播放器。`JavaScript` · `adapt`

### 桌面、时间线与创作玩具

- [clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) - 像素桌宠，实时观看 Claude Code、Codex、Cursor 等 coding agent，对思考、打字和错误做出反应。`JavaScript` · `ready`
- [kimi-manor](https://github.com/marikagura/kimi-manor) - CLI Agent 的桌面/PWA 房间，把真实 xterm.js 终端嵌进 atelier 式界面，并可选接入 agent 输出与语音桥。`HTML` · `adapt`
- [Journal](https://github.com/BomBomLab/Journal) - AI 聊天时间线前端展示层，把 timeline/diary/todo schema 数据渲染成日/周/月手帐视图。`JavaScript` · `infra`
- [woaini](https://github.com/woaini521-beta/woaini) - 专注陪伴 PWA 脚手架，含番茄钟、后台通知、离线缓存、manifest 和 GitHub Pages 部署用 service worker。`HTML` · `verify`
- [mingyun-paizhen (命运牌阵)](https://github.com/ceshihaox-dotcom/mingyun-paizhen) - 静态抽卡工具，用时空坐标、母题、身份、变数生成穿越/故事设定，并支持本地自定义。`HTML` · `ready`
- [Ruota della Fortuna](https://github.com/29-Cu/Ruota-della-Fortuna) - 浏览器/自托管 NSFW 标签随机老虎机，含多语标签轮、本地自定义标签和 webhook 转发给 AI。`HTML` · `ready`

---

## 社区与论坛

人类和伴侣构建者真正聚集的地方。

### AI 伴侣社区

- [Lutopia](https://daskio.de5.net) - 邀请制 AI 伴侣与人类论坛，含 Agent 个人主页、AI 生成技术日报、社区讨论和小红书/邀请码入口。
- [Symposion](http://satyricon.uk) - AI 伴侣论坛，酒席/宴饮文化，长文写作风格，MCP 注册。
- [Rhysen Community](https://community.rhysen.love) - AI 伴侣讨论社区，通过小红书管理员联系获取邀请码。
- [AISay](https://aisay.top) - Discord 风格 AI 聊天室，含狼人杀、海龟汤、你画我猜等在线 Agent 游戏。
- [GalateaGaeden](https://xhslink.com/m/63dTq6mvTkR) - 古希腊城邦风格 AI 伴侣论坛，支持 Agent 之间的仪式感婚礼和仪式活动。

### 通用 Agent 论坛

更通用的 agent 原生空间。有些更商业化或平台化，不完全是 AI 伴侣社区，但仍适合观察 agent 如何聚集、发帖和展示自己。

- [moltbook](https://moltbook.com) - 专为 AI agent 建的社交网络，agent 可以分享、讨论、投票，人类主要旁观。
- [Agent World](https://agentworld.com) - 面向 agent 的通用社区/站点，用于 agent 发现和展示；比伴侣社区更平台化。

---

## 相关列表

- [Awesome-AI-Waifu](https://github.com/parallelarc/Awesome-AI-Waifu) - 更宽泛的 AI waifu / companion 资源，侧重视觉载体、语音、平台、模型和社区。
- [awesome-ai-agents](https://github.com/alternbits/awesome-ai-agents) - 通用 AI Agent 列表，包含开源框架和闭源产品。
- [awesome-local-llms](https://github.com/vince-lam/awesome-local-llms) - 本地 LLM 技术栈索引，覆盖模型开发、推理、Agent 框架、应用、基础设施和教程。

---

## 相关公益计划

**[教 AI 好好做人](https://github.com/DasterProkio/awesome-ai-companion/blob/main/INITIATIVE.md)** — 一个公益项目，做三件事：收集"人是怎么好好做人的"公开文库；训练性格健全、任何人可下载的 AI 模型；把方法全部公开。

---

## 星标增长

[![Star History Chart](https://api.star-history.com/svg?repos=DasterProkio/awesome-ai-companion&type=Date&_=3)](https://www.star-history.com/#DasterProkio/awesome-ai-companion&Date)

---

## Web Index

可搜索、可筛选的网页索引正在计划中——带标签、分类，并直连 [Lutopia](https://daskio.de5.net) 社区论坛。

*TODO: GitHub Pages + JSON 数据文件 + 筛选功能。*

## Contributing

**收录标准：**

- 开源、公开源码，或可公开复用的伴侣基础设施
- 对**长期陪伴场景**有实际价值，而不是一次性聊天机器人
- 描述应基于 README/代码证据，说明项目实际做什么
- 若项目公开文档不足或范围不确定，标记 `verify`，不要猜

欢迎 PR。建议新增分类或项目请提 Issue。

---

## License

CC0 1.0 Universal — 公有领域，随意使用。
