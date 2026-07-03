# 1. 檔名
# 2026-06-11_10_department_salary_ranking.py
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
#         "dept": "HR",
#         "avg_salary": 350,
#         "top_salary": 350
#     },
#     {
#         "dept": "RD",
#         "avg_salary": 300,
#         "top_salary": 500
#     },
#     {
#         "dept": "QA",
#         "avg_salary": 300,
#         "top_salary": 400
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Average, Max, Ranking
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Top Salary
# 4. Ranking
# 5. Multi Sort
# 5. 題目要求
# 統計每個部門：

# 1. avg_salary
# 2. top_salary

# 排序規則：

# 第一順位：
# avg_salary 由大到小

# 第二順位：
# dept 名稱由小到大

# 例如：

# HR:
# avg_salary = 350

# RD:
# avg_salary = 300

# QA:
# avg_salary = 300

# 因此：

# HR 排第一

# RD 與 QA 平手

# 依 dept 排序

# RD 在 QA 前面
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_ranking(
    data: List[Dict]
) -> List[Dict]:
    # time : 16:54 ~ 17:03
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        info = summary.setdefault(
            dept, {'count' : 0, 'total' : 0, 'top_salary' : float('-inf')}
        )
        info['count'] += 1
        info['total'] += salary
        info['top_salary'] = max(info['top_salary'], salary)
    
    return [
    #     標準寫法
    #     {'dept' : dept, 'avg_salary' : summary[dept]['total'] / summary[dept]['count'], 'top_salary' : summary[dept]['top_salary']}
    #     for dept in sorted(
    #         summary,
    #         key = lambda dept: (-summary[dept]['total'] / summary[dept]['count'], dept)
    #     )
    #     進階寫法
        {'dept' : dept, 'avg_salary' : info['total'] / info['count'], 'top_salary' : info['top_salary']}
        for dept, info in sorted(
            summary.items(),
            key = lambda item: (-item[1]['total'] / item[1]['count'], item[0])
        )
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
        department_salary_ranking(
            data
        )
    )

# 這題做完。

# 今天就是：

# 2026-06-11
# 10 題達成

# 而且會剛好把：

# Group By
# Count
# Total
# Average
# Top Salary
# Filter
# Ranking
# items
# setdefault
# update

# 全部串過一次。

# 🐍 第 10 題。今天上午～下午 Aggregation Phase 的收尾題。