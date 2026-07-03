# 1. 檔名
# 2026-06-10_backend_E_department_top_salary_ranking.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Mary", "salary": 500},
#     {"dept": "RD", "name": "Andy", "salary": 300},

#     {"dept": "QA", "name": "Jack", "salary": 200},
#     {"dept": "QA", "name": "John", "salary": 400},

#     {"dept": "HR", "name": "David", "salary": 350},
# ]
# 3. Output
# [
#     {"dept": "RD", "name": "Mary", "salary": 500},
#     {"dept": "QA", "name": "John", "salary": 400},
#     {"dept": "HR", "name": "David", "salary": 350},
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy
# Tag      : Group By, Max, Sorting
# 練習重點
# 1. 每組保留最大值
# 2. Dict Nested Object
# 3. List[Dict]
# 4. Multiple Sort
# 5. Backend Report
# 5. 題目要求
# 找出每個部門薪資最高的員工

# 並依薪資由高到低排序

# 若薪資相同

# 依部門名稱排序

# 輸出格式：

# {
#     "dept": 部門,
#     "name": 員工名稱,
#     "salary": 薪資
# }
# 6. 完整可執行範本
from typing import List, Dict


def department_top_salary_ranking(
    data: List[Dict]
) -> List[Dict]:
    # 11:25 ~ 11:31
    
    find_max = {}
    for d in data:
        dept, name, salary = d["dept"], d["name"], d["salary"]
        if dept not in find_max or salary > find_max[dept]['salary']:
            find_max[dept] = {
                'salary' : salary,
                'name' : name
            }
    
    res = []
    for dept in find_max:
        res.append(
            {
                'dept' : dept,
                'name' : find_max[dept]['name'],
                'salary' : find_max[dept]['salary']
            }
        )
    return sorted(
        res,
        key = lambda item: (-item['salary'], item['dept'])
    )

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 500},
        {"dept": "RD", "name": "Andy", "salary": 300},

        {"dept": "QA", "name": "Jack", "salary": 200},
        {"dept": "QA", "name": "John", "salary": 400},

        {"dept": "HR", "name": "David", "salary": 350},
    ]

    print(department_top_salary_ranking(data))

# 時間：

# 2026-06-10 11:02

# 這題其實是你昨天做過的：

# department_highest_salary_employee()

# 再加上：

# List[Dict]
# +
# sorted()

# 我預估你現在應該能在：

# 3~5 分鐘

# 內解掉。🐍