# 1. 檔名
# 2026-06-11_02_department_average_salary_filter_ranking.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 500},
#     {"dept": "RD", "salary": 300},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},

#     {"dept": "IT", "salary": 1000},
#     {"dept": "IT", "salary": 200},
# ]

# threshold = 320
# 3. Output
# [
#     {
#         "dept": "HR",
#         "avg_salary": 350
#     },
#     {
#         "dept": "IT",
#         "avg_salary": 600
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Average, Filter, Sorting
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Filter
# 4. Multi-stage Data Flow
# 5. Dict -> List[Dict]
# 5. 題目要求
# 計算每個部門平均薪資

# 只保留：

# avg_salary >= threshold

# 最後依 dept 名稱排序

# threshold = 320

# RD:

# (100 + 500 + 300) / 3

# = 300

# 不保留

# QA:

# (200 + 400) / 2

# = 300

# 不保留

# HR:

# 350

# 保留

# IT:

# (1000 + 200) / 2

# = 600

# 保留

# 輸出順序：

# HR
# IT
# 6. 完整可執行範本
from typing import List, Dict


def department_average_salary_filter_ranking(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    # time : 10:13~10:19
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, {'count' : 0, 'salary' : 0}) 
        summary[dept]['count'] += 1
        summary[dept]['salary'] += salary
        
    return [
        {'dept' : dept, 'avg_salary' : summary[dept]['salary'] / summary[dept]['count']}
        for dept in sorted(
            summary,
            key = lambda dept: dept
        )
        if summary[dept]['salary'] / summary[dept]['count'] >= threshold
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 500},
        {"dept": "RD", "salary": 300},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},

        {"dept": "IT", "salary": 1000},
        {"dept": "IT", "salary": 200},
    ]

    print(
        department_average_salary_filter_ranking(
            data,
            320
        )
    )

# 這題我想看的是你會不會自然形成：

# Group By
# ↓
# Average
# ↓
# Filter
# ↓
# Sort
# ↓
# Output

# 而不是做到一半就開始排序。

# 這是很多 Backend 報表需求的標準資料流。

# 🐍 第 2 題開始。