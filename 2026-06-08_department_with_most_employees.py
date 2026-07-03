# 檔名：

# department_with_most_employees.py

# 題目：

from typing import List, Dict

def department_with_most_employees(data: List[Dict]) -> str:
    """
    找出員工數最多的部門

    Input:

    [
        {"name": "Tom", "dept": "RD"},
        {"name": "Jack", "dept": "QA"},
        {"name": "Mary", "dept": "RD"},
        {"name": "John", "dept": "RD"},
    ]

    Output:

    "RD"
    """
    # time 12:20 ~ 12:24
    seen = {}
    for d in data:
        name = d['name']
        dept = d['dept']
        seen[dept] = seen.get(dept, 0) + 1 # 假設員工不重複
    
    max_count = None
    max_dept = None
    for dept, count in seen.items():
        if max_count is None or count > max_count:
            max_count = count
            max_dept = dept
    
    return {'max_dept' : max_dept, 'count' : max_count}

# Input

data = [
    {"name": "Tom", "dept": "RD"},
    {"name": "Jack", "dept": "QA"},
    {"name": "Mary", "dept": "RD"},
    {"name": "John", "dept": "RD"},
]
print('\n-------------------')
print(department_with_most_employees(data))

# Output

# "RD"

# 提示 1

# 這題其實跟你剛剛那題是親戚。

# 提示 2

# 你可能先得到：

# {
#     "RD": 3,
#     "QA": 1
# }

# 提示 3

# 之後要回答：

# 誰最大？

# 提示 4

# 先不要想什麼 fancy 寫法。

# 直接：

# for dept, count in ...

# 一路掃過去就好。

# 這題的目標不是新觀念。

# 而是讓：

# dict
# set
# len
# items