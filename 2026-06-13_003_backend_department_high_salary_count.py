# 檔名

# 2026-06-13_003_backend_department_high_salary_count.py

# Input

# data = [
#     {"dept": "A", "salary": 100},
#     {"dept": "A", "salary": 300},
#     {"dept": "A", "salary": 250},
#     {"dept": "B", "salary": 500},
#     {"dept": "B", "salary": 100},
#     {"dept": "C", "salary": 200},
# ]

# Output

# [
#     {"dept": "A", "count": 2},
#     {"dept": "B", "count": 1},
# ]

# 難度

# Phase 1 ~ Phase 2

# group by
# filter
# count
# sorting

# 題目要求

# 統計每個部門 salary >= 250 的員工數量

# 只保留 count > 0 的部門

# 回傳 list[dict]

# 依 count DESC 排序

# 若 count 相同，dept ASC 排序

# 禁止使用 Counter

# 禁止先 group 完再第二次掃描原始資料

# 請在一次掃描中完成統計

# 完整可執行範本

from typing import List

data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 300},
    {"dept": "A", "salary": 250},
    {"dept": "B", "salary": 500},
    {"dept": "B", "salary": 100},
    {"dept": "C", "salary": 200},
]


def department_high_salary_count(data: List[dict]) -> List[dict]:
    # time : 21:39 ~ 21:42
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if salary >= 250:
            summary[dept] = summary.get(dept, 0) + 1

    return [
        {'dept' : dept, 'count' : count}
        for dept, count in sorted(
            summary.items(),
            key = lambda item: (-item[1], item[0])
        )
    ]
print(department_high_salary_count(data))

# 這題 3~5 分鐘內應該能 AC，做完直接貼。今天目標還有 3 題。