# 1. 檔名
# 2026-07-07_01_backend_E_remove_duplicate_users.py
# 2. Input
# users = [
#     ("Tom", "A"),
#     ("John", "B"),
#     ("Tom", "A"),
#     ("Mary", "C"),
#     ("John", "B"),
# ]
# 3. Output
# [
#     ("Tom", "A"),
#     ("John", "B"),
#     ("Mary", "C")
# ]
# 4. 題目類型 + 難度 + 練習重點

# Backend / Easy+（LeetCode Easy，體感 Easy+）

# 練習重點：

# set
# tuple
# Backend 去重
# 保持原順序
# 5. 題目描述

# 使用者資料有重複。

# 請保留第一次出現的資料。

# 6. 完整可執行範本
from typing import List

users = [
    ("Tom", "A"),
    ("John", "B"),
    ("Tom", "A"),
    ("Mary", "C"),
    ("John", "B"),
]


def remove_duplicate_users(users):
    # time : 20:28~20:29
    seen = set()
    res = []
    for user in users:
        if user not in seen:
            seen.add(user)
            res.append(user)
    return res
            
print(remove_duplicate_users(users))