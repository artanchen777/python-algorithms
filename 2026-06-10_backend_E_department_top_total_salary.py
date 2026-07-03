# 1. 檔名
# 2026-06-10_backend_E_department_top_total_salary.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]
# 3. Output
# {
#     "dept": "RD",
#     "total_salary": 900
# }
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Sum, Max
# 練習重點
# 1. Group By
# 2. Sum
# 3. 找最大值
# 4. Dict Aggregation
# 5. Backend Report
# 5. 題目要求
# 計算各部門薪資總和

# 找出總薪資最高的部門

# 輸出：

# {
#     "dept": 部門名稱,
#     "total_salary": 總薪資
# }

# 例如：

# RD:

# 100 + 300 + 500 = 900

# QA:

# 200 + 400 = 600

# HR:

# 350

# 所以輸出：

# {
# "dept": "RD",
# "total_salary": 900
# }


# ---

# ## 6. 完整可執行範本

# ```python
from typing import List, Dict


def department_top_total_salary(
    data: List[Dict]
) -> Dict:
    summary = {}
    max_info = {'dept' : '', 'total_salary' : float('-inf')}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary[dept] = summary.get(dept, 0) + salary
        if summary[dept] > max_info['total_salary']:
            max_info['dept'] = dept
            max_info['total_salary'] = summary[dept]
    return max_info

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(department_top_total_salary(data))

# 這題我故意沒要求：

# sorted()

# 看看你會不會直接想到：

# best_dept
# best_salary

# 一路維護到結束。

# 預估：

# 3~6 分鐘

# 🐍🚀