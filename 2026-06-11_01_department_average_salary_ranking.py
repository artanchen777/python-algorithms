# 1. 檔名
# 2026-06-11_backend_Eplus_department_average_salary_ranking.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 500},
#     {"dept": "RD", "salary": 300},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]
# 3. Output
# [
#     {"dept": "HR", "avg_salary": 350},
#     {"dept": "QA", "avg_salary": 300},
#     {"dept": "RD", "avg_salary": 300},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Average, Sorting
# 練習重點
# 1. Count + Total
# 2. Average
# 3. Dict -> List[Dict]
# 4. Multi Sort
# 5. Ranking Report
# 5. 題目要求
# 計算每個部門平均薪資

# 依 avg_salary 由大到小排序

# 如果 avg_salary 相同

# 則依 dept 名稱排序

# 輸出順序必須符合排序結果
# 6. 完整可執行範本
from typing import List, Dict


def department_average_salary_ranking(
    data: List[Dict]
) -> List[Dict]:
    # time : 09:58~10:04
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, {'count' : 0, 'salary' : 0})
        summary[dept]['count'] += 1
        summary[dept]['salary'] += salary
    
    return [
        {'dept' : dept, 'avg_salary' : summary[dept]['salary'] / summary[dept]['count']}
        for dept in sorted(
            summary,
            key = lambda dept: (-summary[dept]['salary'] / summary[dept]['count'], dept)
        )
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
        department_average_salary_ranking(data)
    )

# 這題其實你以前做過類似的。

# 但我故意隔了一天再出。

# 我要看的是：

# count + total
# ↓
# avg
# ↓
# list[dict]
# ↓
# sorted

# 這條資料流有沒有開始變成直覺。