# 檔名
# 2026-06-09_hackerrank_E_department_total_salary_sorted.py
# 題目
from typing import List, Dict


def department_total_salary_sorted(data: List[Dict]) -> List[Dict]:
    """
    計算各部門總薪資，並由高到低排序

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    [
        {"dept": "RD", "salary": 400},
        {"dept": "HR", "salary": 250},
        {"dept": "QA", "salary": 200},
    ]

    說明：

    RD = 400
    HR = 250
    QA = 200

    依薪資由大到小排序
    """
    # time : 11:50 ~ 11:54
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    
    sorted_list = []
    for dept, salary in total.items(): # items 會回傳 turple
        sorted_list.append({
            'dept' : dept,
            'salary' : salary
        })
        
    return sorted(
        sorted_list,
        key = lambda item : -item['salary']
    )


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
    ]

    print(department_total_salary_sorted(data))
    
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag      : Dict, Items, Sorting, List[Dict], Group By
# 本題想練什麼

# 第一階段：

# {
#     "RD": 400,
#     "QA": 200,
#     "HR": 250
# }

# 第二階段：

# 轉成：

# [
#     {"dept": "RD", "salary": 400},
#     {"dept": "QA", "salary": 200},
#     {"dept": "HR", "salary": 250},
# ]

# 第三階段：

# 依薪資排序：

# [
#     {"dept": "RD", "salary": 400},
#     {"dept": "HR", "salary": 250},
#     {"dept": "QA", "salary": 200},
# ]
# 提示（卡住再看）

# 你可能會用到：

# total.items()

# 以及：

# sorted(
#     xxx,
#     key=lambda item: ...
# )

# 這題開始接近真實 API 回傳格式了。

# 以前你都是：

# return "RD"

# 或

# return {"RD": 400}

# 這題開始組裝：

# List[Dict]

# 這是 Backend 很常見的資料型態。