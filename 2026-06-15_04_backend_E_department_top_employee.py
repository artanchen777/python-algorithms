# 1. 檔名
# 2026-06-15_04_backend_E_department_top_employee.py
# 2. Input
# employees = [
#     {"dept": "A", "name": "Tom", "salary": 100},
#     {"dept": "A", "name": "Mary", "salary": 300},
#     {"dept": "A", "name": "Jack", "salary": 200},
#     {"dept": "B", "name": "John", "salary": 500},
#     {"dept": "B", "name": "Amy", "salary": 400},
# ]
# 3. Output
# [
#     {"dept": "A", "name": "Mary", "salary": 300},
#     {"dept": "B", "name": "John", "salary": 500},
# ]
# 4. 題目資訊
# 類型：
# Backend

# LeetCode 難度：
# Easy

# 練習重點：

# 1. dict 保存最佳答案
# 2. 比大小
# 3. list[dict] 操作
# 4. 不使用 sorted
# 5. 單次遍歷
# 5. 題目描述

# 公司要製作年度表揚名單。

# 請找出：

# 每個部門薪資最高的員工

# 並輸出：

# [
#     {
#         "dept": 部門,
#         "name": 員工姓名,
#         "salary": 薪資
#     }
# ]

# 限制：

# 不能使用 sorted()

# 不能先 group 完再排序

# 希望只掃描一次資料
# 6. 完整可執行範本
from typing import *

# time : 

employees = [
    {"dept": "A", "name": "Tom", "salary": 100},
    {"dept": "A", "name": "Mary", "salary": 300},
    {"dept": "A", "name": "Jack", "salary": 200},
    {"dept": "B", "name": "John", "salary": 500},
    {"dept": "B", "name": "Amy", "salary": 400},
]


def department_top_employee(employees: List[dict]) -> List[dict]:
    find_max = {}
    for e in employees:
        dept, name, salary = e['dept'], e['name'], e['salary']
        find_max.setdefault(dept, {'name': '', 'salary': float('-inf')})
        if salary > find_max[dept]['salary']:
            find_max[dept] = {'name' : name, 'salary' : salary}
    return [
        {'dept': dept, **info}
        for dept, info in find_max.items()
    ]


print(department_top_employee(employees))

# 這題故意禁止：

# sorted(...)

# 因為你上次的：

# [:1][0]

# 其實是在排序後取第一名。

# 這次要練的是：

# 資料流經過時

# 即時維護冠軍

# 這種 Backend / Streaming 的思維。

# 這題做完，我們可以開始往你一直缺的：

# dict 裡面放 dict

# 推進了。這會是你從 Easy 真正跨到 Easy+ / Medium 前最重要的一步。