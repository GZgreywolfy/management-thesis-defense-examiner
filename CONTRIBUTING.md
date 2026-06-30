# 贡献指南

感谢你对本项目的关注！我们欢迎任何形式的贡献——无论是提出新想法、报告问题、改进文档还是提交代码。

---

## 📋 提交 Issue

如果你有建议或发现了问题，欢迎 [提交 Issue](https://github.com/GZgreywolfy/management-thesis-defense-examiner/issues/new)。

### Bug 报告

请包含以下信息：

- **清晰描述问题**：说明实际行为与预期行为的差异
- **复现步骤**：如何重现该问题
- **环境信息**：操作系统、AI 平台（ChatGPT/Claude/Kimi/DeepSeek 等）
- **截图或日志**：如有，附上相关截图或错误信息

### 功能建议

请包含以下信息：

- **预期行为**：你希望该功能做什么
- **使用场景**：在什么情况下你会用到这个功能
- **实现思路**：如有初步想法，欢迎分享

---

## 🔧 提交 Pull Request

### 流程

1. **Fork** 本仓库
2. 创建你的特性分支：`git checkout -b feat/your-feature-name`
3. **提交** 你的改动：`git commit -m 'feat: add your feature'`
4. **推送** 到分支：`git push origin feat/your-feature-name`
5. 打开一个 **Pull Request**

### PR 规范

- PR 标题请遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
  - `feat:` 新功能
  - `fix:` 修复
  - `docs:` 文档更新
  - `refactor:` 重构
  - `style:` 格式调整（不影响功能）
  - `test:` 测试相关
  - `chore:` 构建/工具变更
- PR 描述请说明变更内容和动机
- 保持 PR 范围聚焦，一个 PR 解决一个问题

---

## 💻 本地开发

```bash
# 克隆仓库
git clone https://github.com/GZgreywolfy/management-thesis-defense-examiner.git
cd management-thesis-defense-examiner

# 安装依赖（如果有 Python 辅助脚本）
pip install -r requirements.txt  # 如果有

# 修改 SKILL.md 或 knowledge/ 下的文件后，使用 replace_authors.py 确保占位符一致性
python replace_authors.py --check
```

---

## 📝 贡献规范

### 内容要求

- **所有示例对话必须为虚构数据**，不得包含真实姓名、院校或选题
- **提问逻辑应遵循管理学主流研究范式**（问卷实验、二手数据、扎根理论、元分析等）
- **新增知识点请附参考文献支撑**，确保学术严谨性
- 保持文档语言风格一致：中文为主要文档语言，README.en.md 为英文翻译

### 质量标准

- 所有 Markdown 文件格式规范，代码块标注语言类型
- 添加新文件时，同步更新 README.md 中的目录结构
- 保持 MIT 许可证不变

---

## 🤝 行为准则

- **保持尊重**：所有讨论和反馈都应基于建设性的专业交流
- **欢迎初学者**：本项目欢迎各水平的贡献者，我们愿意帮助新手
- **聚焦目标**：讨论应聚焦于如何改进项目，而非个人偏好
- **包容开放**：欢迎不同背景的贡献者参与

---

## ❓ 有问题？

欢迎通过 [Issue](https://github.com/GZgreywolfy/management-thesis-defense-examiner/issues/new) 或 [Discussion](https://github.com/GZgreywolfy/management-thesis-defense-examiner/discussions) 与我们联系。

再次感谢你的贡献！🎉