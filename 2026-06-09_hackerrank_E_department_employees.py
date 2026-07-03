# 檔名
# 2026-06-09_hackerrank_E_department_employees.py
# 題目
from typing import List, Dict


def department_employees(data: List[Dict]) -> Dict[str, List[Dict]]:
    """
    將員工依部門分組

    Input:

    [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "QA", "name": "Jack", "salary": 200},
        {"dept": "RD", "name": "Mary", "salary": 300},
    ]

    Output:

    {
        "RD": [
            {"name": "Tom", "salary": 100},
            {"name": "Mary", "salary": 300},
        ],
        "QA": [
            {"name": "Jack", "salary": 200}
        ]
    }
    """
    group = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        if dept not in group:
            group[dept] = []
        group[dept].append({
            'name' : name,
            'salary' : salary
        })
    return group

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "QA", "name": "Jack", "salary": 200},
        {"dept": "RD", "name": "Mary", "salary": 300},
    ]

    print(department_employees(data))
    
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag      : Dict[str, List[Dict]]
# 本題重點

# 以前你存的是：

# {
#     "RD": ["Tom", "Mary"]
# }

# 今天變成：

# {
#     "RD": [
#         {"name": "Tom", "salary": 100},
#         {"name": "Mary", "salary": 300}
#     ]
# }

# 這題做完。

# 你會第一次開始真正操作：

# Dict[str, List[Dict]]

# 這種工作上超常見的資料結構。

# 我預估你會卡一下。

# 不是邏輯。

# 而是要適應：

# dict 裡放 list
# list 裡放 dict

# 到底長什麼樣。

# 這正是你剛剛提到的盲點，所以很適合現在練。🐍🚀