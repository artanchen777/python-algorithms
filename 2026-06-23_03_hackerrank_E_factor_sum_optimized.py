# 檔名
# 2026-06-23_03_hackerrank_E_factor_sum_optimized.py
# Input
# nums = [6, 10, 15]
# Output
# [12, 18, 24]

# 說明：

# 6  的因數：1,2,3,6
# 總和：12

# 10 的因數：1,2,5,10
# 總和：18

# 15 的因數：1,3,5,15
# 總和：24
# 題目類型 + 難度 + 練習重點
# 類型：HackerRank / Math / Optimization

# LeetCode難度：Easy

# 體感難度：Medium

# 練習重點：

# 1. 因數(Factor)概念
# 2. 效能優化思維
# 3. O(n) → O(√n)
# 4. 找出重複計算
# 5. 成對因數(pair factor)
# 題目描述

# 某資料平台每天需要分析大量數字。

# 請實作一個函式：

# factor_sum(nums)

# 對於 nums 中每個數字：

# 計算所有因數總和。

# 最後回傳結果陣列。

# 限制
# 1 <= nums[i] <= 1,000,000
# 完整可執行範本
from typing import List


def factor_sum(nums: List[int]) -> List[int]:
    # time:
    
    result = []
    
    for n in nums:
    
        total = 0
        for i in range(1, int(n ** 0.5) + 1): # 平方根就是 pair 的交會處
            if  n % i == 0:
                pair = n // i # 當 n 可被 i 整除，另一半就是用除的
                total += i
                
                if pair != i: # 完全平方根的 case
                    total += pair

        result.append(total)

    return result


nums = [6, 10, 15]

print(factor_sum(nums))
# 額外要求（這題關鍵）

# 今天先不要寫：

# for i in range(1, n+1)

# 因為這就是你 HackerRank Timeout 的版本。

# 想想看：

# 36

# 的因數：

# 1 × 36
# 2 × 18
# 3 × 12
# 4 × 9
# 6 × 6

# 你真的需要檢查：

# 7~35

# 嗎？

# 這題我希望你自己先推。

# 如果卡住，我再帶你進入：

# Pair Factor
# 平方根優化
# O(√n)

# 這個思維。