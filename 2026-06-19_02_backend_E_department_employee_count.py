# 檔名
# 2026-06-19_02_backend_E_department_employee_count.py
# Input
# employees = [
#     {"name": "Alice", "dept": "RD"},
#     {"name": "Bob", "dept": "RD"},
#     {"name": "Cindy", "dept": "QA"},
#     {"name": "David", "dept": "PM"},
#     {"name": "Eric", "dept": "QA"},
# ]
# Output
# [
#     {"dept": "RD", "count": 2},
#     {"dept": "QA", "count": 2},
#     {"dept": "PM", "count": 1},
# ]
# 題目類型 + 難度資訊
# 類型：
# Backend / HashMap

# 難度：
# E

# 體感：
# E

# 練習重點：

# 1. dict
# 2. get()
# 3. group by
# 4. list comprehension
# 題目目標

# 統計每個部門的人數。

# 完整可執行範本
from typing import *

employees = [
    {"name": "Alice", "dept": "RD"},
    {"name": "Bob", "dept": "RD"},
    {"name": "Cindy", "dept": "QA"},
    {"name": "David", "dept": "PM"},
    {"name": "Eric", "dept": "QA"},
]

def department_employee_count(
    employees: List[dict]
) -> List[dict]:
    # time : 11:44 ~ 11:46
    
    counter = {}
    for e in employees:
        dept = e['dept']
        counter[dept] = counter.get(dept, 0) + 1

    return [
        {'dept' : dept, 'count' : count}
        for dept, count in counter.items()
    ]


print(
    department_employee_count(
        employees
    )
)

# 這題我預估你：

# 3 分鐘內 AC

# 甚至可能直接秒殺。

# 做完之後。

# 下一題我會開始提高 M 的含金量。

# 不再是：

# 套模板就過

# 而會開始出：

# 看起來像 Backend 題
# 其實藏著 DP 或 Sliding Window 思維

# 這才是 HackerRank 最愛玩的套路。 😈