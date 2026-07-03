# 檔名

# 2026-06-13_005_backend_department_salary_summary.py

# 題目

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

# def department_salary_summary(data: List[dict]) -> List[dict]:

# Output

# [
#     {
#         "dept": "A",
#         "min_salary": 100,
#         "max_salary": 300,
#         "salary_range": 200,
#     },
#     {
#         "dept": "B",
#         "min_salary": 400,
#         "max_salary": 500,
#         "salary_range": 100,
#     },
#     {
#         "dept": "C",
#         "min_salary": 700,
#         "max_salary": 700,
#         "salary_range": 0,
#     },
# ]

# 題目要求與限制

# 回傳 List[dict]
# 依 dept 升冪排序
# 不可使用 pandas
# 不可先把所有薪資存成 list
# 每個部門只能維護必要資訊

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


def department_salary_summary(data: List[dict]) -> List[dict]:
    # time : 21:57 ~ 22:02

    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        info = summary.setdefault(dept, {'max_salary' : float('-inf'), 'min_salary' : float('inf')})
        if salary > info['max_salary']:
            info['max_salary'] = salary
        if salary < info['min_salary']:
            info['min_salary'] = salary
        info['salary_range'] = info['max_salary'] - info['min_salary']

    return [
        {'dept' : dept, **info}
        for dept, info in sorted(summary.items())
    ]


print(department_salary_summary(data))

# 這題其實是上一題的自然延伸。

# 你會發現：

# salary_range

# 其實只是：

# max
# min

# 衍生出來的欄位而已。

# 看看你會不會開始主動避免重複計算。