# 1. 檔名
# 2026-06-17_03_leetcode_E_employee_rest_schedule.py
# 2. Input
# workload = [4, 8, 5, 3]
# 3. Output
# 11
# 4. 題目資訊
# 類型：
# LeetCode

# LeetCode 難度：
# Easy

# Artan 體感難度：
# Medium

# 練習重點：

# 1. 自己定義 State
# 2. 自己推導 Transition
# 3. 驗證 House Robber 是否已內化
# 4. 練習先定義 State 再寫程式
# 5. 題目描述

# 公司安排員工輪流值班。

# 每天都有不同的工作量：

# workload = [4, 8, 5, 3]

# 為了避免過勞：

# 不能連續兩天值班

# 請計算：

# 最多可以承接多少工作量

# 例如：

# [4, 8, 5, 3]

# 最佳方案：

# 第2天 + 第4天

# 8 + 3

# 或

# 第1天 + 第3天

# 4 + 5

# 請自行判斷誰比較大。

# 6. 完整可執行範本
from typing import *

# time : 14:19~14:25

workload = [4, 8, 5, 3]

def max_workload(workload: List[int]) -> int:
    dp = [0] * len(workload) # 定義 dp 為目前為止，最大的工作量
    
    for i in range(0, len(workload)):
        if i == 0:
            dp[0] = workload[0]
            continue
        elif i == 1:
            dp[1] = max(workload[1], dp[0])
            continue
        
        dp[i] = max(
            dp[i-1],
            dp[i-2] + workload[i]
        )
    print(dp)
    return dp[-1] # 最後的冠軍

print(max_workload(workload))

# 這題額外規定

# 先不要寫 code。

# 先回我兩句：

# Q1
# dp[i]

# 你想定義成什麼？

# Q2

# 如果今天要選：

# workload[i]

# 那麼你能接誰？

# 如果這兩句能自己回答出來，

# 我就知道你是真的開始掌握：

# State
# →
# Transition

# 而不是在背 House Robber 公式。