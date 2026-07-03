# 檔名
# 2026-06-19_03_leetcode_DP_M_department_bonus_plan.py
# Input
# bonus = [2, 7, 9, 3, 1]
# Output
# 12
# 題目類型 + 難度資訊
# 類型：
# Leetcode 特殊題型或演算法(DP)

# 難度：
# M

# 體感：
# M-

# 練習重點：

# 1. DP
# 2. State
# 3. Base Case
# 4. House Robber 類型
# 5. 熟悉 DP 骨架
# 題目目標、要求、限制

# 公司年底準備發放特別獎金。

# 各部門可獲得的獎金如下：

# [2, 7, 9, 3, 1]

# 但為了避免資源衝突。

# 如果某部門領取獎金：

# 左右相鄰部門不能同時領取

# 請計算：

# 最高可以發出多少獎金

# 例如：

# 2 + 9 + 1

# 得到：

# 12
# 完整可執行範本
from typing import *

bonus = [2, 7, 9, 3, 1]

def department_bonus_plan(
    bonus: List[int]
) -> int:
    # time : : 11:50 ~ 11:53
    
    dp = [0] * len(bonus) # 定義 dp 為目前為止最高的總領獎
    
    dp[0] = bonus[0]
    dp[1] = max(bonus[1], dp[0])

    for i in range(2, len(bonus)):
        dp[i] = max(
            dp[i-1],
            dp[i-2] + bonus[i]
        )
        
    return dp[-1]

print(
    department_bonus_plan(
        bonus
    )
)