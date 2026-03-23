---
agent: agent
description: 创建新的编程作业
argument-hint: 提供作业详情
---

# Create New Programming Assignment

你的目标是为 Mergington High School 的学生生成一个新的编程作业。

## 第一步：收集作业信息

如果用户未提供，请询问作业的主题、学习目标、所需技能以及任何特殊要求或截止日期。

## 第二步：创建作业结构

1. 在 `assignments` 文件夹中根据作业主题创建一个唯一名称的新目录。
2. 在该目录中创建一个名为 `README.md` 的文件，文件结构应遵循 [assignment-template.md](../../templates/assignment-template.md)。
3. 在 `README.md` 中填写作业详情（标题、目标、任务描述、要求和示例）。
4. （可选）如需提供起始代码或附件，请将这些文件添加到同一作业文件夹中（例如 `starter-code.py`、数据文件、测试用例等）。

## 第三步：更新网站配置

在网站配置文件 [config.json](../../config.json) 的作业列表中添加新作业。对于 `dueDate` 字段，除非另有指定，否则使用当前日期加 7 天作为默认截止日期。
