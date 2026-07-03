# 檔名
# 2026-06-17_06_backend_M_department_salary_growth.py
# Input
# employees = [
#     {"name": "Tom", "dept": "RD", "salary": 100, "last_salary": 80},
#     {"name": "Amy", "dept": "RD", "salary": 200, "last_salary": 180},
#     {"name": "John", "dept": "QA", "salary": 150, "last_salary": 100},
#     {"name": "Mary", "dept": "QA", "salary": 250, "last_salary": 200},
# ]
# Output
# [
#     {"dept": "RD", "total_growth": 40},
#     {"dept": "QA", "total_growth": 100},
# ]
# 題目類型 + 難度資訊
# 類型：
# Backend

# LeetCode 難度：
# Medium

# Artan 體感：
# Medium

# 練習重點：

# 1. dict aggregation
# 2. 商業邏輯轉換
# 3. 多欄位計算
# 4. 先算個人，再算部門
# 題目目標

# 公司想知道：

# 各部門本年度薪資成長總額

# 每位員工：

# salary
# =
# 今年薪資

# last_salary
# =
# 去年薪資

# 個人成長額：

# salary - last_salary

# 部門成長額：

# 所有員工成長額加總

# 例如：

# RD

# Tom:
# 100 - 80 = 20

# Amy:
# 200 - 180 = 20

# 總成長：

# 40

# 請回傳：

# {
#     "dept": 部門,
#     "total_growth": 成長總額
# }
# 完整可執行範本
from typing import *

employees = [
    {"name": "Tom", "dept": "RD", "salary": 100, "last_salary": 80},
    {"name": "Amy", "dept": "RD", "salary": 200, "last_salary": 180},
    {"name": "John", "dept": "QA", "salary": 150, "last_salary": 100},
    {"name": "Mary", "dept": "QA", "salary": 250, "last_salary": 200},
]

def department_salary_growth(
    employees: List[dict]
) -> List[dict]:
    # time : 22:36 ~ 22:41

    summary = {}
    for e in employees:
        dept, growth = e['dept'], e['salary'] - e['last_salary']
        summary[dept] = summary.get(dept, 0) + growth

    return [
        {'dept' : dept, 'growth' : growth}
        for dept, growth in summary.items()
    ]

print(department_salary_growth(employees))

# 這題我刻意出成：

# 不是直接加總 salary

# 而是：

# 先算差值
# 再聚合

# 看看你能不能很自然地把商業需求轉換成資料結構。

# 如果這題 5~8 分鐘內完成，而且沒有我剛剛那種隱藏 Bug，代表你的 Python Backend 基礎已經開始往 Medium 靠攏了。