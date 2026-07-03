# 1. 檔名
# 2026-06-11_04_department_unique_employee_count.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Mary"},

#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "Amy"},

#     {"dept": "HR", "name": "David"},
# ]
# 3. Output
# [
#     {
#         "dept": "RD",
#         "unique_employee_count": 2
#     },
#     {
#         "dept": "QA",
#         "unique_employee_count": 2
#     },
#     {
#         "dept": "HR",
#         "unique_employee_count": 1
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Set, Unique Count
# 練習重點
# 1. Group By
# 2. Set
# 3. 去重複
# 4. Dict[Set]
# 5. Dict -> List[Dict]
# 5. 題目要求
# 統計每個部門有幾位不同的員工

# 注意：

# 同一個名字重複出現

# 只能計算一次

# 例如：

# RD:

# Tom
# Tom
# Mary

# 實際員工數量：

# 2

# (Tom、Mary)
# 6. 完整可執行範本
from typing import List, Dict


def department_unique_employee_count(
    data: List[Dict]
) -> List[Dict]:
    # time : 10:28~10:30
    
    seen = {}
    for d in data:
        dept, name = d['dept'], d['name']
        seen.setdefault(dept, set())
        seen[dept].add(name)
    
    return [
        {'dept' : dept, 'unique_employee_count' : len(seen[dept])}
        for dept in seen
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},

        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "Amy"},

        {"dept": "HR", "name": "David"},
    ]

    print(
        department_unique_employee_count(
            data
        )
    )

# 這題我故意不要求排序。

# 我要看的是你會不會自然想到：

# {
#     "RD": {"Tom", "Mary"},
#     "QA": {"Jack", "Amy"}
# }

# 這種：

# Dict[Set]

# 結構。

# 這是昨天我們提到但還沒大量練到的類型。

# 🐍 第 4 題開始。