# 用 AI 学英语

AI 对话工具是目前最容易获得的英语陪练：无限耐心、随时可用、可以按你的水平调整难度。它的价值是**陪练和即时反馈**，不是替你输出——你自己说出来、写出来的部分才算练习量。

## 可以用的工具

| 工具 | 说明 |
| --- | --- |
| [ChatGPT](https://chatgpt.com/) | 支持语音对话，适合口语陪练和写作批改 |
| [Claude](https://claude.ai/) | 长文本理解好，适合精读讲解和写作批改 |
| [Gemini](https://gemini.google.com/) | 支持语音对话，和 YouTube 内容结合方便 |
| [DeepSeek](https://www.deepseek.com/) | 国内直接可用，免费额度充足 |
| [Kimi](https://www.kimi.com/) | 国内直接可用，长文档阅读和讲解方便 |
| [豆包](https://www.doubao.com/) | 国内直接可用，App 支持语音通话练口语 |
| [通义](https://tongyi.aliyun.com/) | 国内直接可用，配合阿里系工具顺手 |

选择建议：国内网络优先用 DeepSeek / Kimi / 豆包 / 通义；能稳定访问海外服务再考虑 ChatGPT / Claude / Gemini。工具之间差别远小于「每天是否真的开口和动笔」。

## 基本原则

1. 每次只练一个目标：一次对话只练口语、只改作文或只学词汇，不要混着来。
2. 要求 AI 只纠正影响理解的 1-2 个错误，不要每句都打断。
3. 对 AI 给的表达保持怀疑：重要表达用 [Cambridge Dictionary](https://dictionary.cambridge.org/) 或 [YouGlish](https://youglish.com/) 验证真实用法。
4. 对话结束后把错句和新表达搬进打卡记录或 Anki，不要留在聊天记录里。
5. 不要让 AI 替你写：先自己写完，再让 AI 修改和讲解。

## 按能力点使用

对应 [自适应学习计划](adaptive-plan.md) 的 6 个能力分。

| 能力 | 用法 | 提示词示例 |
| --- | --- | --- |
| L 听力理解 | 把听不懂的句子发给 AI，拆解连读、弱读和生词 | `Explain why this sentence is hard to catch for learners: "..." Break down the connected speech.` |
| P 发音准确 | 用语音模式跟读对比；让 AI 生成易混音对比清单 | `Give me 10 minimal pairs to practice the sounds /ɪ/ vs /iː/, with example sentences.` |
| F 口语流利 | 语音对话做 30 秒复述和角色扮演（点餐、面试、站会） | `Let's role-play a job interview. Ask one question at a time. After each answer, give me one better expression.` |
| V 词汇短语 | 生成由易到难的例句；批量做成 Anki 卡片 | `Make Anki cards for these words: ... Format: word[TAB]definition + one example sentence.` |
| G 语法句型 | 把错句发给 AI 归类讲解，再做句型替换训练 | `Here are my wrong sentences this week: ... Group them by grammar issue and give me 3 practice sentences for each.` |
| W 写作表达 | 三步批改闭环：改正、讲解、自己重写 | `Correct my writing, explain the top 3 recurring mistakes, then let me rewrite it and check again.` |

## 三个现成训练流程

### 每日 10 分钟口语陪练

```text
Act as my English conversation partner. My level is [A2/B1/B2].
Talk about [today's topic]. Ask one question at a time.
Keep your replies under 3 sentences. After each of my answers,
correct only the 1-2 mistakes that most affect understanding.
At the end, list the corrections and 3 useful expressions.
```

结束后把纠错清单抄进 [每日打卡模板](../templates/daily-check-in.md) 的错误整理表。

### 写作批改闭环

1. 自己写 5-10 句英文（日记、总结、观点）。
2. 让 AI 批改并讲解：`Correct my English writing. Explain the top 3 recurring mistakes with examples.`
3. 根据讲解自己重写一遍，再让 AI 检查重写版。
4. 把「原句 → 修改后 → 问题」记录进打卡模板。

### 错题本复习

每周把本周积累的错句、错音、生词发给 AI：

```text
Here are my mistakes from this week: ...
Quiz me on them one by one. Don't show the answers first.
Tell me which ones I still get wrong and should review again next week.
```

答错的项目按 [复习间隔](adaptive-plan.md#复习间隔) 安排下次复习。

## 接入自适应计划

- 每日任务中的「到期复习」和「弱项补偿」都可以让 AI 出题，代替自己翻笔记。
- 语音对话算 F（口语流利）的训练；AI 批改算 W（写作表达）的训练；照常打 0-5 分。
- AI 反馈再多，每天只挑 1-2 条进错误整理表，避免复习堆积。

## 注意事项

- AI 可能编造词组或过度礼貌。开头就要求它直接指出错误，不要客套。
- AI 生成的范文只用来对照学习，不要背下来当自己的输出。
- 不要把身份证件、公司机密等敏感信息放进对话。
- 网络不稳时换国内模型继续练，完全离线时回到本地模板和 Anki，不要中断打卡。
