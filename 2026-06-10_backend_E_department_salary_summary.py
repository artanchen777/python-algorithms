# 1. 檔名
# 2026-06-10_backend_E_department_salary_summary.py
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
# [
#     {
#         "dept": "RD",
#         "count": 3,
#         "total_salary": 900
#     },
#     {
#         "dept": "QA",
#         "count": 2,
#         "total_salary": 600
#     },
#     {
#         "dept": "HR",
#         "count": 1,
#         "total_salary": 350
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Count, Sum, Aggregate
# 練習重點
# 1. 同時維護多個統計值
# 2. count + total
# 3. dict[dict]
# 4. API Response Format
# 5. Aggregate Pattern
# 5. 題目要求
# 統計每個部門：

# 1. 員工數量(count)
# 2. 薪資總和(total_salary)

# 輸出格式：

# {
#     "dept": 部門,
#     "count": 員工數,
#     "total_salary": 薪資總和
# }

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_summary(
    data: List[Dict]
) -> List[Dict]:
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if dept not in summary:
            summary[dept] = {'count' : 0, 'total_salary' : 0}
        summary[dept]['count'] = summary[dept]['count'] + 1
        summary[dept]['total_salary'] = summary[dept]['total_salary'] + salary
    # 標準寫法
    # return [
    #     {'dept' : dept, 'count' : summary[dept]['count'], 'total_salary' : summary[dept]['total_salary']}
    #     for dept in summary
    # ]
    
    # 高階寫法
    return [
        {'dept' : dept, **info} # **info 會直接展開 dict
        for dept, info in summary.items()
    ]

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(department_salary_summary(data))

# 這題我故意出得很樸實。

# 因為我想看看你會不會直接反射出：

# summary[dept] = {
#     'count': ...,
#     'total_salary': ...
# }

# 而不是拆成：

# count = {}
# total = {}

# 這是從昨天到今天一直在進步的地方。

# 時間：

# 2026-06-10 17:00

# 預估：

# 2~4 分鐘

# 這題應該是目前你的舒適區。🐍🚀