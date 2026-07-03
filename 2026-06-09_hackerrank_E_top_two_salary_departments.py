# 檔名
# 2026-06-09_hackerrank_E_top_two_salary_departments.py
# 題目
from typing import List, Dict


def top_two_salary_departments(data: List[Dict]) -> List[Dict]:
    """
    找出總薪資最高的前兩個部門

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
    ]

    Output:

    [
        {"dept": "IT", "salary": 500},
        {"dept": "RD", "salary": 400}
    ]

    說明：

    IT = 500
    RD = 400
    HR = 250
    QA = 200

    只取前兩名
    """
    total = {}
    # time : 14:30~14:33
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    mylist = [
        {
            'dept' : dept,
            'salary' : salary
        }
        for dept, salary in total.items()
    ]
    
    return sorted(
        mylist,
        key = lambda items: -items['salary']
    )[:2]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
    ]

    print(top_two_salary_departments(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Group By, Sorting, Top K, List[Dict]
# 為什麼出這題

# 因為你今天上午已經做過：

# department_total_salary_sorted()

# 那題是：

# Group By
# ↓
# 排序
# ↓
# 全部回傳

# 這題變成：

# Group By
# ↓
# 排序
# ↓
# 取前2名

# 我想看你會不會自然想到：

# [:2]

# 以及：

# List[Dict]

# 的組裝。

# 預估：

# 3~6 分鐘

# 這題如果順手解掉，代表你上午那幾題真的吸收進去了。🐍🚀