# 用 AI 学英语

AI 对话工具是目前最容易获得的英语陪练：无限耐心、随时可用、可以按你的水平调整难度。它的价值是**陪练和即时反馈**，不是替你输出——你自己说出来、写出来的部分才算练习量。

## 可以用的工具

| 工具 | 说明 |
| --- | --- |
| [ChatGPT](https://chatgpt.com/) | 支持语音对话，适合口语陪练和写作批改；支持 Custom GPT 保存人设 |
| [Claude](https://claude.ai/) | 长文本理解好，适合精读讲解和写作批改；支持 Projects 保存人设 |
| [Gemini](https://gemini.google.com/) | 支持语音对话，和 YouTube 内容结合方便；支持 Gems 保存人设 |
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
6. 一次配置好人设，别每次对话都重新交代背景——见下面「配置长期 AI 导师人设」。

## 结构化提示词库

这个模块的核心不是本页的文字，而是 [`content/prompts.json`](../content/prompts.json)：28 条带 [JSON Schema](../content/schema/prompts.schema.json) 约束的 AI 提示词，和 `vocabulary.json` / `reading.json` / `quizzes.json` 走同一套校验和 CI（见 [结构化内容数据](../README.md#结构化内容数据)）。每条记录包含：

- `category`：对应 [自适应学习计划](adaptive-plan.md) 的六能力点 `L/P/F/V/G/W`，外加 `exam`（考试模拟）、`tutor-setup`（长期人设配置）、`review`（错题/周复盘）
- `prompt`：英文提示词模板，`[方括号]` 是需要替换的变量，`variables` 字段逐个解释
- `usage`：什么场景用、怎么用
- `followUp`（可选）：用完之后产出该沉淀到哪个模板

| 分类 | 数量 | 解决什么问题 |
| --- | --- | --- |
| `L` 听力理解 | 4 | 拆连读、听写纠错、播客理解自测、口音适应 |
| `P` 发音准确 | 3 | 易混音对比、重音检查、技术词错音自查 |
| `F` 口语流利 | 4 | 场景角色扮演、复述挑战、观点辩论、日常寒暄 |
| `V` 词汇短语 | 3 | 例句 + Anki 卡片、近义词辨析、搭配挖掘 |
| `G` 语法句型 | 3 | 错句归类、句型转换、语法自测题生成 |
| `W` 写作表达 | 4 | 三步批改闭环、语域转换、提纲教练、技术写作润色 |
| `exam` 考试模拟 | 3 | IELTS 口语模拟考、TOEFL 写作评分、CEFR/雅思水平诊断 |
| `tutor-setup` 长期人设 | 2 | 持久化导师系统提示词、周度能力诊断生成器 |
| `review` 错题复盘 | 2 | 错题周测、间隔复习排期计算 |

用法：打开 `content/prompts.json`，按 `category` 或 `id` 找到需要的条目，把 `prompt` 里的 `[变量]` 换成自己的内容，粘贴给 AI。程序化使用（比如自己写脚本批量生成练习）也可以直接读这个文件。

## 配置长期 AI 导师人设

不想每次对话都重新交代"我在学英语、什么水平、别帮我写"，可以把 `content/prompts.json` 里的 `p-tutor-persona` 设成一个持久化角色：

1. **ChatGPT**：Explore GPTs → Create → 把 `p-tutor-persona` 的 `prompt`（替换 `[level]` 为自己的等级）粘进 Instructions。
2. **Claude**：新建 Project → Project instructions → 同样粘贴，之后这个 Project 里的每次对话都会带着这个人设。
3. **Gemini**：Gems → New Gem → Instructions 里粘贴。
4. **国内工具**（豆包 / Kimi / 通义 / DeepSeek）：多数支持"角色/记忆"或"系统提示词"设置，同样粘贴；如果不支持，就把这段话固定存成一个 Snippet，每次对话开头粘一次。

配置好之后，每周用 `p-tutor-weekly-diagnostic` 把打卡记录喂给它，输出可以直接抄进 [周复盘模板](../templates/weekly-review.md)。

## 三个现成训练流程

### 每日 10 分钟口语陪练

对应 `p-speaking-roleplay`：

```text
Let's role-play [scenario]. Ask me one question at a time in character.
After each of my answers, give me one more natural way to say the
same thing, then continue the role-play.
```

结束后把更地道的说法抄进 [每日打卡模板](../templates/daily-check-in.md)。

### 写作批改闭环

对应 `p-writing-3step`：

1. 自己写 5-10 句英文（日记、总结、观点）。
2. 用 `p-writing-3step` 的提示词让 AI 讲解，不代写。
3. 根据讲解自己重写一遍，再让 AI 检查重写版。
4. 把「原句 → 修改后 → 问题」记录进 [错词错句本](../templates/error-log.md)。

### 错题本复习

对应 `p-review-weekly-quiz` + `p-review-spaced-schedule`：每周把积累的错句、错音、生词发给 AI 做测验，答错的项目再用间隔复习提示词算出下次复习日期，安排进 [复习间隔](adaptive-plan.md#复习间隔)。

## 接入自适应计划

- 每日任务中的「到期复习」和「弱项补偿」都可以让 AI 出题（`review` 分类），代替自己翻笔记。
- 语音对话算 F（口语流利）的训练；AI 批改算 W（写作表达）的训练；照常打 0-5 分。
- 每周用 `p-tutor-weekly-diagnostic` 生成六能力点估分表，比自己手动估算更快。
- AI 反馈再多，每天只挑 1-2 条进错误整理表，避免复习堆积。

## 如何判断 AI 陪练是否真的有效

AI 陪练最大的风险是「虚假掌握感」：跟 AI 对话时觉得自己听懂了、说得出来，脱离 AI 就不行了。用这几条自查：

1. **能认出 ≠ 能产出**：AI 讲解的表达，隔几天不看提示自己能不能主动说出来，才算学会。
2. **定期脱离 AI 自测**：每 1-2 周用 [placement-test.md](../templates/placement-test.md) 或不带 AI 的听力/阅读材料测一次，看是否真的进步。
3. **对比录音**：口语练习定期录音，一个月后回听更早的录音，能听出差距才说明在进步，光凭感觉不准。
4. **警惕 AI 的礼貌性鼓励**：AI 默认倾向于说"你做得不错"，主动要求它更严格（见下方注意事项）。
5. **看输出量而不是对话轮数**：聊了很久但都是 AI 在说、你在附和，不算有效练习。

## 注意事项

- AI 可能编造词组或过度礼貌。开头就要求它直接指出错误，不要客套。
- AI 生成的范文只用来对照学习，不要背下来当自己的输出。
- 不要把身份证件、公司机密等敏感信息放进对话。
- 网络不稳时换国内模型继续练，完全离线时回到本地模板和 Anki，不要中断打卡。
- `content/prompts.json` 里的提示词是模板起点，不是圣经；根据自己的水平和目标调整措辞比照抄更重要。
