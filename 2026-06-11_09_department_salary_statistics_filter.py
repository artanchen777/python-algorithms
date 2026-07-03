# 1. 檔名
# 2026-06-11_09_department_salary_statistics_filter.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Mary", "salary": 500},
#     {"dept": "RD", "name": "John", "salary": 300},

#     {"dept": "QA", "name": "Jack", "salary": 400},
#     {"dept": "QA", "name": "Amy", "salary": 200},

#     {"dept": "HR", "name": "David", "salary": 350},
# ]

# threshold = 350
# 3. Output
# [
#     {
#         "dept": "RD",
#         "avg_salary": 300,
#         "top_employee": "Mary",
#         "top_salary": 500
#     },
#     {
#         "dept": "QA",
#         "avg_salary": 300,
#         "top_employee": "Jack",
#         "top_salary": 400
#     },
#     {
#         "dept": "HR",
#         "avg_salary": 350,
#         "top_employee": "David",
#         "top_salary": 350
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Max, Aggregate Record, Filter
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Top Employee
# 4. Filter
# 5. Aggregate Report
# 5. 題目要求
# 統計每個部門：

# 1. avg_salary
# 2. top_employee
# 3. top_salary

# 只保留：

# top_salary >= threshold

# threshold = 350

# 例如：

# RD:

# top_salary = 500

# 保留

# QA:

# top_salary = 400

# 保留

# HR:

# top_salary = 350

# 保留

# 如果某部門 top_salary < 350

# 則不輸出
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_statistics_filter(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    # time : 16:36~16:42
    
    summary = {}
    for d in data:
        dept, name, salary = d["dept"], d["name"], d["salary"]
        info = summary.setdefault(
            dept,
            {
                'count' : 0,
                'total' : 0,
                "top_employee": '',
                "top_salary": float('-inf')
            }
        )
        info['count'] += 1
        info['total'] += salary
        if salary > info['top_salary'] :
            info.update({
                'top_employee': name,
                'top_salary': salary
            })
    return [
        {
            "dept": dept,
            "avg_salary": info['total'] / info['count'],
            "top_employee": info['top_employee'],
            "top_salary": info['top_salary']
        }
        for dept, info in summary.items()
        if info['top_salary'] >= threshold
    ]

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 500},
        {"dept": "RD", "name": "John", "salary": 300},

        {"dept": "QA", "name": "Jack", "salary": 400},
        {"dept": "QA", "name": "Amy", "salary": 200},

        {"dept": "HR", "name": "David", "salary": 350},
    ]

    print(
        department_salary_statistics_filter(
            data,
            350
        )
    )

# 這題故意跟上一題 90% 像。

# 我要看的是你會不會自然做到：

# 複製上一題模型
# ↓
# 局部修改
# ↓
# 完成新需求

# 這其實就是你以前工作裡最強的能力。

# 🐍 第 9 題開始。