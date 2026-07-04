# 檔名
# 2026-07-04_00_backend_E_find_duplicate_orders.py
# Input
# orders = [
#     "A001",
#     "A002",
#     "A003",
#     "A002",
#     "A005",
#     "A001"
# ]
# Output
# ["A002", "A001"]
# 題目類型

# Backend / Hash Set

# LeetCode：Easy

# 體感：Easy

# 練習重點

# set
# in
# append
# 保持第一次重複出現順序
# 題目

# 商城收到大量訂單。

# 請找出：

# 有哪些訂單編號重複出現。

# 每個重複訂單只輸出一次。

# 範本
from typing import List

# time :

# Time Complexity:
# O(n)

# Space Complexity:
# O(n)

# Why:
# duplicated set 用來避免 list 線性搜尋。

def find_duplicate_orders(orders: List[str]) -> List[str]:
    seen = set()
    duplicated  = set() # Track reported duplicates for O(1) lookup
    result = []
    for order in orders:
        if order in seen: 
            if order not in duplicated :
                duplicated.add(order) # Avoid duplicate results
                result.append(order) # Preserve first duplicate occurrence order
        else:
            seen.add(order)
    return result


orders = [
    "A001",
    "A002",
    "A003",
    "A002",
    "A005",
    "A001"
]

print(find_duplicate_orders(orders))