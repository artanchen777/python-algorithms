# 檔名

# 2026-06-30_00_backend_E_department_salary_report.py

# Input
# employees = [
#     ("RD", "Alice", 50000),
#     ("HR", "Bob", 42000),
#     ("RD", "Cindy", 68000),
#     ("IT", "David", 73000),
#     ("HR", "Eva", 46000),
#     ("RD", "Frank", 62000),
# ]
# Output
# {
#     "RD": {
#         "count": 3,
#         "total_salary": 180000,
#         "average_salary": 60000
#     },
#     "HR": {
#         "count": 2,
#         "total_salary": 88000,
#         "average_salary": 44000
#     },
#     "IT": {
#         "count": 1,
#         "total_salary": 73000,
#         "average_salary": 73000
#     }
# }
# 題目類型
# 類型：Backend / Data Processing
# LeetCode 難度：Easy
# 體感難度：Easy
# 練習重點：
# dict
# setdefault
# dict 巢狀結構
# 第二次遍歷(dict.values())
# Python 可讀性
# 題目描述

# 公司希望每天產生各部門的薪資摘要。

# 請撰寫函式：

# def department_salary_report(employees):

# 回傳每個部門：

# 員工數量
# 薪資總和
# 平均薪資（整數即可）

# 請自行建立適合的資料結構。

# 限制
# 不可使用 pandas
# 可使用 dict
# 平均薪資請使用整數除法 (//)
# 完整範本
from typing import List, Tuple


def department_salary_report(
    employees: List[Tuple[str, str, int]]
):
    # time: 11:35~11:44
    res = {}
    for dept, _, salary in employees:
        res.setdefault(dept, {'count' : 0, 'total_salary' : 0})
        res[dept]['count'] += 1
        res[dept]['total_salary'] += salary
    
    for dept, info in res.items():
        info['average_salary'] = info['total_salary'] // info['count']

    return res





employees = [
    ("RD", "Alice", 50000),
    ("HR", "Bob", 42000),
    ("RD", "Cindy", 68000),
    ("IT", "David", 73000),
    ("HR", "Eva", 46000),
    ("RD", "Frank", 62000),
]

print(department_salary_report(employees))