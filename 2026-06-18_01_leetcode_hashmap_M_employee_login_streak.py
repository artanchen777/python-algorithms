# 檔名
# 2026-06-18_02_leetcode_hashmap_M_employee_login_streak.py
# Input
# logs = [
#     "Tom",
#     "Amy",
#     "Tom",
#     "Tom",
#     "Amy",
#     "Amy",
#     "Amy",
#     "John",
# ]
# Output
# {
#     "name": "Amy",
#     "streak": 3
# }
# 題目類型 + 難度資訊
# 類型：
# Leetcode

# 主題：
# HashMap / State

# 難度：
# M

# 練習重點：

# 1. 狀態維護
# 2. 連續區間
# 3. 最大值更新
# 4. 不使用 Counter
# 題目目標

# 找出：

# 連續出現次數最多的員工
# 完整可執行範本
from typing import *

logs = [
    "Tom",
    "Amy",
    "Tom",
    "Tom",
    "Amy",
    "Amy",
    "Amy",
    "John",
]

def employee_login_streak(
    logs: List[str]
) -> dict:
    # time : 11:08 ~ 11:21 failed

    current_name = ''
    count = 0
    max_count, max_name = float('-inf'), ''
    
    for i in range(0, len(logs)):
        if i == 0:
            current_name = logs[0]
            count += 1
        else:
            if logs[i] == logs[i-1]:
                count += 1
            else:
                current_name = logs[i]
                count = 1
            
        if count > max_count:
            max_count = count
            max_name = current_name
    
    return {'name' : max_name, 'streak' : max_count}
    


print(employee_login_streak(logs))