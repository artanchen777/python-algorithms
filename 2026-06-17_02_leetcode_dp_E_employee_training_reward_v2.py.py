# 1. 檔名
# 2026-06-17_02_leetcode_E_employee_training_reward_v2.py
# 2. Input
# reward = [5, 1, 10, 5]
# 3. Output
# 15
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
# 3. 驗證是否真的理解 House Robber
# 4. 不依賴題目名稱辨認 DP
# 5. 題目描述

# 公司安排員工參加培訓。

# 每一天都有不同的培訓價值：

# reward = [5, 1, 10, 5]

# 規則：

# 員工不能連續兩天參加培訓

# 請計算：

# 能取得的最大培訓價值總和

# 例如：

# [5,1,10,5]

# 最佳方案：

# 第1天
# 第3天

# 得到：

# 5 + 10 = 15
# 6. 完整可執行範本
from typing import *

# time : 11:18~11:25

reward = [5, 1, 10, 5]


def max_training_reward(reward: List[int]) -> int:
    
    # 定義 dp 為，至這天為止，最大的培訓價值
    dp = [0] * len(reward) 
    
    for i in range(0, len(reward)):
        if i == 0:
            dp[0] = reward[0]
            continue
        if i == 1:
            dp[1] = max(reward[1], dp[0])
            continue
        
        dp[i] = max(
            dp[i-1],
            dp[i-2] + reward[i]
        )

    return dp[-1]


print(max_training_reward(reward))

# 這題的要求

# 這次不要直接寫 code。

# 先在紙上回答：

# Q1

# 你要怎麼定義：

# dp[i]
# Q2

# 如果：

# dp[i]

# 是你定義的意思。

# 那：

# dp[i-1]

# 代表什麼？

# Q3

# 如果我要拿：

# reward[i]

# 那我能接誰？

# Q4

# 你能不能自己推導出：

# dp[i] = ?

# 注意。

# 這題其實就是：

# House Robber

# 換皮。

# 但我故意隔了一天才拿回來。

# 因為我要驗證的不是：

# 你記不記得公式

# 而是：

# 你能不能從 State 自己長出公式

# 如果你能自己長出來。

# 那今天中午吃飯前，我就正式把：

# DP Phase 0

# 打勾。 ✅