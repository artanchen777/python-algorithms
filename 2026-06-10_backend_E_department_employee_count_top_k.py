# 1. 檔名
# 2026-06-10_backend_E_department_employee_count_top_k.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Mary"},
#     {"dept": "RD", "name": "Andy"},

#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "John"},

#     {"dept": "HR", "name": "David"},
#     {"dept": "HR", "name": "Amy"},
#     {"dept": "HR", "name": "Bob"},
#     {"dept": "HR", "name": "Kevin"},
# ]

# k = 2
# 3. Output
# [
#     {"dept": "HR", "count": 4},
#     {"dept": "RD", "count": 3},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Count, Sorting, Top K
# 練習重點
# 1. Group By
# 2. Count
# 3. List[Dict]
# 4. Multi Sort
# 5. Top K
# 5. 題目要求
# 計算各部門員工數量

# 依員工數由高到低排序

# 若員工數相同

# 依部門名稱排序

# 最後只保留前 k 名

# 例如：

# HR = 4

# RD = 3

# QA = 2

# 取前 2 名：

# HR
# RD


# ---

# ## 6. 完整可執行範本

# ```python
from typing import List, Dict


def department_employee_count_top_k(
    data: List[Dict],
    k: int
) -> List[Dict]:
    
    counter = {}
    for d in data:
        dept = d["dept"]
        counter[dept] = counter.get(dept, 0) + 1

    res = []
    for dept, count in counter.items():
        res.append({
            'dept' : dept,
            'count' : count
        })
    return sorted(
        res,
        key = lambda item: (-item['count'], item['dept'])
    )[:k]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "RD", "name": "Andy"},

        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "John"},

        {"dept": "HR", "name": "David"},
        {"dept": "HR", "name": "Amy"},
        {"dept": "HR", "name": "Bob"},
        {"dept": "HR", "name": "Kevin"},
    ]

    print(
        department_employee_count_top_k(
            data,
            2
        )
    )

# 這題其實是把你昨天練過的：

# department_employee_count_ranking()

# 再加上：

# [:k]

# 而已。

# 但我要觀察的是，你會不會自然形成：

# count
# ↓
# list
# ↓
# sorted
# ↓
# top k

# 這個資料流。

# 時間：

# 2026-06-10 11:39

# 預估 3~5 分鐘。🐍