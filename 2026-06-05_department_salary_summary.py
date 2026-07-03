# 檔名：

# department_salary_summary.py

# 題目：

from typing import List, Dict

def department_salary_summary(data: List[Dict]) -> Dict[str, int]:
    """
    將員工薪資依部門加總

    Example:

    Input:
    [
        {"name": "Tom", "dept": "RD", "salary": 100},
        {"name": "Jack", "dept": "QA", "salary": 200},
        {"name": "Mary", "dept": "RD", "salary": 300},
    ]

    Output:
    {
        "RD": 400,
        "QA": 200
    }
    """
    
    # time : 22:53~22:54
    
    keep = {}
    for user in data:
        dept = user['dept']
        salary = user['salary']
        keep[dept] = keep.get(dept, 0) + salary
        
    return keep

# Input

data = [
    {"name": "Tom", "dept": "RD", "salary": 100},
    {"name": "Jack", "dept": "QA", "salary": 200},
    {"name": "Mary", "dept": "RD", "salary": 300},
]

# Output

# {
#     "RD": 400,
#     "QA": 200
# }

# 提示 1

# 這題你其實做過類似的。

# 提示 2

# 關鍵字：

# group by
# sum

# 提示 3

# 如果看到：

# GROUP BY dept
# SUM(salary)

# 你會想到什麼？

# 提示 4

# 今天我想看的是：

# dict.get()

# 有沒有真的開始變成肌肉記憶。

# 這題不是考你。

# 而是熱身。

# 因為如果你 3 分鐘 AC。

# 下一題我準備出一個：

# dict + set

# 一起出現的題目。

# 那才是今天真正的主菜。🐍🔥

# 貼程式就好，我來 review。