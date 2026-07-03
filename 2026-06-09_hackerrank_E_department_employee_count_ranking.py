# 檔名
# 2026-06-09_hackerrank_E_department_employee_count_ranking.py
# 題目
from typing import List, Dict


def department_employee_count_ranking(data: List[Dict]) -> List[Dict]:
    """
    計算各部門員工數量

    並依員工數由多到少排序

    若人數相同，依部門名稱排序

    Input:

    [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "HR", "name": "John"},
        {"dept": "HR", "name": "Andy"},
        {"dept": "HR", "name": "David"},
    ]

    Output:

    [
        {"dept": "HR", "count": 3},
        {"dept": "RD", "count": 2},
        {"dept": "QA", "count": 1},
    ]

    說明：

    HR = 3
    RD = 2
    QA = 1

    依員工數由大到小排序
    """
    count = {}
    for d in data:
        dept = d['dept']
        count[dept] = count.get(dept, 0) + 1
    
    res_list = []
    for dept, cnt in count.items():
        res_list.append(
            {
                'dept' : dept,
                'count' : cnt
            }
        )
    return sorted(
        res_list,
        key = lambda item : (-item['count'], item['dept'])
    )
    
if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "HR", "name": "John"},
        {"dept": "HR", "name": "Andy"},
        {"dept": "HR", "name": "David"},
    ]

    print(department_employee_count_ranking(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag      : Count, Group By, Sorting, List[Dict]
# 這題的目的

# 其實不是練 Count。

# 因為：

# count[dept] = count.get(dept, 0) + 1

# 你已經太熟了。

# 我想讓你注意的是：

# 最後輸出的結構：

# [
#     {"dept": "HR", "count": 3},
#     {"dept": "RD", "count": 2},
# ]

# 跟剛剛的：

# [
#     {"dept": "QA", "avg_salary": 300},
# ]

# 是不是幾乎同一個套路？

# 如果你能在 3~5 分鐘內寫出來。

# 代表：

# Aggregation
# ↓
# List[Dict]
# ↓
# Multi Sort

# 這個模板已經開始固定下來了。🐍🚀

# 記一下開始時間。