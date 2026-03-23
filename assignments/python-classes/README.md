# 📘 Assignment: Python Classes

> 🟡 **难度 / Difficulty：中级 (Intermediate)**

## 🎯 Objective

Learn how to define and use classes in Python to model real-world objects and behaviors.

## 🎯 目标

学习如何在 Python 中定义和使用类，以对现实世界中的对象和行为进行建模。

## 📝 Tasks / 任务

### 🛠️ Define a Simple Class / 定义简单类

#### Description
Create a class named `Car` that represents a car with attributes for make, model, and year. Add a method to display information about the car.

#### 描述
创建一个名为 `Car` 的类，表示一辆具有品牌、型号和年份属性的汽车，并添加一个显示汽车信息的方法。

#### Requirements
Completed program should:

- Define a class `Car` with `make`, `model`, and `year` attributes
- Include a method `display_info()` that prints the car's details
- Create an instance of `Car` and call `display_info()`

#### 要求
完成的程序应满足：

- 定义一个具有 `make`、`model` 和 `year` 属性的 `Car` 类
- 包含一个打印汽车详情的 `display_info()` 方法
- 创建一个 `Car` 实例并调用 `display_info()`


### 🛠️ Add Methods and Interactions / 添加方法与交互

#### Description
Expand the `Car` class to include a method to update the car's mileage and another to display the current mileage.

#### 描述
扩展 `Car` 类，添加一个更新里程的方法和一个显示当前里程的方法。

#### Requirements
Completed program should:

- Add a `mileage` attribute to the `Car` class (default 0)
- Add a method `update_mileage(new_mileage)` to update the mileage
- Add a method `display_mileage()` to print the current mileage
- Demonstrate updating and displaying mileage for a `Car` instance

#### 要求
完成的程序应满足：

- 向 `Car` 类添加 `mileage` 属性（默认值为 0）
- 添加 `update_mileage(new_mileage)` 方法用于更新里程
- 添加 `display_mileage()` 方法用于打印当前里程
- 演示对 `Car` 实例进行里程更新和显示

## 🚀 Advanced Challenges / 进阶挑战

> 完成以上任务后，尝试以下进阶挑战来加深理解！

1. **Inheritance / 继承**：Create a subclass `ElectricCar` that inherits from `Car` and adds a `battery_size` attribute and a `describe_battery()` method. / 创建一个继承自 `Car` 的子类 `ElectricCar`，添加 `battery_size` 属性和 `describe_battery()` 方法。

2. **Validation / 数据验证**：Add validation to `update_mileage()` so that mileage cannot be set to a lower value than the current mileage (odometer rollback protection). / 为 `update_mileage()` 添加验证，使里程不能被设置为低于当前里程的值（防止里程表回退）。

3. **Class Method & Static Method / 类方法与静态方法**：Add a class method `from_string(car_str)` that creates a `Car` instance from a string formatted as `"make-model-year"`. Also add a static method `is_valid_year(year)` that checks whether the year is between 1886 and the current year. / 添加类方法 `from_string(car_str)`，从 `"make-model-year"` 格式的字符串创建 `Car` 实例；添加静态方法 `is_valid_year(year)`，检查年份是否在 1886 到当前年之间。
