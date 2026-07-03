# 1. 檔名
# 2026-06-15_00_leetcode_E_employee_training_reward.py
# 2. Input
# scores = [3, 2, 5, 10, 7]
# 3. Output
# 15
# 4. 題目類型 + 難度資訊 + 練習重點
# 類型：
# Dynamic Programming (Phase 0)

# LeetCode 難度：
# Easy~Medium 之間

# 體感難度：
# Medium

# 練習重點：

# 1. DP 最基礎狀態轉移
# 2. 今天答案依賴昨天答案
# 3. 不使用遞迴
# 4. 建立 dp 陣列思維
# 5. 學會把問題拆成小問題
# 5. 題目目標、要求、限制

# 某公司要發放員工培訓獎勵。

# 每位員工都有一個分數：

# scores = [3, 2, 5, 10, 7]

# 公司規定：

# 如果今天選了某位員工領獎，

# 那麼左右相鄰的員工都不能領獎。

# 避免培訓資源衝突。

# 請計算：

# 最多可以領到多少總分

# 範例：

# 選 3 + 5 + 7 = 15

# 比：

# 2 + 10 = 12

# 更好。

# 所以答案：

# 15

# 限制：

# 不能修改原始陣列

# 時間複雜度希望 O(n)

# 先不要使用遞迴
# 6. 完整可執行範本
from typing import List


scores = [3, 2, 5, 10, 7]

def max_training_reward(scores: List[int]) -> int:
    # time : 06:43 ~ 18:46
    dp = [0] * len(scores)
    for i, s in enumerate(scores):
        if i == 0:
            dp[i] = s
        elif i == 1:
            dp[i] = max(dp[i-1], s) # tip: dp[-1] 並不會出錯，代表最後一個元素
        else:
            dp[i] = max(
                dp[i-1],
                dp[i-2] + s
            )

    return dp[-1] # 最後一個就是截至目前最好的答案

print('\n-' * 10)
print(max_training_reward(scores))

# 這題有一個很重要的特徵。

# 先不要急著想 DP。

# 先拿紙寫：

# index=0
# 答案是多少

# index=1
# 答案是多少

# index=2
# 答案是多少

# index=3
# 答案是多少

# 你會發現：

# dp[3]
# 其實會依賴
# dp[2]
# 和
# dp[1]

# 這就是 DP 的起點。

# 這題做完後，我會帶你總結：

# 什麼是 DP

# 為什麼這題是 DP

# DP 跟遞迴差在哪

# DP 跟你熟悉的 ETL / Backend 思維有什麼對應關係

# 不要查資料。

# 先用你現在的工程師直覺解一次。