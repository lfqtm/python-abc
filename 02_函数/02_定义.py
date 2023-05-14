# -*- coding: utf-8 -*-
"""
    定义语法
"""

def say_hi():
    print("hello func")

# 带形式参数的函数定义
def add(x, y):
    result = x + y
    print(f"{x} + {y} = {x+y}")

# 实参传递
add(1, 3)

# None类型
result = say_hi()
print(type(result))

# 全局变量的使用
num = 100

# 全局变量在函数体中的使用
def test_global():
    global num
    num = 200
    print(f"num值为 {num}")

print(num)  
test_global()
print(num) # 值已修改