# 檔名
# 2026-06-09_hackerrank_E_department_average_salary.py
# 題目
from typing import List, Dict


def department_average_salary(data: List[Dict]) -> List[Dict]:
    """
    計算各部門平均薪資

    並依平均薪資由高到低排序

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    [
        {"dept": "QA", "avg_salary": 300},
        {"dept": "HR", "avg_salary": 250},
        {"dept": "RD", "avg_salary": 200},
    ]

    說明：

    RD = (100 + 300) / 2 = 200

    QA = (200 + 400) / 2 = 300

    HR = 250 / 1 = 250

    依平均薪資由高到低排序
    """
    # time : 18:46 ~ 18:51
    m_sum = {}
    m_count = {}
    
    for d in data:
        dept, salary = d['dept'], d['salary']
        m_sum[dept] = m_sum.get(dept, 0) + salary
        m_count[dept] = m_count.get(dept, 0) + 1

    res = []
    for dept, salary in m_sum.items():
        res.append({
            'dept' : dept,
            'avg_salary' : salary / m_count[dept]
        })
    
    return sorted(
        res,
        key = lambda item : -item['avg_salary']
    )
if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    print(department_average_salary(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Group By, Aggregation, Sorting
# 為什麼出這題

# 你今天一直在做：

# sum
# max
# top k

# 這題第一次碰：

# sum + count

# 也就是：

# Aggregation

# 的另一種形式。

# 很像：

# avg(salary)
# group by dept

# 提示先不給。

# 我想看你會不會自然想到：

# 每個部門
# 需要維護兩個資訊

# 這個思路。

# 記一下開始時間，解完我們再 review。🐍🚀