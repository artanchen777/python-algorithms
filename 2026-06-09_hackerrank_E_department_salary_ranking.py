#  檔名
#  2026-06-09_hackerrank_E_department_salary_ranking.py
#  題目
from typing import List, Dict


def department_salary_ranking(data: List[Dict]) -> List[Dict]:
    """
    計算各部門總薪資並排序

    排序規則：

    1. 總薪資高的排前面
    2. 若總薪資相同，部門名稱字母小的排前面

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "IT", "salary": 400},
        {"dept": "HR", "salary": 400},
    ]

    Output:

    [
        {"dept": "HR", "salary": 400},
        {"dept": "IT", "salary": 400},
        {"dept": "RD", "salary": 400},
        {"dept": "QA", "salary": 200},
    ]

    說明：

    HR = 400
    IT = 400
    RD = 400
    QA = 200

    三個 400 同分

    所以依部門名稱排序：

    HR < IT < RD
    """
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
        
    sort_list = sorted(
        [
            {'dept' : dept, 'salary' : salary}
            for dept, salary in total.items()
        ], 
        key = lambda item: (-item['salary'], item['dept'])
    )
    
    return sort_list

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "IT", "salary": 400},
        {"dept": "HR", "salary": 400},
    ]

    print(department_salary_ranking(data))

#  難度
#  Platform : HackerRank
#  Level    : Easy
#  Tag       : Group By, List[Dict], Multi Sort
#  本題目的

#  今天你已經碰過：

#  key=lambda item: -item['salary']

#  這題第一次碰：

#  key=lambda item: (...)

#  也就是：

#  排序條件不只一個

#  提示到這裡就好。

#  如果卡住超過 5 分鐘再看提示。

#  因為這題的核心不是 Group By。

#  而是：

#  排序規則可以有多個