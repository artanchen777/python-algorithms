# 1. 檔名
# 2026-06-17_01_leetcode_E_min_cost_climbing_stairs.py
# 2. Input
# cost = [10, 15, 20]
# 3. Output
# 15
# 4. 題目資訊
# 類型：
# LeetCode

# LeetCode 難度：
# Easy

# Artan 體感難度：
# Medium-

# 練習重點：

# 1. DP State 定義
# 2. DP 不一定是最大值
# 3. DP 不一定是方法數
# 4. 理解狀態如何被重複利用
# 5. 題目目標、要求、限制

# 公司有一個樓梯。

# 每一階都有一個體力消耗：

# cost = [10, 15, 20]

# 意思：

# 踩到第0階要花10體力

# 踩到第1階要花15體力

# 踩到第2階要花20體力

# 你每次可以：

# 走1階

# 或

# 走2階

# 請問：

# 到達樓梯頂端

# 最少需要花多少體力？

# 例如：

# cost = [10, 15, 20]

# 最佳路線：

# 直接從第1階開始

# 花15

# 跳到頂樓

# 答案：

# 15
# 6. 完整可執行範本
from typing import *

# time : 10:29~10:35

cost = [10, 15, 20]


def min_cost_climbing_stairs(cost: List[int]) -> int:
    length = len(cost)

    # 定義 dp 為，到底此階的最小總花費
    dp = [0] * length 
    dp[0] = 10
    dp[1] = 15
    
    for i in range(2, length):
        dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
    return min(dp[length - 1], dp[length - 2])

print('\n' * 3)
print(min_cost_climbing_stairs(cost))