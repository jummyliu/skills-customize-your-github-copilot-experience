# 📘 Assignment: Python Text Processing

## 🎯 Objective

Build utilities for processing and analyzing text files. Students will practice string manipulation, file I/O, regular expressions, and basic text statistics (word/line counts, frequency analysis).

## 🎯 目标

实现用于处理和分析文本文件的工具。学生将练习字符串操作、文件输入/输出、正则表达式以及基本文本统计（词数/行数、频率分析）。

## 📝 Tasks

### 🛠️ Implement text-processing utilities

#### Description

Write a command-line Python program that reads a text file and provides the following utilities: count lines, count words, compute frequency of each word (case-insensitive), find and replace a substring, and extract lines matching a regex pattern.

#### 描述

编写一个命令行 Python 程序，读取文本文件并提供以下功能：统计行数、统计词数、计算每个单词的频率（不区分大小写）、查找并替换子字符串、提取匹配正则表达式的行。

#### Requirements

Completed program should:

- Accept a file path as input and handle file-not-found errors gracefully.
- Provide commands/options to: `--count-lines`, `--count-words`, `--freq`, `--find-replace <old> <new>`, `--grep <pattern>`.
- For `--freq`, output the top N most common words (default 10) and support an option to ignore a list of stopwords.
- Preserve file encoding and avoid data loss when writing replacements (write to a new file or ask before overwrite).
- Include docstrings and a short `README` usage example in the file header or repository README.

#### 要求

完成的程序应满足：

- 接受文件路径作为输入，并优雅处理文件未找到错误。
- 提供命令/选项：`--count-lines`、`--count-words`、`--freq`、`--find-replace <old> <new>`、`--grep <pattern>`。
- 对于 `--freq`，输出最常见的前 N 个单词（默认 10），并支持忽略 stopwords 列表的选项。
- 保持文件编码，写入替换结果时避免数据丢失（写入新文件或在覆盖前询问）。
- 包含 docstrings 以及在文件头部或仓库 README 中提供简短的使用示例。

#### Example usage / 示例用法

```
# Count lines
python text_tool.py --count-lines sample.txt

# Top 20 frequent words ignoring stopwords
python text_tool.py --freq sample.txt --top 20 --ignore-stopwords stopwords.txt

# Find & replace
python text_tool.py --find-replace sample.txt old_word new_word --out replaced.txt

# Grep-like extract
python text_tool.py --grep sample.txt "^Chapter" > chapters.txt
```

**Skills practiced / 练习技能:** String manipulation, file I/O, regular expressions, text parsing, command-line argument parsing.
