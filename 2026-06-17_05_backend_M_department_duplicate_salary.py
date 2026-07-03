# 檔名
# 2026-06-17_06_backend_M_department_duplicate_salary.py
# Input
# employees = [
#     {"name": "Tom", "dept": "RD", "salary": 100},
#     {"name": "Amy", "dept": "RD", "salary": 200},
#     {"name": "John", "dept": "RD", "salary": 100},
#     {"name": "Mary", "dept": "QA", "salary": 150},
#     {"name": "Kevin", "dept": "QA", "salary": 220},
#     {"name": "Alice", "dept": "QA", "salary": 150},
# ]
# Output
# [
#     {
#         "dept": "RD",
#         "duplicate_salaries": [100]
#     },
#     {
#         "dept": "QA",
#         "duplicate_salaries": [150]
#     }
# ]
# 題目類型 + 難度 + 練習重點
# 類型：
# Backend

# LeetCode 難度：
# Easy ~ Medium

# Artan 體感：
# Medium

# 練習重點：

# 1. dict of dict
# 2. 統計出現次數
# 3. list comprehension
# 4. 資料整理
# 5. 商業報表情境
# 題目描述

# 公司想檢查薪資資料是否有重複設定。

# 請找出：

# 每個部門中

# 出現超過一次的薪資

# 例如：

# RD

# 100
# 200
# 100

# 則：

# 100

# 出現兩次。

# 應列入結果。

# QA：

# 150
# 220
# 150

# 則：

# 150

# 應列入結果。

# 如果某部門沒有任何重複薪資：

# 不需要出現在結果中
# 完整可執行範本
from typing import *

employees = [
    {"name": "Tom", "dept": "RD", "salary": 100},
    {"name": "Amy", "dept": "RD", "salary": 200},
    {"name": "John", "dept": "RD", "salary": 100},
    {"name": "Mary", "dept": "QA", "salary": 150},
    {"name": "Kevin", "dept": "QA", "salary": 220},
    {"name": "Alice", "dept": "QA", "salary": 150},
]

def department_duplicate_salary(
    employees: List[dict]
) -> List[dict]:
    # time : 22:23 ~ 22:31

    found = {}
    for e in employees:
        dept, salary = e['dept'], e['salary']
        found.setdefault(
            dept, 
            {
                'seen' : set(), 
                'duplicate_salaries' : set() # 重複偵測到也能確保唯一
            }
        )
        if salary in found[dept]['seen']:
            found[dept]['duplicate_salaries'].add(salary)
        else:
            found[dept]['seen'].add(salary)
            
    return [
        {'dept' : dept, 'duplicate_salaries' : list(info['duplicate_salaries'])}
        for dept, info in found.items()
        if len(info['duplicate_salaries']) > 0 
    ]

print(department_duplicate_salary(employees))

# 這題我故意放在你最近能力圈的邊界。

# 不需要 DP。

# 不需要演算法技巧。

# 但需要你自己決定：

# 資料結構怎麼設計

# 這其實很接近 HackerRank 第二題常見的感覺。