# English Study

[![Content Check](https://github.com/luckliu2007/English-study/actions/workflows/content-check.yml/badge.svg)](https://github.com/luckliu2007/English-study/actions/workflows/content-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Pages](https://img.shields.io/badge/GitHub-Pages-blue.svg)](https://luckliu2007.github.io/English-study/)
[![Last Commit](https://img.shields.io/github/last-commit/luckliu2007/English-study)](https://github.com/luckliu2007/English-study/commits/main)
[![Issues](https://img.shields.io/github/issues/luckliu2007/English-study)](https://github.com/luckliu2007/English-study/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/luckliu2007/English-study/pulls)

面向中文学习者的英语学习资源库。这里不追求把链接堆满，而是把能长期使用的高质量资源按场景分类，配上学习路线和打卡模板，方便每天真正用起来。

> A curated, actively-maintained English learning hub for Chinese speakers — organized by skill (listening / speaking / reading / writing / vocabulary), backed by schema-validated structured content (`content/*.json`), an adaptive study plan, check-in templates, and CI that validates content and checks for dead links on every push.

## 目录

- [快速开始](#快速开始)
- [分类导航](#分类导航)
- [今日最小任务](#今日最小任务)
- [自适应学习闭环](#自适应学习闭环)
- [推荐起步组合](#推荐起步组合)
- [30 天路线](#30-天路线)
- [资源选择标准](#资源选择标准)
- [结构化内容数据](#结构化内容数据)
- [如何贡献](#如何贡献)
- [更新日志](#更新日志)
- [License](#license)

## 快速开始

| 你现在想做什么 | 推荐入口 |
| --- | --- |
| 不知道怎么开始 | [30 天学习路线](docs/learning-path.md) |
| 想按算法式计划自动安排任务 | [自适应学习计划](docs/adaptive-plan.md) |
| 想让 AI 当你的陪练 | [用 AI 学英语](docs/ai-english.md) |
| 想找高质量 GitHub 英语资源 | [精选合集](docs/awesome-lists.md) |
| 想直接用 GitHub 上的学习项目 | [GitHub 项目精选](docs/github-projects.md) |
| 想在国内网络环境下稳定学习 | [中国环境友好资源](docs/china-friendly.md) |
| 想每天打卡 | [学习打卡模板](templates/daily-check-in.md) |
| 想整理错词错句 | [错词错句本](templates/error-log.md) |
| 想按技能找资源，或想调整学习方法本身（记忆、专注、抗考试焦虑） | 看下面的分类导航 |

## 分类导航

| 分类 | 内容 |
| --- | --- |
| [听力](docs/listening.md) | 播客、慢速英语、真实语料输入 |
| [自适应学习计划](docs/adaptive-plan.md) | 诊断水平、生成每日任务、复盘弱项 |
| [用 AI 学英语](docs/ai-english.md) | AI 口语陪练、写作批改、提示词库 |
| [口语](docs/speaking.md) | 跟读、发音、影子训练、对话练习 |
| [阅读](docs/reading.md) | 分级读物、新闻、泛读材料 |
| [写作](docs/writing.md) | 语法检查、写作练习、学术/职场表达 |
| [词汇与语法](docs/vocabulary-grammar.md) | 单词、Anki、语法系统学习 |
| [GitHub 项目精选](docs/github-projects.md) | 开源英语学习项目、词汇库、程序员发音 |
| [精选合集](docs/awesome-lists.md) | GitHub 上值得收藏的英语学习资源合集 |
| [中国环境友好资源](docs/china-friendly.md) | 国内更稳定访问、可离线、适合通勤学习 |
| [考试](docs/exams.md) | IELTS、TOEFL、四六级、综合测试 |
| [程序员英语](docs/developer-english.md) | 技术文档、开源协作、工程师职场英语 |
| [工具](docs/tools.md) | 字典、字幕、浏览器插件、AI 辅助工具 |

### 学习方法（元认知）

| 方法 | 解决什么问题 |
| --- | --- |
| [主动回忆法](docs/active-recall.md) | 用测试代替重复阅读，记得更牢 |
| [康奈尔笔记法](docs/cornell-notes.md) | 听课/阅读时如何做结构化笔记 |
| [考试焦虑应对](docs/exam-anxiety.md) | 考前紧张、发挥失常的调节方法 |
| [费曼技巧](docs/feynman.md) | 用"讲给别人听"检验是否真的学会 |
| [交错练习](docs/interleaving.md) | 打乱练习顺序反而学得更牢的原理 |
| [元认知](docs/metacognition.md) | 如何监控和调整自己的学习策略 |
| [番茄工作法](docs/pomodoro.md) | 专注力管理和时间分块 |
| [学习小组](docs/study-group.md) | 如何组织高效的英语学习搭子/小组 |

## 今日最小任务

忙的时候只做这三件事也算完成：

- 听 5 分钟英文
- 复习 10 张单词卡
- 跟读 3 句话

## 自适应学习闭环

这个仓库现在按“测评 -> 分级 -> 训练 -> 复盘 -> 调整”的方式使用：

1. 用 [入学测评模板](templates/placement-test.md) 判断起点。
2. 按 [自适应学习计划](docs/adaptive-plan.md) 生成每天 20-35 分钟任务。
3. 用 [每日打卡模板](templates/daily-check-in.md) 记录完成度和错误。
4. 把当天的错误沉淀到 [错词错句本](templates/error-log.md)，滚动复习直到掌握。
5. 每周用 [周复盘模板](templates/weekly-review.md) 调整下一周任务。

## 推荐起步组合

| 技能 | 推荐组合 |
| --- | --- |
| 听力 | 每日英语听力 / 可可英语 + BBC Learning English 慢速节目 |
| 词汇 | Anki / TypeWords + 自己的例句卡片 |
| 口语 | YouGlish / 技术词发音清单 + 每天 10 分钟跟读 |
| 阅读 | Engoo Daily News / 新概念英语 GitHub 笔记 / 技术文档 |
| 写作 | LanguageTool / DeepL Write / AI 辅助修改，再整理错句 |

## 30 天路线

| 阶段 | 目标 | 每天任务 |
| --- | --- | --- |
| 第 1-7 天 | 建立节奏 | 慢速听力 10 分钟 + 单词复习 |
| 第 8-14 天 | 增加输出 | 跟读 5 句 + 写 5 句英文 |
| 第 15-21 天 | 提升真实输入 | 听播客片段 + 读短新闻 |
| 第 22-30 天 | 形成闭环 | 复述内容 + 整理错词错句 |

完整版本见：[学习路线](docs/learning-path.md)。

## 资源选择标准

- 免费或有可用的免费部分
- 内容稳定，更新较持续
- 能直接用于练习，而不只是方法论
- 适合自学者长期重复使用
- 优先选择开源、官方、社区口碑好的项目
- 国内使用时优先选择可离线、有文本、有字幕、有替代入口的资源

## 结构化内容数据

`content/` 下是可被程序消费的结构化学习数据（词汇、分级阅读、测验），带 JSON Schema 约束：

| 文件 | 内容 | Schema |
| --- | --- | --- |
| [`content/vocabulary.json`](content/vocabulary.json) | 分级词汇（CEFR A1–C2，含音标/例句/中文释义） | [schema](content/schema/vocabulary.schema.json) |
| [`content/reading.json`](content/reading.json) | 分级阅读：`article`（原创英文短文，带生词表+理解题）与 `guide`（仓库文档导航） | [schema](content/schema/reading.schema.json) |
| [`content/quizzes.json`](content/quizzes.json) | 测验题库（选项顺序随机，答案分布均衡） | [schema](content/schema/quizzes.schema.json) |
| [`content/prompts.json`](content/prompts.json) | AI 提示词库：28 条按六能力点 + 考试 + 长期人设 + 错题复盘分类的英文提示词模板 | [schema](content/schema/prompts.schema.json) |
| [`content/manifest.json`](content/manifest.json) | 同步契约（各文件 SHA256 + 条目数），由脚本自动生成 | — |

本地校验与生成：

```bash
pip install -r scripts/requirements.txt
python scripts/validate_content.py          # 按 Schema 校验 + 检查答案分布/释义污染
python scripts/generate_manifest.py         # 重新生成 manifest（内容变更后运行）
```

CI（[`content-check.yml`](.github/workflows/content-check.yml)）会在每次 push/PR 自动跑 Schema 校验、manifest 一致性检查和 Markdown 死链检查。

## 如何贡献

欢迎补充资源、修复失效链接、改进学习计划或结构化内容。参与前请先读一下 [行为准则](CODE_OF_CONDUCT.md)。几种方式：

- 提交 [资源推荐 issue](https://github.com/luckliu2007/English-study/issues/new?template=resource-suggestion.yml)
- 提交 [失效链接报告 issue](https://github.com/luckliu2007/English-study/issues/new?template=broken-link.yml)
- 直接发 Pull Request：普通资源条目按 [贡献指南](CONTRIBUTING.md) 的格式补充到对应分类；`content/*.json` 的改动同样遵循 CONTRIBUTING.md 里“贡献结构化内容”一节的规则

每条资源尽量写清楚：适合什么水平、解决什么问题、是否免费。

## 更新日志

版本历史见 [CHANGELOG.md](CHANGELOG.md)。

## License

本项目采用 [MIT License](LICENSE)。资源列表指向的第三方内容遵循其各自版权，仅供学习参考。

## 免责声明

本仓库只做学习资源整理。部分第三方资源可能包含付费功能，请根据自己的学习目标和预算选择。
