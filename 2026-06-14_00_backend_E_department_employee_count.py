# 1. 檔名
# 2026-06-14_00_backend_E_department_employee_count.py
# 2. Input
# data = [
#     {"dept": "A", "name": "Tom"},
#     {"dept": "A", "name": "Tom"},
#     {"dept": "A", "name": "Mary"},
#     {"dept": "B", "name": "John"},
#     {"dept": "B", "name": "Amy"},
#     {"dept": "B", "name": "Amy"},
# ]
# 3. Output
# [
#     {"dept": "A", "employee_count": 2},
#     {"dept": "B", "employee_count": 2},
# ]
# 4. 難度資訊 + 練習重點
# 難度：E

# 練習重點：
# - dict
# - set
# - 去重複
# - list comprehension
# - sorted
# 5. 題目目標、要求、限制
# 請統計每個部門有幾位不同的員工。

# 同一位員工在同一部門可能出現多次，只能計算一次。

# 回傳格式為 list[dict]。

# 依 dept 升冪排序。

# 不可使用 pandas。
# 6. 完整可執行範本
from typing import List

data = [
    {"dept": "A", "name": "Tom"},
    {"dept": "A", "name": "Tom"},
    {"dept": "A", "name": "Mary"},
    {"dept": "B", "name": "John"},
    {"dept": "B", "name": "Amy"},
    {"dept": "B", "name": "Amy"},
]

def department_employee_count(data: List[dict]) -> List[dict]:
    # time : 09:24 ~ 09:28
    
    seen = {}
    for d in data:
        dept, name = d['dept'], d['name']
        seen.setdefault(dept, set())
        seen[dept].add(name)
    return [
        {'dept' : dept, 'employee_count' : len(seen[dept])}
        for dept in sorted(seen)
    ]

print(department_employee_count(data))