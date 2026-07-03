# 1. 檔名
# 2026-06-15_03_backend_E_department_bonus_summary.py
# 2. Input
# employees = [
#     {"dept": "A", "name": "Tom", "bonus": 100},
#     {"dept": "A", "name": "Mary", "bonus": 200},
#     {"dept": "B", "name": "John", "bonus": 300},
#     {"dept": "C", "name": "Amy", "bonus": 150},
#     {"dept": "C", "name": "Bob", "bonus": 100},
# ]
# 3. Output
# [
#     {"dept": "A", "total_bonus": 300},
#     {"dept": "B", "total_bonus": 300},
#     {"dept": "C", "total_bonus": 250},
# ]
# 4. 題目資訊
# 類型：
# Backend

# LeetCode 難度：
# Easy

# Artan 體感難度：
# Easy ~ Easy+

# 練習重點：

# 1. dict 聚合
# 2. get()
# 3. items()
# 4. list[dict] 輸出
# 5. 將聚合結果轉回指定格式
# 5. 題目目標、要求、限制

# 公司年底要統計各部門的獎金總額。

# 每筆資料代表一位員工實際領到的獎金。

# 請計算：

# 每個部門總共發出了多少獎金

# 並回傳：

# [
#     {"dept": 部門名稱, "total_bonus": 總獎金}
# ]

# 要求：

# 1. 保留所有部門
# 2. 不需要排序
# 3. 不可使用 pandas
# 4. 使用 Python 原生資料結構完成
# 6. 完整可執行範本
from typing import *

# time : 00:18~00:21

employees = [
    {"dept": "A", "name": "Tom", "bonus": 100},
    {"dept": "A", "name": "Mary", "bonus": 200},
    {"dept": "B", "name": "John", "bonus": 300},
    {"dept": "C", "name": "Amy", "bonus": 150},
    {"dept": "C", "name": "Bob", "bonus": 100},
]


def department_bonus_summary(employees: List[dict]) -> List[dict]:
    total = {}
    for e in employees:
        dept, bonus = e['dept'], e['bonus']
        total[dept] = total.get(dept, 0) + bonus
        
    return [
        {'dept' : dept, 'total_bonus' : total_bonus}
        for dept, total_bonus in total.items()
    ]


print(department_bonus_summary(employees))

# 這題是故意讓你從 DP 的高腦力模式切回：

# dict
# aggregation
# backend data processing

# 讓大腦收個尾。

# 而且這題跟你之前做過的：

# department_salary_summary
# department_employee_count
# department_qualified_salary

# 屬於同一脈絡。

# 今晚不用挑戰新觀念。

# 把手感維持住就好。