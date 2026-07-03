# 1. 檔名
# 20260615_01_hackerrank_M_DepartmentQualifiedSalary.py
# 2. Input
# data = [
#     {"dept": "A", "salary": 100},
#     {"dept": "A", "salary": 300},
#     {"dept": "A", "salary": 200},
#     {"dept": "B", "salary": 150},
#     {"dept": "B", "salary": 100},
#     {"dept": "C", "salary": 400},
#     {"dept": "C", "salary": 500},
# ]
# 3. Output
# [
#     {"dept": "A", "total_salary": 600},
#     {"dept": "C", "total_salary": 900},
# ]
# 4. 難度資訊 + 練習重點
# LeetCode 難度
# Easy
# 體感難度（以你目前進度）
# Medium
# 練習重點
# dict
# setdefault
# 累加
# filter
# sorted
# list comprehension
# 5. 題目目標、要求、限制

# 公司想分析各部門的薪資總額。

# 請完成以下需求：

# 計算每個部門的薪資總和
# 只保留總薪資 >= 500 的部門
# 按照部門名稱排序
# 回傳指定格式
# 6. 完整可執行範本
from typing import List

# time : 22:36 ~ 22:40
data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 300},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 150},
    {"dept": "B", "salary": 100},
    {"dept": "C", "salary": 400},
    {"dept": "C", "salary": 500},
]


def department_qualified_salary(data: List[dict]) -> List[dict]:

    # summary = {}
    # res = {}
    # for d in data:
    #     dept, salary = d['dept'], d['salary']
    #     summary[dept] = summary.get(dept, 0) + salary
    #     if summary[dept] >= 500:
    #         res[dept] = max(res.get(dept, 0), summary[dept])
    
    # return [
    #     {'dept' : dept, 'total_salary' : res[dept]}
    #     for dept in sorted(res)
    # ]
    
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary[dept] = summary.get(dept, 0) + salary
    
    return [
        {'dept' : dept, 'total_salary' : total_salary}
        for dept, total_salary in sorted(summary.items())
        if total_salary >= 500
    ]


print(department_qualified_salary(data))
# 7. 額外說明

# 不要用：

# pandas
# itertools
# collections.defaultdict

# 只用你目前已經熟悉的：

# dict
# for
# if
# sorted
# list comprehension

# 即可。

# 這題的真正目標其實不是加總。

# 而是開始訓練你把：

# group by
# ↓
# sum
# ↓
# filter
# ↓
# sort
# ↓
# output

# 拆成明確的 5 個步驟。

# 這是之後很多 HackerRank Medium 題目的核心思維。

# 先寫。

# 寫完直接貼第一版，我不看答案，只看你的思路。