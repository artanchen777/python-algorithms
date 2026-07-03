# 1. 檔名
# 2026-06-10_backend_E_department_max_salary_filter.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 500},
#     {"dept": "RD", "salary": 300},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]

# threshold = 450
# 3. Output
# [
#     {"dept": "RD", "max_salary": 500}
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Max, Filter
# 練習重點
# 1. Max
# 2. Group By
# 3. Aggregate
# 4. Filter
# 5. Dict[Dict]
# 5. 題目要求
# 找出各部門最高薪資

# 只保留：

# max_salary >= threshold

# threshold = 450

# RD:

# max = 500

# 保留

# QA:

# max = 400

# 不保留

# HR:

# max = 350

# 不保留

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_max_salary_filter(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    # time : 18:08 ~ 18:11
    find_max = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        find_max[dept] = max(find_max.get(dept, 0), salary)
    return [
        {'dept' : dept, 'max_salary' : salary}
        for dept, salary in find_max.items()
        if salary >= threshold
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 500},
        {"dept": "RD", "salary": 300},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(
        department_max_salary_filter(
            data,
            450
        )
    )

# 這題 AC。

# 今天白天就達成：

# 10 題里程碑

# 了。🐍🏁