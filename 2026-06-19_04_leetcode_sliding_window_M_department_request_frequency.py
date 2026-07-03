# 檔名
# 2026-06-19_04_leetcode_sliding_window_M_department_request_frequency.py
# Input
# requests = [
#     "RD",
#     "QA",
#     "RD",
#     "PM",
#     "RD",
#     "QA",
#     "RD"
# ]

# k = 2
# Output
# 4
# 題目類型 + 難度資訊
# 類型：
# Leetcode 特殊題型或演算法

# 主題：
# Sliding Window + HashMap

# 難度：
# M

# 體感：
# M

# 練習重點：

# 1. Sliding Window
# 2. HashMap Counter
# 3. Frequency
# 4. Window 合法性判斷
# 5. left / right
# 題目目標

# 公司系統記錄了部門請求：

# [
#     "RD",
#     "QA",
#     "RD",
#     "PM",
#     "RD",
#     "QA",
#     "RD"
# ]

# 請找出：

# 最長連續區間

# 使得：

# 任何部門出現次數都不能超過 k 次

# 例如：

# ["RD","QA","RD","PM"]

# 裡面：

# RD = 2
# QA = 1
# PM = 1

# 合法。

# 長度：

# 4

# 但：

# ["RD","QA","RD","PM","RD"]

# 裡面：

# RD = 3

# 超過：

# k = 2

# 不合法。

# 完整可執行範本
from typing import *

requests = [
    "RD",
    "QA",
    "RD",
    "PM",
    "RD",
    "QA",
    "RD"
]

k = 2

def department_request_frequency(
    requests: List[str],
    k: int
) -> int:
    # time : 11:58~12:06
    # time : 12:07~12:13
    left = 0
    right = 0
    max_len = 0
    counter = {}
    for right in range(0, len(requests)):
        dept = requests[right]
        counter[dept] = counter.get(dept, 0) + 1
        
        while counter[dept] > k:
            counter[requests[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
    


print(
    department_request_frequency(
        requests,
        k
    )
)

# 這題很有 HackerRank 味道。

# 因為：

# 不是求唯一
# 不是求總和

# 而是：

# Frequency Constraint

# 看看你能不能把昨天的：

# seen

# 升級成：

# counter

# 來維護合法視窗。 😈