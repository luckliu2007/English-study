# 更新日志 / Changelog

本项目的重要变更会记录在这个文件里，格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [Unreleased]

## [2.7.0] - 2026-10-26 · AI 学习模式、权威词表、学习科学、AI 时代词汇

### 新增

- `docs/learning-science.md`：按证据强度整理学习方法（Dunlosky 等 2013 综述中评为高效的练习测试与分散练习、评为低效的总结 / 划线 / 重读；The Learning Scientists 六大策略），并对应到本仓库各方法页
- `docs/ai-english.md` 新增“AI 的学习模式”：ChatGPT 学习模式、Gemini 引导式学习、Claude 学习模式、Google 翻译练习功能（注明目前面向西 / 法 / 葡语使用者），附通用的“学习模式”提示词
- `docs/vocabulary-grammar.md` 重写：Oxford 3000/5000、NGSL 系列（含 NAWL、BSL、TSL、NGSL-Spoken）分级词表，Anki FSRS 与期望记忆率设置
- `docs/exams.md` 新增 Duolingo English Test；`docs/china-friendly.md` 新增国家智慧教育公共服务平台、中国大学 MOOC
- `content/vocabulary.json` 新增 18 个“AI 时代高频词”（agent、hallucination、prompt、token、inference、latency、benchmark、guardrail 等，标签 `AI`），共 322 词
- `content/quizzes.json` 新增 `q-ai-vocab-b2`（AI 时代高频词）、`q-workplace-b1`（职场英语句式），共 14 组

## [2.6.0] - 2026-10-22 · 阅读题答案均衡、托福官方练习、AI 语音陪练

### 新增

- `content/reading.json` 新增 4 篇原创文章：B2《Why Remote Teams Write Everything Down》《Can You Trust an AI Summary?》，C1《The Silent Graveyard: Survivorship Bias》《The Paradox of Automation》
- `docs/exams.md` 托福部分新增 ETS 官方样题（2026 年 1 月版）、TestReady 免费模考说明、官方 Practice Test 1
- `docs/ai-english.md` 新增“实时语音陪练”：开场规则、工具自测对比表、发音被“听漏”和隐私两个局限

### 修复

- 阅读题正确答案原有 59%（47/79）集中在第 2 个选项，学习者靠猜即可得高分；在不改动题干和选项文字的前提下重新排列选项，现为 23 / 23 / 23 / 22
- `scripts/validate_content.py` 新增全局答案分布检查（题目 ≥ 20 且同一位置占比 ≥ 40% 即报错），弥补原先只检查单篇 ≥ 4 题的盲区

## [2.5.0] - 2026-10-22 · 职场英语与考试提示词更新

### 新增

- `docs/workplace-english.md`：邮件、会议、演示、协商四个场景的高频句式、AI 练习方式、学习资源和 4 周练习计划
- `content/prompts.json` 新增 2 条：`p-speaking-meeting-roleplay`（职场会议角色扮演）、`p-writing-email-polish`（商务邮件批改），共 30 条

### 修复

- `p-exam-toefl-writing`：原提示词按已于 2023 年取消的“独立写作”题型和旧评分标准打分，改为按题型的官方评分指南、在 2026 起的 1–6 分制下估分
- `p-exam-band-diagnostic`：增加托福 1–6 分制换算

## [2.4.0] - 2026-10-21 · 全面规划升级

### 新增

- `ROADMAP.md`：仓库定位、本次升级内容和待补强方向（每周一自动检索据此补充资源）
- `docs/exams.md` 新增“2026 年考试变化”：托福 1–6 分制（ETS 官方）、雅思全面机考（IELTS 官方 2026-03-05 公告）、四六级官网入口
- `docs/reading.md` 新增 VOA Learning English、News in Levels、Simple English Wikipedia、Standard Ebooks，以及难度选择方法
- `docs/writing.md` 新增 UNC 写作中心、Google / Microsoft 写作风格指南，以及 AI 批改的使用方法
- `docs/speaking.md` 接入 AI 跟读打分工具（Echo-Loop、EchoType）

### 新增（2026-10-21）

- `docs/github-projects.md` “AI 听说与沉浸式输入”收录 Talljack/echo-type（EchoType，开源听说读写一体练习工具，网页版 + 桌面版），并接入自适应计划

### 新增（2026-10-20）

- `docs/tools.md` 收录 Aictionary（开源英汉桌面词典，本地离线查词、Anki 联动）和青简 Qingjian（拼音输入法，候选词旁显示英语译词）

### 新增（2026-10-19）

- `docs/github-projects.md`、`docs/listening.md` 收录 iChochy/NCE（新概念英语全四册在线点读，单句跟读、中英对照），并接入自适应计划

## [2.3.0] - 2026-10-16 · AI 听说项目、CI 升级与链接维护

### 新增

- `docs/github-projects.md` 新增“AI 听说与沉浸式输入”：Echo-Loop（AI 听说训练 App）、陪读蛙 Read Frog（浏览器沉浸式阅读）、LLPlayer（AI 字幕播放器），均核实 2026-09 后仍在更新，并接入自适应计划能力点
- `docs/tools.md` 字幕与视频学习补充 LLPlayer、Read Frog

