# 2026-06-18_03_leetcode_sliding_window_M_longest_department_budget.py
# Input
# budgets = [100, 200, 150, 300, 250]
# limit = 600
# Output
# 3
# 題目類型 + 難度資訊
# 類型：
# Leetcode

# 主題：
# Sliding Window

# 難度：
# M

# 練習重點：

# 1. Sliding Window 第二型態
# 2. Window Sum
# 3. left/right
# 4. 不需要 set
# 題目目標

# 公司準備做部門年度活動。

# 每個部門都有預算需求：

# [100, 200, 150, 300, 250]

# 請找出：

# 連續部門中

# 總預算 <= limit

# 的最長長度

# 例如：

# [100, 200, 150]

# 總和：

# 450

# 合法。

# 但：

# [100, 200, 150, 300]

# 總和：

# 750

# 超過：

# 600

# 所以答案：

# 3
# 題目目標

# 回傳：

# int
# 完整範本
from typing import *

budgets = [100, 200, 150, 300, 250]
limit = 600

def longest_department_budget(
    budgets: List[int],
    limit: int
) -> int:
    # time : 01:11 ~ 01:19

    summary = 0
    max_len = 0
    left = 0
    right = 0
    
    for right in range(0, len(budgets)):
        budget = budgets[right]
        
        summary += budget
        if summary > limit:
            # 超過 limit ，結算最大長度
            max_len = max(max_len, right - left) # 因為先加了爆掉的，故最後長度要少算1個
            
            # 縮小視窗
            while summary > limit:
                summary -= budgets[left]
                left +=1
        else: # 避免最後一個元素也沒超過上限，故都要結算一次
            max_len = max(max_len, right - left + 1) # 因為沒爆掉，所以最右邊要算進去 (+1)
    return max_len

print('\n', 
    longest_department_budget(
        budgets,
        limit
    )
)

# 這題很重要。

# 因為你會發現：

# Sliding Window
# 不一定需要 set

# 昨天那題是在維護：

# 元素唯一性

# 這題是在維護：

# 區間總和

# 但骨架其實長一樣：

# while 不合法:
#     left += 1

# 如果你把這題 AC。

# 你就會開始發現：

# Sliding Window 不是模板

# 而是一種思考方式

# 了。