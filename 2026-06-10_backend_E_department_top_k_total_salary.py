# 1. 檔名
# 2026-06-10_backend_E_department_top_k_total_salary.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},

#     {"dept": "IT", "salary": 1000},
# ]

# k = 2
# 3. Output
# [
#     {"dept": "IT", "total_salary": 1000},
#     {"dept": "RD", "total_salary": 900},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Sum, Sorting, Top K
# 練習重點
# 1. Group By
# 2. Sum
# 3. Dict -> List[Dict]
# 4. Sort
# 5. Top K
# 5. 題目要求
# 計算各部門薪資總和

# 依 total_salary 由高到低排序

# 只保留前 k 名

# 若 total_salary 相同

# 依 dept 名稱排序

# 例如：

# IT = 1000
# RD = 900
# QA = 600
# HR = 350

# 取前 2 名：

# IT
# RD
# 6. 完整可執行範本
from typing import List, Dict


def department_top_k_total_salary(
    data: List[Dict],
    k: int
) -> List[Dict]:
    
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    
    return [
        {'dept' : dept, 'total_salary' : salary}
        for dept, salary in sorted(
            total.items(),
            key = lambda item: (-item[1], item[0])
        )[:k]
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},

        {"dept": "IT", "salary": 1000},
    ]

    print(
        department_top_k_total_salary(
            data,
            2
        )
    )

# 這題其實是把你今天學過的：

# Group By
# +
# Sum
# +
# List[Dict]
# +
# Sort
# +
# Top K

# 全部串起來。

# 如果你秒想到：

# summary
# ↓
# res
# ↓
# sorted(...)
# ↓
# [:k]

# 那代表今天的東西開始沉澱了。