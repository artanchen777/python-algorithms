# 1. 檔名
# 2026-06-17_00_leetcode_E_climbing_stairs.py
# 2. Input
# n = 5
# 3. Output
# 8
# 4. 題目資訊
# 類型：
# LeetCode

# LeetCode 難度：
# Easy

# Artan 體感難度：
# Easy+ ~ Medium-

# 練習重點：

# 1. DP State
# 2. State Transition
# 3. 理解為什麼只看前兩步
# 4. 驗證 DP 不一定是 Max
# 5. 題目目標、要求、限制

# 公司大樓有一個樓梯。

# 你每次可以：

# 走 1 階

# 或

# 走 2 階

# 請計算：

# 共有多少種方式

# 可以走到第 n 階

# 例如：

# n = 3

# 方法有：

# 1+1+1

# 1+2

# 2+1

# 共：

# 3 種
# 6. 完整可執行範本
from typing import *

# time :

n = 5

def climbing_stairs(n: int) -> int:
    dp = [0] * n
    
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        print(i)
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]


print('\n', climbing_stairs(n))
# 額外要求（今天最重要）

# 不要急著寫 code。

# 先回答這兩個問題：

# Q1

# 你認為：

# dp[i]

# 應該代表什麼？

# Q2

# 如果我要到：

# 第 5 階

# 最後一步只能是：

# 從第 4 階跨 1 步

# 或

# 從第 3 階跨 2 步

# 那：

# dp[5]

# 和：

# dp[4]
# dp[3]

# 有什麼關係？

# 這題是故意選的。

# 因為：

# 沒有 Max
# 沒有最佳解
# 沒有冠軍

# 如果你還能自己推導出：

# dp[i]

# 那代表你真的理解 DP 了。

# 而不是只理解 House Robber。