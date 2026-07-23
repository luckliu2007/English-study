# 贡献指南

欢迎继续补充资源。建议每条资源包含：

- 名称
- 链接
- 简短说明
- 适合水平：入门 / 初级 / 中级 / 高级
- 是否免费

## 推荐格式

```md
| [资源名称](https://example.com/) | 一句话说明资源适合什么场景 |
```

## 收录标准

- 链接可访问
- 内容质量稳定
- 不包含明显侵权内容
- 不以广告和付费转化为主
- 能帮助学习者实际练习

## 不建议收录

- 只有标题党文章、内容很浅的网页
- 需要大量付费才能使用的资源
- 长期无法访问或维护停止的项目
- 版权来源不清晰的材料下载站

## 贡献结构化内容（content/*.json）

如果你要新增词汇、阅读或测验数据：

- 字段必须符合 [`content/schema/`](content/schema/) 下对应的 JSON Schema。
- 词汇 `meaning` 必须是纯中文，不能以空格或英文字母开头。
- 测验/阅读理解题的正确答案要打乱选项顺序，同一套题里正确下标不要集中在一个位置（CI 会拦截单一下标占比 ≥60% 的情况）。
- 阅读条目要标明 `type`：`article`（原创英文短文）或 `guide`（指向仓库文档的导航）。
- 提交前本地跑一遍校验，并重新生成 manifest：

  ```bash
  pip install -r scripts/requirements.txt
  python scripts/validate_content.py
  python scripts/generate_manifest.py
  ```
