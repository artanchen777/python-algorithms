# 檔名
# 2026-06-09_hackerrank_E_department_salary_summary.py
# 題目
from typing import List, Dict


def department_salary_summary(data: List[Dict]) -> Dict[str, Dict]:
    """
    計算各部門薪資摘要

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    {
        "RD": {
            "count": 2,
            "total": 400
        },
        "QA": {
            "count": 2,
            "total": 600
        },
        "HR": {
            "count": 1,
            "total": 250
        }
    }

    說明：

    RD 有 2 人
    RD 總薪資 400

    QA 有 2 人
    QA 總薪資 600

    HR 有 1 人
    HR 總薪資 250
    """
    res = {}
    # time : 20:09 ~ 22:12
    for d in data:
        dept, salary = d['dept'], d['salary']
        if dept not in res:
            res[dept] = {'total' : 0, 'count' : 0}
        res[dept]['total'] += salary
        res[dept]['count'] += 1
    
    return res


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 400},
        {"dept": "HR", "salary": 250},
    ]

    print(department_salary_summary(data))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Dict, Nested Dict, Aggregation
# 我想看的點

# 這題沒有排序。

# 沒有 Top K。

# 沒有 List[Dict]。

# 故意回到：

# Dict[str, Dict]

# 我想看你會不會直接想到：

# {
#     dept: {
#         "count": ?,
#         "total": ?
#     }
# }

# 而不是再拆：

# m_count = {}
# m_total = {}

# 因為這題很像真實 API response。

# 記一下時間。

# 我預估你應該能在 3~5 分鐘內完成。🐍🚀