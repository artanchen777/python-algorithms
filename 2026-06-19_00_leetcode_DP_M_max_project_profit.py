# 第一題（DP）
# 檔名
# 2026-06-19_00_leetcode_DP_M_max_project_profit.py
# Input
# profits = [5, 1, 10, 8, 6]
# Output
# 21
# 題目類型 + 難度資訊
# 類型：
# Leetcode 特殊題型或演算法(DP)

# 難度：
# M

# 體感：
# M

# 練習重點：

# 1. DP State 定義
# 2. DP Transition
# 3. House Robber 變形
# 4. 練習相信 dp[i-1]、dp[i-2]
# 題目目標

# 公司有一排專案：

# [5, 1, 10, 8, 6]

# 如果接下某個專案：

# 隔壁專案不能接

# 因為資源衝突。

# 請求出：

# 最大總獲利

# 例如：

# 5 + 10 + 6

# 得到：

# 21
# 完整範本
from typing import *

profits = [5, 1, 10, 8, 6]
profits = [100]

def max_project_profit(
    profits: List[int]
) -> int:
    # time : 10:28 ~ 10:32
    
    dp = [0] * len(profits)  # 定義 dp 為截至目前最大的總獲利

    for i, p in enumerate(profits):
        
        if i == 0:
            dp[0] = p
            continue
        
        if i == 1:
            dp[1] = max(dp[0], p)
            continue
            
        dp[i] = max(
            dp[i-1],
            dp[i-2] + p
        )
    
    return dp[-1]

print(
    max_project_profit(profits)
)