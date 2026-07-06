
# 題目 01
# 1. 檔名
# 2026-07-06_01_backend_E_find_duplicate_email.py
# 2. Input
# emails = [
#     "a@test.com",
#     "b@test.com",
#     "c@test.com",
#     "a@test.com",
#     "d@test.com",
# ]
# 3. Output
# "a@test.com"

# 若沒有重複：

# None
# 4. 題目類型 + 難度 + 練習重點

# Backend / Hash Set

# LeetCode：Easy

# 體感難度：E+

# 練習重點：

# set
# in
# return
# Backend 去重
# 5. 題目目標、要求、限制

# 系統需要檢查 Email 是否重複。

# 請找出第一個重複出現的 Email。

# 限制：

# 不可排序
# 不可使用 Counter
# 時間複雜度希望 O(n)
# 6. 完整可執行範本
from datetime import datetime
from turtle import reset


emails = [
    "a@test.com",
    "b@test.com",
    "c@test.com",
    "a@test.com",
    "d@test.com",
]


def find_duplicate_email(emails):
    
    seen = set()
    for email in emails:
        if email in seen:
            return email
        else:
            seen.add(email)
    return None

print(find_duplicate_email(emails))

# time : 10:16 ~ 10:18