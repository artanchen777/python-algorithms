# 檔名
# 2026-06-09_hackerrank_E_department_highest_salary_employee.py
# 題目
from typing import List, Dict


def department_highest_salary_employee(data: List[Dict]) -> Dict[str, Dict]:
    """
    找出每個部門薪資最高的員工

    Input:

    [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 300},
        {"dept": "RD", "name": "Andy", "salary": 200},
        {"dept": "QA", "name": "Jack", "salary": 250},
        {"dept": "QA", "name": "John", "salary": 180},
    ]

    Output:

    {
        "RD": {
            "name": "Mary",
            "salary": 300
        },
        "QA": {
            "name": "Jack",
            "salary": 250
        }
    }

    說明：

    RD 最高薪是 Mary (300)

    QA 最高薪是 Jack (250)
    """
    # time : 11:14 ~ 11:21
    result = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        if dept not in result or salary > result[dept]['salary']:
            result[dept] = {
                'name' : name,
                'salary' : salary
            }
    return result

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 300},
        {"dept": "RD", "name": "Andy", "salary": 200},
        {"dept": "QA", "name": "Jack", "salary": 250},
        {"dept": "QA", "name": "John", "salary": 180},
    ]

    print(department_highest_salary_employee(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Dict, Group By, Max
# 本題重點

# 這次不要先 group 成：

# {
#     "RD": [
#         ...
#     ]
# }

# 再找最大。

# 試著思考：

# 我在掃描資料時
# 能不能直接維護目前最高薪的人？

# 這是很典型的：

# Single Pass

# 思維。

# 這題如果你抓到感覺。

# 會開始接近：

# 資料流(Data Flow)

# 而不是：

# 資料收集完再處理

# 的思考模式。