# Changelog

## [1.0.0] - 2026-06-03

### 新增
- **SKILL.md**: 完整的"管理学院毕业论文模拟答辩评委"系统提示词，包含角色设定、评审基本原则、六步评审流程和输出风格规范
- **文档体系**: 项目说明 README.md（中文）及 README.en.md（英文），含 shields.io 徽章、功能清单、快速开始指南、贡献指南和路线图
- **提问库**: knowledge/question-bank.md，按四大研究范式（问卷研究、实验研究、质性研究、二手数据研究）分类，每类 ≥10 个提问，附加追问策略和应答质量评判标准
- **危险信号清单**: knowledge/red-flags.md，按致命/严重/警告三级分级，每级 ≥5 条并附具体例子和修改建议，新增外审评分表参考
- **模拟答辩示例**: examples/sample-dialogue.md，完整 5 轮模拟答辩对话，展示学生犯错→评委指出→修正的闭环过程
- **FAQ 文档**: docs/FAQ.md，10 个常见问题解答
- **最佳实践指南**: docs/BEST_PRACTICES.md，5 个使用最佳实践主题
- **评分表**: docs/SCORING.md，7 维度答辩评分表与四档评估标准
- **社区模板**: .github/ISSUE_TEMPLATE/bug_report.md、feature_request.md 和 .github/PULL_REQUEST_TEMPLATE.md
- **隐私保护**: .gitignore 文件，防止原始答辩素材误上传

### 变更
- 重写 README.md，从简短说明扩展为完整的项目文档
- 重构 question-bank.md，从按主题分类改为按研究范式分类
- 重构 red-flags.md，从扁平清单改为三级分级体系
- 扩展 sample-dialogue.md，从 1 轮对话扩展为 5 轮完整对话

### 安全
- 使用 `git filter-branch` 重写全部提交历史，将原始 author/committer 信息替换为 GitHub 匿名邮箱保护隐私