# 檔名

# 2026-06-13_004_backend_department_salary_range.py

# 題目

# 給定員工資料：

# from typing import List

# data = [
#     {"dept": "A", "salary": 100},
#     {"dept": "A", "salary": 300},
#     {"dept": "A", "salary": 200},
#     {"dept": "B", "salary": 500},
#     {"dept": "B", "salary": 400},
#     {"dept": "C", "salary": 700},
# ]

# 請實作：

# def department_salary_range(data: List[dict]) -> List[dict]:
# Output
# [
#     {"dept": "A", "salary_range": 200},
#     {"dept": "B", "salary_range": 100},
#     {"dept": "C", "salary_range": 0},
# ]
# 題目要求與限制
# salary_range = 部門最高薪資 - 部門最低薪資
# 回傳 List[dict]
# 依 dept 升冪排序
# 不可使用 pandas
# 不可先把所有薪資存成 list 再計算
# 每個部門只能維護計算所需資訊
# 完整可執行範本
from typing import List

data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 300},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 500},
    {"dept": "B", "salary": 400},
    {"dept": "C", "salary": 700},
]


def department_salary_range(data: List[dict]) -> List[dict]:
    # time : 21:50 ~ 21:54
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, {'max' : float('-inf'), 'min' : float('inf')})
        if salary > summary[dept]['max']:
            summary[dept]['max'] = salary
        if salary < summary[dept]['min']:
            summary[dept]['min'] = salary
    
    return [
        {'dept' : dept, 'salary_range' : info['max'] - info['min']}
        for dept, info in sorted(summary.items())
    ]


print(department_salary_range(data))

# 這題是承接你剛剛的：

# max

# 下一步變成：

# max + min

# 仍然屬於同一條基礎功路線。AC 後再進 005。