### 修复

- `5mdld/anki-english-60k-decks` 已改名为 `anki-english-mwld-decks`，更新链接
- GitHub Docs “About pull requests” 页面已迁移，更新为新地址
- 2026-10-12 定时链接检查失败系 Academic Phrasebank 临时返回 500，复查已恢复

### 变更

- CI：`actions/checkout`、`actions/setup-python` 升级到 v7（运行时 Node 24，旧版 Node 20 action 已被 GitHub 弃用），Python 3.11 → 3.12
- `rspeer/wordfreq` 标注已停更（作者 SUNSET 声明：生成式 AI 内容污染语料，不再更新词频数据）

## [2.2.0] - 2026-08-06 · AI 学英语模块升级

### 新增

- `content/prompts.json`：28 条结构化 AI 提示词，带 [JSON Schema](content/schema/prompts.schema.json) 约束，接入 `validate_content.py`（校验 variables 与 prompt 正文一致、usage 语言）和 `generate_manifest.py`
- `docs/ai-english.md` 扩写：结构化提示词库索引、长期 AI 导师人设配置（ChatGPT Custom GPT / Claude Projects / Gemini Gems）、"如何判断 AI 陪练是否真的有效"自查清单
- README 结构化内容数据表新增 `content/prompts.json` 行

## [2.1.0] - 2026-07-31 · 社区标准与站点上线

### 新增

- 社区健康文件：`CODE_OF_CONDUCT.md`、Issue 模板（资源推荐 / 失效链接报告）、PR 模板，Community Standards 达标率 42% → 85%
- 正式启用 GitHub Pages（此前 `_config.yml` 已就绪但从未在仓库设置里打开），并补上根目录 `index.md` 落地页（原来首页会 404）
- 仓库 description / homepage / topics（此前均为空）
- `templates/error-log.md` 错词错句本模板（原 PR #1 提议，因分支落后 main 13 个提交无法直接合并，改为手动摘取内容合入）
- 本 CHANGELOG

### 修复

- `docs/vocabulary-grammar.md`：`English Grammar in Use` 链接文字与实际指向不符（此前指向不相关的 Cambridge Grammar and Beyond 系列），改为该书官方页面
- Content Check 在 main 上已连续红两天：3 套测验题（q-health-b1/q-tech-b2/q-academic-c1）正确答案 75% 集中在同一下标，且 manifest.json 记录的 vocabulary/reading 两个文件 SHA256 与实际内容不符；重新打乱选项并重新生成 manifest
- lychee 链接检查缺少 `--timeout`/`--retry-wait-time`，单次瞬时超时就会导致整个 job 失败；调大容错窗口
- **content-check.yml 此前只在 `content/**`、`scripts/**` 变化时触发，从不因 `docs/**`（链接实际所在处）变化触发，也没有 schedule** —— 意味着仓库简介里写的"每周自动死链检测"当时并不成立；补上 `docs/**`、`templates/**`、`*.md` 触发路径和每周一定时任务
- `docs/index.md`（Pages 导航首页）只链接了 23 个文档里的 14 个，漏掉 2026-07-19 加入的全部 8 篇学习方法文档和新增的错词错句本；补全
- README 快速开始表格里两行分别指向"看下面的分类导航"，读起来像复制粘贴遗留；合并为一行

### 变更

- README 补充目录（TOC）、贡献入口、License 小节，把新增的 8 篇学习方法文档和 GitHub Pages 入口纳入导航

## [2.0.0] - 2026-07-19 ~ 2026-07-29 · 数据质量与内容升级

- 新增结构化内容数据体系：`content/vocabulary.json`（分级词汇）、`content/reading.json`（分级阅读）、`content/quizzes.json`（测验题库），均带 JSON Schema 约束（`content/schema/`）
- 新增校验与生成脚本：`scripts/validate_content.py`（Schema 校验 + 答案分布/释义污染检查）、`scripts/generate_manifest.py`（生成 `content/manifest.json` 同步契约）
- 新增 CI（`content-check.yml`）：push/PR 自动跑 Schema 校验、manifest 一致性检查、Markdown 死链检查（lychee）
- 新增 8 篇学习方法（元认知）文档：主动回忆法、康奈尔笔记法、考试焦虑应对、费曼技巧、交错练习、元认知、番茄工作法、学习小组
- 内容持续扩充至 v2026.07.29.1（词汇 304 / 阅读 51 / 测验 12）
- 修复 CI 中 manifest 行尾一致性问题和 lychee 误报（新增 `.lycheeignore`、`.gitattributes` 强制 LF）

## [1.1.0] - 2026-07-13

- 新增 `docs/ai-english.md`：AI 陪练指南，接入六能力点体系
- 清理失效链接（bbc-english-china.com、tingclass.net 已下线；byoungd 仓库改名为 up）

## [1.0.0] - 2026-05-26 ~ 2026-06-03

- 建立分类导航：听力、口语、阅读、写作、词汇与语法、考试、程序员英语、工具
- 新增自适应学习计划、30 天学习路线、打卡与复盘模板
- 新增中国环境友好资源、GitHub 项目精选、精选合集
