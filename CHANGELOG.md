# 更新日志 / Changelog

本项目的重要变更会记录在这个文件里，格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [Unreleased]

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
