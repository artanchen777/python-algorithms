# 檔名
# 2026-07-04_02_backend_E_filter_active_users.py
# Input
# users = [
#     {"name": "Tom", "active": True},
#     {"name": "Amy", "active": False},
#     {"name": "John", "active": True},
# ]
# Output
# [
#     {"name": "Tom", "active": True},
#     {"name": "John", "active": True},
# ]
# 題目類型

# Backend

# LeetCode：Easy

# 體感：Easy

# 練習重點

# list
# dict
# append
# 條件判斷
# 範本
from typing import List

# time :


def filter_active_users(users: List[dict]) -> List[dict]:
    return [u for u in users if u['active']]
        


users = [
    {"name": "Tom", "active": True},
    {"name": "Amy", "active": False},
    {"name": "John", "active": True},
]

print(filter_active_users(users))