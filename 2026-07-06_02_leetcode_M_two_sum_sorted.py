
# 題目 02
# 1. 檔名
# 2026-07-06_02_leetcode_M_two_sum_sorted.py
# 2. Input
# nums = [1, 3, 5, 8, 10, 12]

# target = 13
# 3. Output
# (1, 4)

# 或

# [1, 4]

# 皆可。

# 4. 題目類型 + 難度 + 練習重點

# LeetCode / Two Pointer

# LeetCode：Medium

# 體感難度：E+ ~ M

# 練習重點：

# Two Pointer
# 左右夾擊
# 排序陣列
# O(n)
# 5. 題目目標、要求、限制

# 已知陣列一定已排序。

# 請找出兩個數字相加等於 target 的索引。

# 限制：

# 不可使用 HashMap
# 不可使用雙層迴圈
# 必須使用 Two Pointer
# 6. 完整可執行範本
from datetime import datetime


nums = [1, 3, 5, 8, 10, 12]

target = 13


def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total > target:
            right -= 1
        else:
            #case : total < target:
            left += 1
    return None

print(two_sum_sorted(nums, target))

# time : 10:18~10:22