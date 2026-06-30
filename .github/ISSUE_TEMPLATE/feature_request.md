---
name: Feature Request
description: 建议新功能或改进
title: "[Feature] "
labels: ["enhancement"]
assignees:
  -
projects:
  -
milestone:
body:
  - type: markdown
    attributes:
      value: |
        ## ✨ 功能请求

        感谢您提出改进建议！请详细描述您希望的新功能或改进。

  - type: textarea
    id: feature_description
    attributes:
      label: 功能描述
      description: 请清晰简洁地描述您希望添加的功能。
      placeholder: 请描述您期望的功能...
    validations:
      required: true

  - type: textarea
    id: problem_solved
    attributes:
      label: 解决的问题
      description: 这个功能解决了什么问题？在使用过程中遇到了什么不便？
      placeholder: 当前存在的问题或使用痛点...
    validations:
      required: true

  - type: textarea
    id: proposed_solution
    attributes:
      label: 预期方案
      description: 请描述您预期的解决方案或实现方式。
      placeholder: 您认为应该如何实现这个功能...
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: 备选方案
      description: 您还考虑过哪些其他解决方案或变通方法？
      placeholder: 其他替代方案...
    validations:
      required: false

  - type: textarea
    id: additional_context
    attributes:
      label: 其他上下文
      description: 任何其他有助于理解功能需求的上下文信息，如截图、示例、参考资料等。
      placeholder: 添加任何其他相关信息...
    validations:
      required: false

  - type: checkboxes
    id: terms
    attributes:
      label: 确认清单
      description: 提交前请确认
      options:
        - label: 我已搜索现有 Issue，确认没有重复提出相同功能请求
          required: true
        - label: 我已详细描述该功能的使用场景和期望效果
          required: true