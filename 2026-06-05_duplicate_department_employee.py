# 題目：

from typing import List, Dict

data = [
        {"name": "Tom", "dept": "RD"},
        {"name": "Jack", "dept": "QA"},
        {"name": "Tom", "dept": "RD"},
        {"name": "Mary", "dept": "HR"},
]

def duplicate_department_employee(data: List[Dict]) -> List[str]:
    """
    找出有重複員工名稱的部門

    Input:

    [
        {"name": "Tom", "dept": "RD"},
        {"name": "Jack", "dept": "QA"},
        {"name": "Tom", "dept": "RD"},
        {"name": "Mary", "dept": "HR"},
    ]

    Output:

    ["RD"]

    因為 RD 裡面的 Tom 出現兩次
    """
    
    # 23:12 ~ 23:17(finish first version) ~ 23:22(debug)
    result = []
    keep = {}
    for employee in data:
        name = employee['name']
        dept = employee['dept']
        
        if dept not in keep:
            keep[dept] = set()
        
        if name in keep[dept]:
            result.append(dept)
        else:
            keep[dept].add(name)
    
    return result

print(duplicate_department_employee(data))
# 提示 1

# 這題一定會同時出現：

# dict
# set

# 提示 2

# 你可以想成：

# {
#     "RD": ?
#     "QA": ?
#     "HR": ?
# }

# 提示 3

# 每個部門裡面。

# 你需要知道：

# 有哪些人出現過

# 提示 4

# 今天真正想練的是：

# dict 裡面放 set

# 這是 Python 面試很常出現的組合。

# 看看你能不能自己設計出資料結構。