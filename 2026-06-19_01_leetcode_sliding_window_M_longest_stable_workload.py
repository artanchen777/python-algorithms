# 檔名
# 2026-06-19_01_leetcode_sliding_window_M_longest_stable_workload.py
# Input
# workloads = [2, 1, 3, 2, 4, 1]
# limit = 7
# Output
# 3
# 題目類型 + 難度資訊
# 類型：
# Leetcode 特殊題型或演算法(Sliding Window)

# 難度：
# M

# 體感：
# M

# 練習重點：

# 1. Sliding Window
# 2. Window Sum
# 3. 合法區間維護
# 4. left / right
# 5. max_len
# 6. while
# 題目目標

# 有一串工作負載：

# [2, 1, 3, 2, 4, 1]

# 如果連續安排太多工作。

# 團隊會超載。

# 請找出：

# 總工作量 <= limit

# 的最長連續區間長度。

# 例如：

# [2, 1, 3]

# 總和：

# 6

# 合法。

# 例如：

# [2, 1, 3, 2]

# 總和：

# 8

# 超過：

# 7

# 不合法。

# 其中一組最長合法區間：

# [1, 3, 2]

# 長度：

# 3

# 答案是：

# 3

# （請自己驗證是哪個區間）

# 完整可執行範本
from typing import *

workloads = [2, 1, 3, 2, 4, 1]
limit = 7

def longest_stable_workload(
    workloads: List[int],
    limit: int
) -> int:
    # time : 11:25 ~ 11:33
    left = 0
    right = 0
    max_len = 0
    summary = 0
    for right in range(0, len(workloads)):
        summary += workloads[right]
    
        # 超過就結算
        while summary > limit:
            summary -= workloads[left]
            left += 1
        
        # 結算當前合法區間長度並更新最大值
        max_len = max(max_len, right- left + 1)
        print(summary,',', max_len)

    return max_len


print('\n',
    longest_stable_workload(
        workloads,
        limit
    )
)

# 這題我故意不給額外提示。

# 因為它和你昨晚的：

# 2026-06-18_03_leetcode_sliding_window_M_longest_department_budget.py

# 有 95% 相似。

# 我想看看你能不能：

# 看出題目本質
# 而不是記住題目內容

# 這是從「會寫」走向「會抽象化」的重要一步。