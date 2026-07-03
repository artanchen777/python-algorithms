# 1. 檔名
# 2026-06-11_08_department_salary_statistics.py
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
# Tag      : Group By, Average, Max, Aggregate Record
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Top Employee
# 4. Dict[Dict]
# 5. Aggregate Report
# 5. 題目要求
# 統計每個部門：

# 1. avg_salary
#    (平均薪資)

# 2. top_employee
#    (最高薪員工)

# 3. top_salary
#    (最高薪資)

# 例如：

# RD:

# Tom 100
# Mary 500
# John 300

# avg_salary = 300

# top_employee = Mary

# top_salary = 500
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_statistics(
    data: List[Dict]
) -> List[Dict]:
    # time : 16:12~16:19
    summary = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        info = summary.setdefault(dept, {
            'count' : 0,
            'total' : 0,
            'top_employee': '',
            'top_salary': float('-inf')
        })
        info['count'] += 1
        info['total'] += salary
        if salary > info['top_salary']:
            info.update(
                {
                    'top_employee': name,
                    'top_salary': salary
                }
            )
    
    return [
        {
            'dept' : dept,
            'avg_salary': info['total'] / info['count'],
            'top_employee': info['top_employee'],
            'top_salary': info['top_salary']
        }
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
        department_salary_statistics(
            data
        )
    )

# 這題有一個我刻意埋的點。

# 你剛剛那題維護的是：

# {
#     'employee_count': 0,
#     'top_employee': '',
#     'top_salary': float('-inf')
# }

# 這次你會發現：

# count
# +
# total_salary
# +
# top_employee
# +
# top_salary

# 開始一起存在了。

# 這很像真正的 ETL 中繼資料結構。

# 🐍 第 8 題開始。