# 檔名
# 2026-06-18_00_backend_M_department_top_employee.py
# Input
# employees = [
#     {"name": "Tom", "dept": "RD", "salary": 100},
#     {"name": "Amy", "dept": "RD", "salary": 250},
#     {"name": "John", "dept": "RD", "salary": 180},
#     {"name": "Mary", "dept": "QA", "salary": 220},
#     {"name": "Kevin", "dept": "QA", "salary": 150},
#     {"name": "Alice", "dept": "Sales", "salary": 500},
# ]
# Output
# [
#     {"dept": "RD", "name": "Amy", "salary": 250},
#     {"dept": "QA", "name": "Mary", "salary": 220},
#     {"dept": "Sales", "name": "Alice", "salary": 500},
# ]
# 題目類型 + 難度資訊
# 類型：
# Backend

# 難度：
# Medium

# LeetCode 體感：
# Easy+

# Artan 體感：
# Medium

# 練習重點：

# 1. dict 聚合
# 2. 狀態更新
# 3. 保留最佳解
# 4. DP 思維雛形
# 題目目標

# 公司想知道：

# 每個部門薪資最高的人

# 請回傳：

# {
#     "dept": 部門,
#     "name": 員工姓名,
#     "salary": 薪資
# }

# 例如：

# RD

# Tom   100
# Amy   250
# John  180

# 結果：

# {
#     "dept": "RD",
#     "name": "Amy",
#     "salary": 250
# }
# 限制

# 不要先：

# group by
# ↓
# sort

# 試著一路掃描完成。

# 也就是：

# for e in employees:

# 過程中就決定：

# 目前冠軍是誰
# 完整範本
from typing import *

employees = [
    {"name": "Tom", "dept": "RD", "salary": 100},
    {"name": "Amy", "dept": "RD", "salary": 250},
    {"name": "John", "dept": "RD", "salary": 180},
    {"name": "Mary", "dept": "QA", "salary": 220},
    {"name": "Kevin", "dept": "QA", "salary": 150},
    {"name": "Alice", "dept": "Sales", "salary": 500},
]

def department_top_employee(
    employees: List[dict]
) -> List[dict]:
    # time : 11:01~11:03
    
    findmax = {}
    for e in employees:
        dept, name, salary = e['dept'], e['name'], e['salary']
        findmax.setdefault(dept, {'name' : '', 'salary' : float('-inf')})
        if salary > findmax[dept]['salary']:
            findmax[dept] = {'name' : name, 'salary' : salary}
    
    return [
        {'dept' : dept, **info}
        for dept, info in findmax.items()
    ]

    


print(department_top_employee(employees))

# 這題我故意選它當今天第一題。

# 因為它其實跟你昨天的 DP 有一個共同點：

# 保留目前最佳解

# 只是：

# DP 保留的是：

# 最佳狀態

# 而這題保留的是：

# 最佳員工

# 你寫完後，我們再決定第二題要走：

# Sliding Window（續）

# 還是：

# 真正 Medium DP

# 看你的狀態。