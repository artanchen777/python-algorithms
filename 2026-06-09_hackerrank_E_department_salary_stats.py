# 檔名
# 2026-06-09_hackerrank_E_department_salary_stats.py
# 題目
from typing import List, Dict


def department_salary_stats(data: List[Dict]) -> Dict[str, Dict]:
    """
    計算各部門薪資統計

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 200},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    {
        "RD": {
            "count": 3,
            "total": 600,
            "max_salary": 300
        },
        "QA": {
            "count": 2,
            "total": 600,
            "max_salary": 400
        },
        "HR": {
            "count": 1,
            "total": 250,
            "max_salary": 250
        }
    }

    說明：

    RD:
        count = 3
        total = 600
        max_salary = 300

    QA:
        count = 2
        total = 600
        max_salary = 400

    HR:
        count = 1
        total = 250
        max_salary = 250
    """
    # time : 22:58 ~ 23:02
    res = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        if dept not in res:
            res[dept] = {}
        res[dept]['count'] = res[dept].get('count', 0) + 1
        res[dept]['total'] = res[dept].get('total', 0) + salary
        res[dept]['max_salary'] = max(res[dept].get('max_salary', 0), salary)
    
    return res


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 200},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    print(department_salary_stats(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Nested Dict, Aggregation, Max Tracking
# 這題的目的

# 今天最後一題，我想看你能不能做到：

# 一個 Dict
# 同時維護

# count
# total
# max_salary

# 而不是拆成：

# m_count
# m_total
# m_max

# 三份資料。

# 這題很像今天下午那題：

# department_highest_salary_employee

# 的概念。

# 只是把：

# 最高薪

# 和

# 統計資訊

# 融合在一起。

# 我預估如果今天的東西有吸收進去：

# 3~6 分鐘

# 應該能解掉。