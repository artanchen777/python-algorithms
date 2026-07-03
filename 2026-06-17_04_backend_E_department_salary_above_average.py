# 1. 檔名
# 2026-06-17_04_backend_E_department_salary_above_average.py
# 2. Input
# employees = [
#     {"name": "Tom", "dept": "RD", "salary": 100},
#     {"name": "Amy", "dept": "RD", "salary": 200},
#     {"name": "John", "dept": "QA", "salary": 150},
#     {"name": "Mary", "dept": "QA", "salary": 250},
# ]
# 3. Output
# [
#     {"name": "Amy", "dept": "RD", "salary": 200},
#     {"name": "Mary", "dept": "QA", "salary": 250},
# ]
# 4. 題目資訊
# 類型：
# Backend

# LeetCode 難度：
# Easy

# Artan 體感難度：
# Easy ~ Medium

# 練習重點：

# 1. dict 聚合
# 2. 平均值計算
# 3. 二次遍歷資料
# 4. Python 思維而非 DP
# 5. 題目描述

# 公司希望找出：

# 薪資高於自己部門平均薪資

# 的員工。

# 例如：

# RD 部門：

# 100
# 200

# 平均：

# 150

# 因此：

# Amy

# 符合條件。

# QA 部門：

# 150
# 250

# 平均：

# 200

# 因此：

# Mary

# 符合條件。

# 請回傳所有：

# 薪資高於所屬部門平均薪資

# 的員工。

# 6. 完整可執行範本
from typing import *

# time :

employees = [
    {"name": "Tom", "dept": "RD", "salary": 100},
    {"name": "Amy", "dept": "RD", "salary": 200},
    {"name": "John", "dept": "QA", "salary": 150},
    {"name": "Mary", "dept": "QA", "salary": 250},
]


def department_salary_above_average(
    employees: List[dict]
) -> List[dict]:
    # time : 
    info = {}
    for e in employees:
        dept, salary = e['dept'], e['salary']
        item = info.setdefault(dept, {'count' : 0, 'total' : 0})
        item['count'] +=1
        item['total'] += salary
    
    return [
        {'dept' : e['dept'], 'name' : e['name'], 'salary' : e['salary']}
        for e in employees
        if e['salary'] > info[e['dept']]['total'] / info[e['dept']]['count']
    ]
    


print(department_salary_above_average(employees))

# 這題是故意出的。

# 因為它剛好踩在你最近的能力圈：

# dict
# get()
# items()
# 二次遍歷
# 商業邏輯

# 但又不是你最近一直在刷的：

# 加總
# 最大值
# 計數

# 應該會需要思考一下，但不至於卡太久。