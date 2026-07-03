# 1. 檔名
# 2026-06-10_backend_E_department_salary_above_average.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Mary", "salary": 300},
#     {"dept": "RD", "name": "Andy", "salary": 200},
#     {"dept": "QA", "name": "Jack", "salary": 200},
#     {"dept": "QA", "name": "John", "salary": 400},
# ]
# 3. Output
# [
#     {"dept": "RD", "name": "Mary", "salary": 300},
#     {"dept": "QA", "name": "John", "salary": 400},
# ]
# 4. 題目要求
# 找出高於部門平均薪資的員工

# 1. 先計算各部門平均薪資
# 2. 找出高於部門平均薪資的員工
# 3. 等於平均值不算
# 4. 保持原始出現順序
# 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Aggregate, Filter
# 5. 完整可執行範本
from typing import List, Dict


def department_salary_above_average(data: List[Dict]) -> List[Dict]:
    # 10:42 ~ 10:48
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if dept not in summary:
            summary[dept] = {}
        summary[dept]['count'] = summary[dept].get('count', 0) + 1
        summary[dept]['total'] = summary[dept].get('total', 0) + salary
    
    for dept in summary:
        summary[dept]['average'] = summary[dept]['total'] / summary[dept]['count']
    
    res = []
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        if salary > summary[dept]['average']:
            res.append(
                {
                    'dept' : dept,
                    'name' : name,
                    'salary' : salary
                }
            )
    return res

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 300},
        {"dept": "RD", "name": "Andy", "salary": 200},
        {"dept": "QA", "name": "Jack", "salary": 200},
        {"dept": "QA", "name": "John", "salary": 400},
    ]

    print(department_salary_above_average(data))

# 這題有個你最近很需要練的點：

# 第一次迭代：
# 算平均需要的資料

# 第二次迭代：
# 依平均值過濾資料

# 也就是你昨天提過的：

# 不是所有題目都能一個 for 解決

# 有些需求本來就需要：

# 統計
# ↓
# 再篩選

# 開始計時吧。🐍

# 2026-06-10 10:42