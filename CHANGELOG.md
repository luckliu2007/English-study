# 更新日志 / Changelog

本项目的重要变更会记录在这个文件里，格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [Unreleased] - 2026-07-31

### 新增

- 社区健康文件：`CODE_OF_CONDUCT.md`、Issue 模板（资源推荐 / 失效链接报告）、PR 模板，提升 GitHub Community Standards 达标率
- 本 CHANGELOG

### 修复

- `docs/vocabulary-grammar.md` 中链接文字与实际指向不符的问题：`English Grammar in Use` 之前指向的是另一个不相关的 Cambridge 系列（Grammar and Beyond），已改为该书官方页面

### 变更

- README 补充目录（TOC）、贡献入口、License 小节，并把新增的 8 篇学习方法文档纳入分类导航

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
