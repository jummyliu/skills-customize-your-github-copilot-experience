
# 📘 Assignment: Python Basics

> 🟢 **难度 / Difficulty：初级 (Beginner)**

## 🎯 Objective

Practice fundamental Python programming skills including user input, string formatting, arithmetic operations, and conditional statements by implementing simple functions.

## 🎯 目标

通过实现简单函数，练习 Python 基础编程技能，包括用户输入、字符串格式化、算术运算以及条件语句。

## 📝 Tasks / 任务

### 🛠️ User Input and String Formatting / 用户输入与字符串格式化

#### Description
Write a function called `welcome_message()` that interacts with the user and returns a formatted welcome message.

#### 描述
编写一个名为 `welcome_message()` 的函数，与用户交互并返回一条格式化的欢迎信息。

#### Requirements
Completed program should:

- Ask the user for their name, age, and favorite color using `input()`.
- Return a welcome message formatted as:
  `Hello, [name]! You are [age] years old and your favorite color is [color].`
- Example output:
  `Hello, Alice! You are 25 years old and your favorite color is blue.`

#### 要求
完成的程序应满足：

- 使用 `input()` 询问用户的姓名、年龄和最喜欢的颜色。
- 返回格式如下的欢迎信息：
  `Hello, [name]! You are [age] years old and your favorite color is [color].`
- 示例输出：
  `Hello, Alice! You are 25 years old and your favorite color is blue.`

### 🛠️ Basic Arithmetic / 基本算术

#### Description
Write a function called `add_two_numbers()` that prompts the user for two numbers and prints their sum.

#### 描述
编写一个名为 `add_two_numbers()` 的函数，提示用户输入两个数字并打印它们的和。

#### Requirements
Completed program should:

- Ask the user to enter two numbers.
- Add the numbers together.
- Print the result. Example:
  Enter the first number: 3
  Enter the second number: 7
  10

#### 要求
完成的程序应满足：

- 提示用户输入两个数字。
- 将两个数字相加。
- 打印结果。示例：
  Enter the first number: 3
  Enter the second number: 7
  10

### 🛠️ Conditional Statements / 条件语句

#### Description
Write a function called `is_even()` that checks if a number is even.

#### 描述
编写一个名为 `is_even()` 的函数，判断一个数字是否为偶数。

#### Requirements
Completed program should:

- Take a single integer argument.
- Return `True` if the number is even, and `False` if it is odd.
- Example usage:
  ```python
  print(is_even(4))  # True
  print(is_even(5))  # False
  ```

#### 要求
完成的程序应满足：

- 接受一个整数参数。
- 如果数字为偶数，返回 `True`；如果为奇数，返回 `False`。
- 示例用法：
  ```python
  print(is_even(4))  # True
  print(is_even(5))  # False
  ```

## 🚀 Advanced Challenges / 进阶挑战

> 完成以上任务后，尝试以下进阶挑战来加深理解！

1. **Input Validation / 输入验证**：Modify `add_two_numbers()` to handle non-numeric input gracefully using a `try/except` block and prompt the user to re-enter a valid number. / 使用 `try/except` 处理非数字输入，并提示用户重新输入有效数字。

2. **Extended Arithmetic / 扩展算术**：Add functions for subtraction, multiplication, and division. Handle division by zero. / 增加减法、乘法和除法函数，并处理除以零的情况。

3. **FizzBuzz Challenge / FizzBuzz 挑战**：Write a function `fizzbuzz(n)` that prints numbers from 1 to `n`, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz". / 编写函数 `fizzbuzz(n)`，打印 1 到 `n` 的数字，3 的倍数替换为 "Fizz"，5 的倍数替换为 "Buzz"，两者的倍数替换为 "FizzBuzz"。

