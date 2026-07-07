# 1. 檔名
# 2026-07-07_02_backend_M_merge_user_scores.py
# 2. Input
# scores = [
#     ("Tom", 30),
#     ("John", 20),
#     ("Tom", 50),
#     ("Mary", 60),
#     ("John", 40),
# ]
# 3. Output
# [
#     ("Tom", 80),
#     ("John", 60),
#     ("Mary", 60),
# ]
# 4. 題目類型 + 難度 + 練習重點

# Backend / Medium（LeetCode Easy+，體感 Medium）

# 練習重點：

# dict
# list
# Backend Aggregation
# SQL GROUP BY 思維
# 保持第一次出現順序
# 5. 題目描述

# 系統收到許多使用者的分數紀錄。

# 同一位使用者可能會出現很多次。

# 請將同一位使用者的分數加總，並保持第一次出現的順序。

# 6. 完整可執行範本
from typing import List

scores = [
    ("Tom", 30),
    ("John", 20),
    ("Tom", 50),
    ("Mary", 60),
    ("John", 40),
]


def merge_user_scores(scores):
    # time : 20:39~20:47
    summary = {}
    order_map = {}
    order_id = 0
    for user, score in scores:
        
        summary[user] = summary.get(user, 0) + score
        if user not in order_map:
            order_map[user] = order_id
            order_id += 1
    # Python 3.7 之後, dict 天然就保證插入順序。
    return list(summary.items())
    
print(merge_user_scores(scores))