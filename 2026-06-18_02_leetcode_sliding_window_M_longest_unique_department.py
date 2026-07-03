# 檔名
# 2026-06-18_02_leetcode_sliding_window_M_longest_unique_department.py
# Input
# departments = [
#     "RD",
#     "QA",
#     "PM",
#     "RD",
#     "Sales",
#     "QA"
# ]
# Output
# 4
# 題目類型 + 難度資訊
# 類型：
# Leetcode

# 主題：
# Sliding Window

# 難度：
# M

# 體感：
# 目前對 Artan 屬於 M+

# 練習重點：

# 1. left / right
# 2. set
# 3. while
# 4. 維護合法區間
# 5. 第一題真正的 Sliding Window
# 題目描述

# 找出：

# 最長的一段連續區間

# 使得：

# 區間內所有部門都不重複

# 例如：

# [
#     "RD",
#     "QA",
#     "PM",
#     "RD",
#     "Sales",
#     "QA"
# ]

# 最長區間：

# [
#     "QA",
#     "PM",
#     "RD",
#     "Sales"
# ]

# 長度：

# 4
# 限制

# 禁止：

# seen[left:right]

# 禁止：

# departments[left:right]

# 禁止：

# 切片解法

# 必須使用：

# left
# right
# seen = set()
# 完整可執行範本
from typing import *

departments = [
    "RD",
    "QA",
    "PM",
    "RD",
    "Sales",
    "QA"
]

def longest_unique_department(
    departments: List[str]
) -> int:
    # time : 
    left = 0
    right = 0
    seen = set()
    max_len = 0
    
    for right in range(0, len(departments)):
        dept = departments[right]
        
        # 先建構核心判斷基底
        if dept not in seen:
            seen.add(dept)
        else:
            # 發現重複，故結算並將視窗左側縮小
            while dept in seen:
                seen.remove(departments[left])
                left += 1
            
            seen.add(dept) # 最後記得把這次新出現的重複部門補進去，做為此部門新的第一個基準點
        
        # 最後比較一下最大值
        max_len = max(max_len, right - left + 1)
        
    return max_len


print(longest_unique_department(departments))

# 額外提示（只給一句）：

# 昨天你最接近 AC 的時候其實已經摸到了。

# 真正的核心不是：

# seen.remove(dept)

# 而是：

# seen.remove(departments[left])

# 因為：

# 重複的是 right

# 要移走的是 left

# 這句話如果哪個瞬間突然想通了，Sliding Window 就開竅了。