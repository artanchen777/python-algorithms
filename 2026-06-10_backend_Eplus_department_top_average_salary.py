# 1. 檔名
# 2026-06-10_backend_Eplus_department_top_average_salary.py
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
# {
#     "dept": "HR",
#     "avg_salary": 350
# }
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Average, Max
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Running Leader
# 4. Aggregate + Compare
# 5. Backend Report
# 5. 題目要求
# 計算各部門平均薪資

# 找出平均薪資最高的部門

# 輸出：

# {
#     "dept": 部門名稱,
#     "avg_salary": 平均薪資
# }

# 範例：

# RD:

# (100 + 500 + 300) / 3

# = 300

# QA:

# (400 + 200) / 2

# = 300

# HR:

# 350

# = 350

# 所以：

# {
#     "dept": "HR",
#     "avg_salary": 350
# }
# 6. 完整可執行範本
from typing import List, Dict


def department_top_average_salary(
    data: List[Dict]
) -> Dict:
    # time : 22:53 ~ 22:59
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, {})
        summary[dept]['count'] = summary[dept].get('count', 0) + 1
        summary[dept]['total'] = summary[dept].get('total', 0) + salary
    # 拼湊寫法    
    # return [
    #     {'dept' : dept, 'avg_salary' : summary[dept]['total'] / summary[dept]['count']}
    #     for dept in sorted(
    #         summary,
    #         key = lambda dept : -(summary[dept]['total'] / summary[dept]['count'])
    #     )[:1]
    # ][0]
    
    # 標準寫法
    max_dept = max(
        summary,
        key = lambda dept : summary[dept]['total'] / summary[dept]['count']
    )
    
    return {
        'dept' : max_dept,
        'avg_salary' : summary[max_dept]['total'] / summary[max_dept]['count']
    }

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
        department_top_average_salary(data)
    )

# 這題有兩種思路：

# A.
# 先 Group By
# 再算平均
# 再找最大

# B.
# Group By
# 維護 count + total
# 最後掃一次找冠軍

# 我比較好奇你現在會自然選哪一種。

# 這題 AC。

# 今天就正式達成：

# 2026-06-10

# 15 題里程碑

# 🐍🏆