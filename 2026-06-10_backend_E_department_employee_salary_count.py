# 1. 檔名
# 2026-06-10_backend_E_department_employee_salary_count.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 100},
#     {"dept": "QA", "salary": 200},

#     {"dept": "HR", "salary": 350},
# ]

# threshold = 250
# 3. Output
# [
#     {"dept": "RD", "count": 2},
#     {"dept": "QA", "count": 0},
#     {"dept": "HR", "count": 1},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Count, Filter
# 練習重點
# 1. Group By
# 2. 條件計數
# 3. 保留 0 的部門
# 4. API Summary
# 5. 題目要求
# 統計每個部門薪資 >= threshold 的員工數量

# threshold = 250

# RD:

# 100 -> 不算
# 300 -> 算
# 500 -> 算

# count = 2

# QA:

# 100 -> 不算
# 200 -> 不算

# count = 0

# HR:

# 350 -> 算

# count = 1

# 注意：

# 即使 count = 0

# 也要出現在結果中

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_employee_salary_count(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    # time : 17:50 ~ 17:52(寶寶亂入) ~ 17:59重新開始 ~ 18:00結束
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, 0)
        if salary >= threshold:
            summary[dept] += 1
    return [
        {'dept' : dept, 'count' : count}
        for dept, count in summary.items()
    ]


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
        department_employee_salary_count(
            data,
            250
        )
    )

# 這題故意跟你剛剛那題很像。

# 但有個陷阱：

# QA 要保留
# count = 0

# 所以不能再用剛剛那種：

# if salary >= threshold:
#     counter[dept] += 1

# 一路偷懶了。

# 看看你會不會自然想到：

# 所有部門都先初始化

# 🐍🚀

# 這題 AC 就是第 9 題。