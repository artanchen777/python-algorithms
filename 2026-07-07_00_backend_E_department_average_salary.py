# 1. 檔名
# 2026-07-07_00_backend_E_department_average_salary.py
# 2. Input
# employees = [
#     ("RD", 80000),
#     ("RD", 90000),
#     ("QA", 60000),
#     ("QA", 70000),
#     ("HR", 50000)
# ]
# 3. Output
# {
#     "RD": 85000,
#     "QA": 65000,
#     "HR": 50000
# }
# 4. 題目類型 + 難度 + 練習重點

# Backend / Easy（LeetCode Easy，體感 Easy）

# 練習重點：

# dict
# get()
# 多次遍歷
# Backend 統計資料
# 5. 題目描述

# 公司希望查看各部門的平均薪資。

# 請根據員工資料，計算每個部門的平均薪資，最後回傳 dictionary。

# 6. 完整可執行範本
from typing import List

# time : 20:19~22:26


employees = [
    ("RD", 80000),
    ("RD", 90000),
    ("QA", 60000),
    ("QA", 70000),
    ("HR", 50000)
]


def department_average_salary(employees):
    summary = {}
    for dept, salary in employees:
        info = summary.setdefault(dept, {'count' : 0, 'salary' : 0})
        info['count'] += 1
        info['salary'] += salary
    
    return {
        dept: info['salary'] // info['count']
        for dept, info in summary.items()
    }

print(department_average_salary(employees))