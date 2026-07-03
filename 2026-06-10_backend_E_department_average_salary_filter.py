# 1. 檔名
# 2026-06-10_backend_E_department_average_salary_filter.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 100},
#     {"dept": "QA", "salary": 200},

#     {"dept": "HR", "salary": 350},
# ]

# threshold = 300
# 3. Output
# [
#     {"dept": "RD", "avg_salary": 300},
#     {"dept": "HR", "avg_salary": 350},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Average, Filter
# 練習重點
# 1. count + total
# 2. average
# 3. filter
# 4. Aggregate + Filter
# 5. API Summary
# 5. 題目要求
# 計算各部門平均薪資

# 只保留平均薪資 >= threshold 的部門

# threshold = 300

# RD:

# (100 + 300 + 500) / 3 = 300

# 保留

# QA:

# (100 + 200) / 2 = 150

# 不保留

# HR:

# 350

# 保留

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_average_salary_filter(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        
        summary.setdefault(
            dept,
            {'count' : 0, 'salary' : 0}
        )

        summary[dept]['count'] += 1
        summary[dept]['salary'] += salary
    
    # 進階寫法
    return [
        {'dept' : dept, 'avg_salary' : info['salary'] / info['count']} 
        for dept, info in summary.items()
        if info['salary'] / info['count'] >= threshold
    ]
    
    # 標準寫法
    # res = []
    # for dept in summary:
    #     avg_salary = summary[dept]['salary'] / summary[dept]['count']
    #     if avg_salary >= threshold:
    #         res.append(
    #             {
    #                 'dept' : dept,
    #                 'avg_salary' : avg_salary
    #             }
    #         )
    # return res

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 100},
        {"dept": "QA", "salary": 200},

        {"dept": "HR", "salary": 350},
    ]

    print(
        department_average_salary_filter(
            data,
            300
        )
    )

# 這題是：

# Group By
# +
# Average
# +
# Filter

# 而且 QA 被故意改成平均 150，這樣才能真正測出：

# if avg_salary >= threshold:

# 的邏輯。🐍