# 檔名：

# top_two_departments.py
from typing import List, Dict


def top_two_departments(data: List[Dict]) -> List[str]:
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

    ["IT", "RD"]

    因為：

    IT = 500
    RD = 400
    HR = 250
    QA = 200
    """
    # time : 10:46 ~ 10:49
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    
    sort_list = sorted(
        total,
        key = lambda dept: -total[dept], 
    )
    
    return sort_list[:2]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
    ]

    print(top_two_departments(data))
    
# 提示 1

# 先得到：

# {
#     "RD": 400,
#     "QA": 200,
#     "HR": 250,
#     "IT": 500
# }
# 提示 2

# 想想：

# 我要一個最大值

# 通常用：

# max(...)

# 但現在是：

# 我要前兩名

# 所以：

# max(...)

# 是不是開始有點不夠用了？

# 提示 3

# 昨天我們討論過：

# sorted(
#     total,
#     key=lambda dept: total[dept]
# )

# 會得到：

# ["QA", "HR", "RD", "IT"]

# 那如果想拿前兩名呢？

# 本題學習點

# 第一次讓你感受到：

# max 適合找冠軍

# sorted 適合排名

# 這個差異。

# 預估：

# 5 分鐘左右

# 這題如果順利，你對：

# sorted(..., key=...)

# 的理解會大幅提升。🐍🚀