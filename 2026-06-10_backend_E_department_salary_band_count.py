# 1. 檔名
# 2026-06-10_backend_E_department_salary_band_count.py
# 2. Input
# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "RD", "salary": 300},
#     {"dept": "RD", "salary": 500},

#     {"dept": "QA", "salary": 200},
#     {"dept": "QA", "salary": 400},

#     {"dept": "HR", "salary": 350},
# ]

# threshold = 300
# 3. Output
# [
#     {"dept": "RD", "count": 2},
#     {"dept": "QA", "count": 1},
#     {"dept": "HR", "count": 1},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Count, Filter
# 練習重點
# 1. 條件計數
# 2. Group By
# 3. Counter
# 4. Backend Statistics
# 5. API Summary
# 5. 題目要求
# 統計每個部門薪資 >= threshold 的員工數量

# threshold = 300

# RD:

# 100 -> 不算

# 300 -> 算

# 500 -> 算

# count = 2

# QA:

# 200 -> 不算

# 400 -> 算

# count = 1

# HR:

# 350 -> 算

# count = 1

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_salary_band_count(
    data: List[Dict],
    threshold: int
) -> List[Dict]:
    
    counter = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if salary >= threshold:
            counter[dept] = counter.get(dept, 0) + 1
    
    res = [
        {'dept' : dept, 'count' : count}
        for dept, count in counter.items()
    ]
    
    return res


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},

        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},

        {"dept": "HR", "salary": 350},
    ]

    print(
        department_salary_band_count(
            data,
            300
        )
    )

# 這題我故意出得很短。

# 因為我想確認你有沒有把昨天的：

# if salary >= threshold:
#     ...

# 以及：

# counter[dept] = counter.get(dept, 0) + 1

# 徹底變成反射。

# 現在時間：

# 2026-06-10 16:53

# 預估：

# 2~4 分鐘

# 這題應該是秒殺等級。🐍🚀