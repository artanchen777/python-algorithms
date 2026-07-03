# 1. 檔名
# 2026-06-11_03_department_employee_count_ranking.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom"},
#     {"dept": "RD", "name": "Mary"},
#     {"dept": "RD", "name": "John"},

#     {"dept": "QA", "name": "Jack"},
#     {"dept": "QA", "name": "Amy"},

#     {"dept": "HR", "name": "David"},

#     {"dept": "IT", "name": "Bob"},
#     {"dept": "IT", "name": "Kevin"},
#     {"dept": "IT", "name": "Lucy"},
#     {"dept": "IT", "name": "Eric"},
# ]
# 3. Output
# [
#     {
#         "dept": "IT",
#         "employee_count": 4
#     },
#     {
#         "dept": "RD",
#         "employee_count": 3
#     },
#     {
#         "dept": "QA",
#         "employee_count": 2
#     },
#     {
#         "dept": "HR",
#         "employee_count": 1
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Count, Ranking, Sorting
# 練習重點
# 1. Group By
# 2. Count
# 3. Dict -> List[Dict]
# 4. Multi Sort
# 5. Ranking Report
# 5. 題目要求
# 統計每個部門的人數

# 依 employee_count 由大到小排序

# 如果 employee_count 相同

# 則依 dept 名稱排序

# 輸出格式：

# {
#     "dept": 部門名稱,
#     "employee_count": 人數
# }
# 6. 完整可執行範本
from typing import List, Dict


def department_employee_count_ranking(
    data: List[Dict]
) -> List[Dict]:
    # time : 10:23~10:26
    
    summary = {}
    for d in data:
        dept = d['dept']
        summary[dept] = summary.get(dept, 0) + 1
    
    return [
        {'dept' : dept, 'employee_count' : count}
        for dept, count in sorted(
            summary.items(),
            key = lambda item: (-item[1], item[0])
        )
    ] 

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "RD", "name": "John"},

        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "Amy"},

        {"dept": "HR", "name": "David"},

        {"dept": "IT", "name": "Bob"},
        {"dept": "IT", "name": "Kevin"},
        {"dept": "IT", "name": "Lucy"},
        {"dept": "IT", "name": "Eric"},
    ]

    print(
        department_employee_count_ranking(
            data
        )
    )

# 這題我故意把：

# salary

# 拿掉。

# 只剩：

# dept
# name

# 我要看你會不會自然發現：

# 其實 name 根本不用存

# 只需要：

# counter[dept] += 1

# 就夠了。