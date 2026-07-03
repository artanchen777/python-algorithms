# 1. 檔名
# 2026-06-10_backend_E_department_min_salary_filter.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]

# threshold = 150
# 3. Output
# [
#     {"dept": "QA", "min_salary": 200},
#     {"dept": "HR", "min_salary": 350},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Min, Filter
# 練習重點
# 1. float("inf")
# 2. Min
# 3. Group By
# 4. Filter
# 5. Aggregate
# 5. 題目要求
# 計算各部門最低薪資

# 只保留：

# min_salary > threshold

# threshold = 150

# RD:

# min = 100

# 不保留

# QA:

# min = 200

# 保留

# HR:

# min = 350

# 保留

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_min_salary_filter(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, float('inf'))
        if salary < summary[dept]:
            summary[dept] = salary
            
    return [
        {'dept' : dept, 'min_salary' : salary}
        for dept, salary in summary.items()
        if salary > threshold
    ]

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(
        department_min_salary_filter(
            data,
            150
        )
    )

# 這題其實是白天那題：

# find_max[dept] = max(...)

# 的鏡像版。

# 看看你會不會自然想到：

# float("inf")

# 而不是：

# 999999999

# 😆

# 第 13 題，開始。🐍