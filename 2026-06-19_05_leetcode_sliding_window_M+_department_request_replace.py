# 檔名
# 2026-06-19_05_leetcode_sliding_window_M+_department_request_replace.py
# Input
# requests = [
#     "RD",
#     "QA",
#     "RD",
#     "PM",
#     "RD"
# ]

# k = 1
# Output
# 4
# 題目類型 + 難度資訊
# 類型：
# Leetcode

# 主題：
# Sliding Window + HashMap

# 難度：
# M+

# 體感：
# M+

# 練習重點：

# 1. Frequency Counter
# 2. Sliding Window
# 3. Max Frequency
# 4. Window 合法條件
# 5. 題目轉譯能力
# 題目目標

# 公司記錄了一段請求：

# [
#     "RD",
#     "QA",
#     "RD",
#     "PM",
#     "RD"
# ]

# 你有：

# k = 1

# 次機會。

# 意思是：

# 最多允許修改 1 筆請求

# 讓它變成任何部門。

# 請求出：

# 最長連續區間

# 使得經過最多一次修改後：

# 整個區間都能變成同一個部門

# 例如：

# [
#     "RD",
#     "QA",
#     "RD"
# ]

# 把：

# "QA"

# 改成：

# "RD"

# 得到：

# [
#     "RD",
#     "RD",
#     "RD"
# ]

# 合法。

# 長度：

# 3
# 完整範本
from typing import *

requests = [
    "RD",
    "QA",
    "RD",
    "PM",
    "RD"
]

k = 1

def department_request_replace(
    requests: List[str],
    k: int
) -> int:
    # time : 10:54~11:00

    pass


print(
    department_request_replace(
        requests,
        k
    )
)

# 這題有點像你今天下午那題：

# Frequency Window

# 但合法條件換了。

# 我故意不給提示。

# 看看你能不能先自己定義：

# 什麼叫合法視窗？

# 這是今天最後一題的價值所在。

# 等寶寶洗澡、大家輪流洗完，你應該剛好有 10~15 分鐘可以跟它打一架。😈