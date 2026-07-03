# 檔名：

# department_employee_count.py

# 題目：

from typing import List, Dict

def department_employee_count(data: List[Dict]) -> Dict[str, int]:
    """
    計算每個部門有多少位不同員工

    Example:

    Input:
    [
        {"name": "Tom", "dept": "RD"},
        {"name": "Jack", "dept": "QA"},
        {"name": "Tom", "dept": "RD"},
        {"name": "Mary", "dept": "RD"},
    ]

    Output:
    {
        "RD": 2,
        "QA": 1
    }

    說明：
    RD 有 Tom、Mary
    QA 有 Jack
    """
    seen = {}
    # time : 00:14 ~ 00:18
    for d in data:
        name = d['name']
        dept = d['dept']
        if dept not in seen:
            seen[dept] = set()
        
        seen[dept].add(name)
    
    res = {}
    for dept in seen:
        res[dept] = len(seen[dept])
    
    return res

# 提示 1

# 這題和你剛剛 AC 的題目是親戚。

# 提示 2

# 我希望你用：

# dict[str, set]

# 來做。

# 提示 3

# 你可能會得到：

# {
#     "RD": {"Tom", "Mary"},
#     "QA": {"Jack"}
# }

# 之後呢？

# 想想今天早上學過的：

# len()

# 這題我預期：

# 5~10 分鐘