# 1. 檔名
# 2026-07-06_00_backend_E_department_employee_count.py
# 2. Input
# employees = [
#     ("RD", "Kevin"),
#     ("RD", "Amy"),
#     ("QA", "Tom"),
#     ("RD", "John"),
#     ("QA", "Mary"),
# ]
# 3. Output
# {
#     "RD": 3,
#     "QA": 2
# }
# 4. 題目類型 + 難度 + 練習重點

# Backend / Dictionary

# LeetCode：Easy

# 體感難度：E+

# 練習重點：

# dict 基本操作
# get()
# Key 是否存在
# Backend 常見統計
# 5. 題目目標、要求、限制

# 公司希望快速知道每個部門目前共有幾位員工。

# 請根據輸入資料，統計每個部門的人數。

# 限制：

# 不可使用 Counter
# 不可使用 defaultdict
# 時間複雜度希望 O(n)
# 6. 完整可執行範本
from datetime import datetime

employees = [
    ("RD", "Kevin"),
    ("RD", "Amy"),
    ("QA", "Tom"),
    ("RD", "John"),
    ("QA", "Mary"),
]


def department_employee_count(employees):
    
    counter = {}
    for employee in employees:
        dept, name = employee
        counter[dept] = counter.get(dept, 0) + 1
    
    return counter


print(department_employee_count(employees))

# time : 10:13 ~ 10:15
