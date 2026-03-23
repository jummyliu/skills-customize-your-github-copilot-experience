# 📘 Assignment: Hangman Game Challenge

（中文：Hangman 游戏挑战）

## 🎯 Objective

Build the classic word-guessing game (Hangman). Students will practice string manipulation, loops, conditionals, and user input handling by creating an interactive command-line game.

## 🎯 目标

构建经典的猜词游戏（Hangman）。学生将练习字符串操作、循环、条件分支和用户输入处理，完成一个交互式命令行游戏。

## 📝 Tasks

### 🛠️ Implement the Hangman game

（中文：实现 Hangman 游戏）

#### Description

The program should randomly select a word from a predefined list. Players guess letters to gradually reveal the word. Players have a limited number of incorrect attempts; guessing the word before attempts run out results in a win, otherwise a loss.

#### 描述

程序应从预定义的单词列表中随机选择一个单词，玩家通过输入字母逐步揭示单词。玩家有固定次数的错误机会，猜对则获胜，次数用尽则失败。

#### Requirements

Completed program should:

- Randomly select a word from a predefined list.
- Accept single-letter guesses and display current progress in a `_ _ a _ _` format.
- Track and display remaining incorrect attempts.
- End when the word is fully guessed or attempts are exhausted, and show win/lose messages.
- Show guessed letters and avoid double-counting repeated guesses.

完成的程序应满足：

- 从预定义的单词列表中随机选择一个单词。
- 接受单个字母的输入，并以 `_ _ a _ _` 的格式显示当前猜测进度。
- 跟踪并显示剩余的错误次数（尝试次数）。
- 在单词被完整猜出或尝试次数耗尽时结束游戏，并显示相应的胜利或失败信息。
- 显示已猜过的字母并避免重复计数相同字母的错误。

#### Example session (示例会话)

```
Word: _ _ _ _ _
Guessed: a, e
Enter a letter: o
Correct! Progress: _ o _ _ _
Remaining incorrect attempts: 5
```

```
单词：_ _ _ _ _
已猜：a, e
请输入一个字母：o
正确！当前进度：_ o _ _ _
剩余错误次数：5
```

**Skills practiced / 练习技能:** String manipulation, loops, conditionals, random selection, user input handling.
