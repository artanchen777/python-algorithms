# 1. 檔名
# 2026-06-11_05_department_unique_employee_filter.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Mary"},

#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "Amy"},

#     {"dept": "HR", "name": "David"},

#     {"dept": "IT", "name": "Bob"},
#     {"dept": "IT", "name": "Kevin"},
#     {"dept": "IT", "name": "Lucy"},
# ]

# threshold = 2
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
#         "dept": "IT",
#         "unique_employee_count": 3
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Set, Unique Count, Filter
# 練習重點
# 1. Dict[Set]
# 2. Unique Count
# 3. Filter
# 4. Dict -> List[Dict]
# 5. Backend Report
# 5. 題目要求
# 統計每個部門有幾位不同的員工

# 只保留：

# unique_employee_count >= threshold

# threshold = 2

# RD:

# Tom
# Tom
# Mary

# => 2

# 保留

# QA:

# Jack
# Jack
# Amy

# => 2

# 保留

# HR:

# David

# => 1

# 不保留

# IT:

# Bob
# Kevin
# Lucy

# => 3

# 保留

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_unique_employee_filter(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    # time : 10:32~10:34
    
    seen = {}
    for d in data:
        dept, name = d['dept'], d['name']
        seen.setdefault(dept, set())
        seen[dept].add(name)
    
    return [
        {'dept' : dept, 'unique_employee_count' : len(seen[dept])}
        for dept in seen
        if len(seen[dept]) >= threshold
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

        {"dept": "IT", "name": "Bob"},
        {"dept": "IT", "name": "Kevin"},
        {"dept": "IT", "name": "Lucy"},
    ]

    print(
        department_unique_employee_filter(
            data,
            2
        )
    )

# 這題是剛剛那題的自然延伸：

# Group By
# ↓
# Set 去重
# ↓
# Unique Count
# ↓
# Filter

# 如果你 2 分鐘內寫完，我下一題就開始把：

# Dict[Dict]
# +
# Dict[Set]

# 混在一起。🐍