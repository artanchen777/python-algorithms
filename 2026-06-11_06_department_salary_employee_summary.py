# 1. 檔名
# 2026-06-11_06_department_salary_employee_summary.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Tom", "salary": 200},
#     {"dept": "RD", "name": "Mary", "salary": 300},

#     {"dept": "QA", "name": "Jack", "salary": 400},
#     {"dept": "QA", "name": "Amy", "salary": 500},

#     {"dept": "HR", "name": "David", "salary": 600},
# ]
# 3. Output
# [
#     {
#         "dept": "RD",
#         "employee_count": 3,
#         "unique_employee_count": 2,
#         "total_salary": 600
#     },
#     {
#         "dept": "QA",
#         "employee_count": 2,
#         "unique_employee_count": 2,
#         "total_salary": 900
#     },
#     {
#         "dept": "HR",
#         "employee_count": 1,
#         "unique_employee_count": 1,
#         "total_salary": 600
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Dict, Set, Aggregate
# 練習重點
# 1. Dict[Dict]
# 2. Dict[Set]
# 3. Count
# 4. Unique Count
# 5. Total Salary
# 6. Summary Report
# 5. 題目要求
# 統計每個部門：

# 1. employee_count
#    (資料總筆數)

# 2. unique_employee_count
#    (不同員工數)

# 3. total_salary
#    (薪資總和)

# 例如：

# RD:

# Tom 100
# Tom 200
# Mary 300

# employee_count = 3

# unique_employee_count = 2

# total_salary = 600
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_employee_summary(
    data: List[Dict]
) -> List[Dict]:
    # time : 12:37~12:44
    summary = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        summary.setdefault(dept, {'employee_count' : 0, 'unique_employee' : set(), 'total_salary' : 0})
        summary[dept]['employee_count'] += 1
        summary[dept]['unique_employee'].add(name)
        summary[dept]['total_salary'] += salary
        
    return [
        {
            'dept' : dept, 
            'employee_count' : info['employee_count'], 
            'unique_employee_count' : len(info['unique_employee']), 
            'total_salary' : info['total_salary']
        }
        for dept, info in summary.items()
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Tom", "salary": 200},
        {"dept": "RD", "name": "Mary", "salary": 300},

        {"dept": "QA", "name": "Jack", "salary": 400},
        {"dept": "QA", "name": "Amy", "salary": 500},

        {"dept": "HR", "name": "David", "salary": 600},
    ]

    print(
        department_salary_employee_summary(
            data
        )
    )

# 這題其實就是把你前面練過的：

# Count
# +
# Unique Count
# +
# Salary Sum

# 合併到同一個 Summary。

# 很像真實 ETL 的中繼資料表。

# 我預估你現在大概會在：

# 3 ~ 6 分鐘

# 內完成。🐍🚀