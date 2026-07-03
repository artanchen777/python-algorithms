# 檔名
# 2026-06-17_07_leetcode_hashmap_M_longest_unique_department.py
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
# 3
# 題目類型 + 難度資訊
# 類型：
# LeetCode

# 主題：
# HashMap / Sliding Window

# LeetCode 難度：
# Medium

# Artan 體感：
# Medium

# 練習重點：

# 1. HashMap
# 2. Set
# 3. Sliding Window
# 4. 狀態更新
# 5. 區間思維
# 題目目標、要求、限制

# 公司想分析一段時間內各部門的工作紀錄。

# 請找出：

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

# 最長區間為：

# [
#     "QA",
#     "PM",
#     "RD",
#     "Sales"
# ]

# 長度：

# 4

# 因此答案應該是：

# 4

# （注意，我上面故意修正了範例，請以題目描述推導。）

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
    # time : First. 22:45 ~ 22:55 failed
    # time : 2rd. 23:06 ~ 23:11 failed
    
    left = 0
    right = 0
    max_len = 0
    seen = []
    while right < len(departments):
        dept = departments[right]
        if dept in seen:
            while dept in seen[left:right] and left < right:
                left += 1
        seen.append(dept)
        right += 1
        max_len = max(max_len, len(seen[left:right]))
        print(seen[left:right])
        
    return max_len

print(longest_unique_department(departments))

# 這題有個重要目標。

# 你先不要急著想：

# Sliding Window

# 怎麼寫。

# 先回答自己：

# 如果我用最笨的方法

# 從每個位置開始往後掃

# 我要怎麼判斷重複？

# 你把這個想清楚。

# Sliding Window 幾乎就自己長出來了。

# 這題如果你能自己摸出：

# seen = set()

# 然後開始思考：

# 重複了怎麼辦？

# 那就已經開始進入真正 HackerRank Q2 的領域了。