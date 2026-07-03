# 檔名：

# departments_by_salary.py

# 題目：

from typing import List, Dict
def group_by_salary(data: List[Dict]) -> Dict:
    res = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        res[dept] = res.get(dept, 0) + salary
    
    return res

def departments_by_salary(data: List[Dict]) -> List[str]:
    """
    依照部門總薪資由小到大排序

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    ["QA", "HR", "RD"]

    因為：

    QA = 200
    HR = 250
    RD = 400
    """
    total = group_by_salary(data)
    
    return sorted(
        total,
        key = lambda dept : total[dept]
    )

# 提示 1

# 第一步你一定會得到：

# {
#     "RD": 400,
#     "QA": 200,
#     "HR": 250
# }

# 提示 2

# 昨天你已經寫過：

# max(
#     total,
#     key=lambda dept: total[dept]
# )

# 今天只是把：

# max(...)

# 換成：

# sorted(...)

# 提示 3

# 我希望你先直接嘗試。

# 不要 Google。

# 不要查語法。

# 憑昨天的理解寫。

# 就算錯也沒關係。

# 因為這題的目的就是：

# 把 max(key=...)
# 映射成
# sorted(key=...)

# 時間目標：

# 5~10 分鐘

# 貼程式即可，我來 review。