# 词汇与语法

## 先定范围：权威分级词表

背词最常见的浪费，是背了大量用不到的词。先用分级词表定好范围，再决定背什么。

| 词表 | 说明 |
| --- | --- |
| [Oxford 3000 / Oxford 5000](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000) | 牛津学习词典的官方核心词表：Oxford 3000 是 A1–B2 学习者最该掌握的 3,000 词，Oxford 5000 再加 2,000 个 B2–C1 词。按 CEFR 标级，依据语料库频率和对学习者的实用性选词，可免费在线查看 |
| [New General Service List 系列](https://www.newgeneralservicelist.com/) | 基于语料库的开放词表项目，以知识共享协议免费提供（含商用）：通用高频词表 NGSL，以及学术（NAWL）、商务（BSL）、托业（TSL）、口语（NGSL-Spoken）等专项词表 |
| [first20hours/google-10000-english](https://github.com/first20hours/google-10000-english) | 高频英文词表，可做自定义词库 |
| [rspeer/wordfreq](https://github.com/rspeer/wordfreq) | 判断词汇常用程度，适合做词表筛选（作者已宣布停止更新，词频数据停在 2021 年前后，但做常用度判断仍然可靠，见 [SUNSET.md](https://github.com/rspeer/wordfreq/blob/master/SUNSET.md)） |

**建议顺序**：先掌握 Oxford 3000，再按目标选专项词表：考雅思托福、读论文看 NAWL，职场看 BSL，考托业看 TSL，想提升口语看 NGSL-Spoken。

## 记住它：间隔重复

| 资源 | 说明 |
| --- | --- |
| [Anki](https://apps.ankiweb.net/) | 间隔重复记忆工具，适合长期背词 |
| [Anki 牌组选项：FSRS](https://docs.ankiweb.net/deck-options.html) | 新版 Anki 内置 FSRS 调度算法，在牌组选项中开启。“期望记忆率”默认 90%：调低复习量明显减少但忘得更多，调高则复习量快速增加。一般保持默认，考前冲刺再适当调高 |
| [5mdld/anki-english-mwld-decks](https://github.com/5mdld/anki-english-mwld-decks)（原 anki-english-60k-decks） | 大型英语词汇 Anki 牌组 |
| [zyronon/TypeWords](https://github.com/zyronon/TypeWords) | 开源词汇和文章练习工具，适合边敲边记 |

## 查清楚：学习者词典

| 资源 | 说明 |
| --- | --- |
| [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) | 学习者词典，释义清楚，例句实用；词条标注是否属于 Oxford 3000/5000 |
| [Cambridge Dictionary](https://dictionary.cambridge.org/) | 释义、发音、搭配和语法说明 |

## 本仓库的词汇数据

[`content/vocabulary.json`](../content/vocabulary.json) 收录 322 个分级词条（A1–C2，含音标、中文释义和例句），其中带 `AI` 标签的是 2026 年新增的“AI 时代高频词”（agent、hallucination、prompt、token、latency、guardrail 等）。配套测验见 [`content/quizzes.json`](../content/quizzes.json) 中的 `q-ai-vocab-b2`。

## 语法

| 资源 | 说明 |
| --- | --- |
| [English Grammar in Use](https://www.cambridge.org/us/cambridgeenglish/catalog/grammar-vocabulary-and-pronunciation/english-grammar-use-5th-edition) | Murphy 经典语法书官方页面，B1-B2 自学语法首选 |
| [Perfect English Grammar](https://www.perfect-english-grammar.com/) | 清晰的语法讲解和练习 |
| [British Council Grammar](https://learnenglish.britishcouncil.org/grammar) | 官方语法课程和练习 |
| [protogenesis/New-Concept-English](https://github.com/protogenesis/New-Concept-English) | 新概念英语笔记，适合用课文带语法 |

## 背词建议

- 先用分级词表定范围，高频词优先，低频词少量补充。
- 不只背中文释义，要背英文例句。
- 每个词至少记录一个真实短语搭配。
- 复习比新学更重要：每天先清空 Anki 到期卡片，再学新词。
- 背完要用：每周用新词写 5 句话或复述一段内容，记进 [错词错句本](../templates/error-log.md)。
