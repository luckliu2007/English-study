# 职场英语

工作中最常用英语的四个场景：**邮件、会议、演示、协商**。每个场景先背 5 个高频句式，再用 AI 角色扮演练成自己的话。程序员的技术文档、开源协作英语见 [程序员英语](developer-english.md)。

## 四个场景的高频句式

### 邮件：开门见山，一个明确请求，一个截止时间

| 用途 | 句式 |
| --- | --- |
| 说明来意 | I'm writing to follow up on [topic]. / Quick update on [project]: |
| 提出请求 | Could you please [action] by [day]? |
| 发送附件 | Please find the updated [document] attached. |
| 委婉催促 | Just checking in on [item]. Is there anything you need from me? |
| 结尾 | Let me know if you have any questions. / Thanks in advance. |

### 会议：澄清、表态、礼貌反对、总结

| 用途 | 句式 |
| --- | --- |
| 确认理解 | Just to make sure I understand, you're saying [summary]? |
| 表达观点 | From my side, I think [view], mainly because [reason]. |
| 礼貌反对 | I see your point, but I'm a bit concerned about [risk]. |
| 推迟讨论 | That's a good question. Can we take it offline? |
| 总结行动 | To summarize, we agreed that [A], and [person] will [task] by [day]. |

### 演示：先给结论，再讲依据

| 用途 | 句式 |
| --- | --- |
| 开场路线图 | Today I'll walk you through three things: [A], [B], and [C]. |
| 引导看图 | As you can see on this slide, [trend]. |
| 强调结论 | The key takeaway here is [point]. |
| 过渡 | That brings me to the next point. |
| 接受提问 | Happy to take any questions. |

### 协商：给选项，不只说“不”

| 用途 | 句式 |
| --- | --- |
| 交换条件 | We can be flexible on [X] if you can move on [Y]. |
| 探询底线 | What would it take to [goal]? |
| 争取时间 | Let me check with my team and get back to you by [day]. |
| 拒绝并给替代方案 | That doesn't quite work for us, but how about [alternative]? |
| 确认共识 | So, just to confirm, we've agreed on [terms]. |

## 用 AI 练

| 场景 | 提示词（见 [`content/prompts.json`](../content/prompts.json)） | 用法 |
| --- | --- | --- |
| 会议、协商 | `p-speaking-meeting-roleplay` 职场会议角色扮演 | AI 扮演经理、客户或合作方，会故意提出反对意见；每 3 轮复盘一次 |
| 邮件 | `p-writing-email-polish` 商务邮件批改 | 发重要邮件前自查目的、请求、截止时间和语气，只讲解不代写 |
| 通用对话 | `p-speaking-roleplay` 情景角色扮演 | 求职面试、电话沟通、商务社交等任意场景 |

完整用法见 [用 AI 学英语](ai-english.md)。

## 学习资源

| 资源 | 说明 |
| --- | --- |
| [Purdue OWL：职场与技术写作](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html) | 普渡大学写作中心的免费讲义：商务信函、备忘录、报告、求职材料的格式和写法 |
| [Business English: Networking（华盛顿大学，Coursera）](https://www.coursera.org/learn/business-english-intro) | 商务英语沟通系列课程中的一门：自我介绍、介绍工作和公司、写职业邮件、电话与邮件约会议。可免费注册，证书需付费 |
| [Microsoft 写作风格指南](https://learn.microsoft.com/en-us/style-guide/welcome/) | 简洁、友好、面向读者的职场写作原则 |

## 4 周练习计划

| 周 | 场景 | 每天 15 分钟 | 周末产出 |
| --- | --- | --- | --- |
| 1 | 邮件 | 把当天一封中文工作消息改写成英文邮件，用 `p-writing-email-polish` 自查 | 5 封邮件 + 自己最常犯的 3 个问题 |
| 2 | 会议 | 用 `p-speaking-meeting-roleplay` 练一个真实议题，录音回听 | 个人会议句式库（≥15 句） |
| 3 | 演示 | 用“路线图 → 三个要点 → 结论”的结构讲 2 分钟，录音 | 一段 2 分钟英文演示录音 |
| 4 | 协商 | 角色扮演一次延期或预算谈判，要求 AI 至少反对两次 | 一页“我的协商句式”清单 |

所有句式和错误都整理进 [错词错句本](../templates/error-log.md)，按 [自适应学习计划](adaptive-plan.md) 的节奏复习。
