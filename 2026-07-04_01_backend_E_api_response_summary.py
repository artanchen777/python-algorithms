# 第二題
# 檔名
# 2026-07-04_01_backend_E_api_response_summary.py
# Input
# responses = [
#     {"status": 200},
#     {"status": 404},
#     {"status": 500},
#     {"status": 200},
#     {"status": 200},
# ]
# Output
# {
#     200: 3,
#     404: 1,
#     500: 1
# }
# 題目類型

# Backend

# LeetCode：Easy

# 體感：Easy

# 練習重點

# dict
# get()
# 累加統計
# 題目

# 統計 API Response Status Code 出現次數。

# 範本
from typing import List

# time :

def response_summary(responses: List[dict]) -> dict:
    counter = {}
    for r in responses:
        status = r['status']
        counter[status] = counter.get(status, 0) + 1
        
    return counter

responses = [
    {"status": 200},
    {"status": 404},
    {"status": 500},
    {"status": 200},
    {"status": 200},
]

print(response_summary(responses))