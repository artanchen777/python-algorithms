# 1. 檔名
# 2026-06-11_07_department_top_salary_summary.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Mary", "salary": 500},
#     {"dept": "RD", "name": "John", "salary": 300},

#     {"dept": "QA", "name": "Jack", "salary": 400},
#     {"dept": "QA", "name": "Amy", "salary": 200},

#     {"dept": "HR", "name": "David", "salary": 350},
# ]
# 3. Output
# [
#     {
#         "dept": "RD",
#         "employee_count": 3,
#         "top_employee": "Mary",
#         "top_salary": 500
#     },
#     {
#         "dept": "QA",
#         "employee_count": 2,
#         "top_employee": "Jack",
#         "top_salary": 400
#     },
#     {
#         "dept": "HR",
#         "employee_count": 1,
#         "top_employee": "David",
#         "top_salary": 350
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Max, Aggregate Record
# 練習重點
# 1. Dict[Dict]
# 2. Count
# 3. Max
# 4. 關聯資料保存
# 5. Summary Report
# 5. 題目要求
# 統計每個部門：

# 1. employee_count
#    (資料筆數)

# 2. top_employee
#    (最高薪員工)

# 3. top_salary
#    (最高薪資)

# 例如：

# RD:

# Tom 100
# Mary 500
# John 300

# employee_count = 3

# top_employee = Mary

# top_salary = 500
# 6. 完整可執行範本
from typing import List, Dict


def department_top_salary_summary(
    data: List[Dict]
) -> List[Dict]:
    # time : 15:58 ~ 16:05
    
    summary = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        summary.setdefault(
            dept,
            {
                'employee_count': 0,
                'top_employee': '',
                'top_salary': float('-inf')
            }
        )
        summary[dept]['employee_count'] += 1
        if salary > summary[dept]['top_salary']:
            summary[dept].update(
                { 'top_employee': name, 'top_salary': salary }
            )
    return [
        {'dept' : dept, **info}
        for dept, info in summary.items()
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
        department_top_salary_summary(
            data
        )
    )

# 這題是我們前面練過的兩條線合併：

# employee_count
# +
# top salary record

# 我想看你會不會自然想到：

# {
#     'employee_count': 0,
#     'top_employee': '',
#     'top_salary': float('-inf')
# }

# 這種結構。

# 這在 ETL 和報表系統裡非常常見。

# 🐍 第 7 題開始。