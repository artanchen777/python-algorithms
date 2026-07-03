# 1. 檔名
# 2026-06-10_backend_E_department_salary_range.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 500},
#     {"dept": "RD", "salary": 300},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]
# 3. Output
# [
#     {"dept": "RD", "range": 400},
#     {"dept": "QA", "range": 200},
#     {"dept": "HR", "range": 0},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Min, Max, Aggregate
# 練習重點
# 1. 每組同時維護 Min
# 2. 每組同時維護 Max
# 3. Dict Nested Object
# 4. Aggregate Result
# 5. 題目要求
# 計算各部門薪資區間(range)

# range = max_salary - min_salary

# RD:

# max = 500
# min = 100

# range = 400

# QA:

# max = 400
# min = 200

# range = 200

# HR:

# 只有一筆資料

# range = 0

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict

# time : 10:42 ~ 10:47
def department_salary_range(
    data: List[Dict]
) -> List[Dict]:
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if dept not in summary:
            summary[dept] = {'max': salary, 'min': salary, 'range' : 0}
        
        if salary > summary[dept]['max']:
            summary[dept]['max'] = salary
            summary[dept]['range'] = salary - summary[dept]['min']
        
        if salary < summary[dept]['min']:
            summary[dept]['min'] = salary
            summary[dept]['range'] = summary[dept]['max'] - salary

    res = [
        {
            'dept' : dept,
            'range' : summary[dept]['range']
        }
        for dept in summary
    ]
    
    return res


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 500},
        {"dept": "RD", "salary": 300},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(department_salary_range(data))

# 這題有個小陷阱：

# max
# +
# min

# 要一起維護。

# 我想看看你會不會自然想到：

# summary[dept] = {
#     'max': ...,
#     'min': ...
# }

# 開始計時。

# 2026-06-10 16:42

# 🐍🚀