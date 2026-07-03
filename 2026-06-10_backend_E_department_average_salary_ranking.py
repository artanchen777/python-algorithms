# 1. 檔名
# 2026-06-10_backend_E_department_average_salary_ranking.py
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
#     {"dept": "HR", "avg_salary": 350},
#     {"dept": "QA", "avg_salary": 300},
#     {"dept": "RD", "avg_salary": 300},
# ]
# 4. 題目要求
# 計算各部門平均薪資

# 並依平均薪資由高到低排序

# 若平均薪資相同

# 依部門名稱排序

# 例如：

# HR = 350

# QA = (200 + 400) / 2 = 300

# RD = (100 + 300 + 500) / 3 = 300

# 所以：

# HR 在前

# QA 與 RD 同為 300

# QA < RD

# 因此 QA 排前面


# ### 難度資訊

# ```text
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Aggregate, Sorting
# 練習重點
# 1. count + total
# 2. average
# 3. list[dict]
# 4. sorted
# 5. 多條件排序
# 5. 完整可執行範本
from typing import List, Dict


def department_average_salary_ranking(
    data: List[Dict]
) -> List[Dict]:
    # 10:53 ~ 10:56
    
    summary = {}
    for d in data:
        dept, salary = d["dept"], d["salary"]
        if dept not in summary:
            summary[dept] = {}
        summary[dept]['total'] = summary[dept].get('total', 0) + salary
        summary[dept]['count'] = summary[dept].get('count', 0) + 1

    avg_list = []
    for s in summary:
        avg_list.append({
            'dept' : s,
            'avg_salary' : summary[s]['total'] / summary[s]['count']
        })
        
    return sorted(
        avg_list,
        key=lambda item: (-item['avg_salary'], item['dept'])
    )
    



if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(department_average_salary_ranking(data))

# 這題其實是把你剛剛那題：

# Group By
# +
# Average

# 再加上昨天已經碰過的：

# sorted(
#     res,
#     key=lambda item: (...)
# )

# 所以我預估：

# 3~6 分鐘

# 就能解掉。

# 開始計時。🐍