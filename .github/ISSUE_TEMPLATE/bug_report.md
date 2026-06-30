---
name: Bug Report
description: 报告项目中的问题
title: "[Bug] "
labels: ["bug"]
assignees:
  -
projects:
  -
milestone:
body:
  - type: markdown
    attributes:
      value: |
        ## 🐛 Bug 报告

        感谢您花时间报告这个问题！请尽可能详细地填写以下信息，以便我们快速定位和修复问题。

  - type: textarea
    id: description
    attributes:
      label: 问题描述
      description: 请清晰简洁地描述这个 Bug 是什么。
      placeholder: 请描述您遇到的问题...
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: 复现步骤
      description: 请提供复现该问题的详细步骤。
      placeholder: |
        1. 打开 '...'
        2. 点击 '....'
        3. 滚动到 '....'
        4. 看到错误
      render: markdown
    validations:
      required: true

  - type: textarea
    id: expected_behavior
    attributes:
      label: 期望行为
      description: 请描述您期望发生的结果。
      placeholder: 期望发生的事情...
    validations:
      required: true

  - type: textarea
    id: actual_behavior
    attributes:
      label: 实际行为
      description: 请描述实际发生的结果。
      placeholder: 实际发生的事情...
    validations:
      required: true

  - type: textarea
    id: screenshots
    attributes:
      label: 截图
      description: 如果可以，请添加截图以帮助解释您的问题。
      placeholder: 拖拽图片到此处或粘贴截图链接...
    validations:
      required: false

  - type: markdown
    attributes:
      value: |
        ## 环境信息

  - type: input
    id: os
    attributes:
      label: 操作系统
      description: 例如 Windows 11、macOS 14.0、Ubuntu 22.04
      placeholder: Windows 11
    validations:
      required: false

  - type: input
    id: browser
    attributes:
      label: 浏览器
      description: 例如 Chrome 120、Safari 17、Firefox 121
      placeholder: Chrome 120
    validations:
      required: false

  - type: input
    id: version
    attributes:
      label: 项目版本
      description: 您正在使用的项目版本
      placeholder: v1.0.0
    validations:
      required: false

  - type: textarea
    id: additional_context
    attributes:
      label: 其他上下文
      description: 任何其他有助于解决问题的上下文信息，如日志文件、错误截图等。
      placeholder: 添加任何其他相关信息...
    validations:
      required: false

  - type: checkboxes
    id: terms
    attributes:
      label: 确认清单
      description: 提交前请确认
      options:
        - label: 我已搜索现有 Issue，确认没有重复报告相同问题
          required: true
        - label: 我已提供详细的复现步骤和必要的环境信息
          required: true