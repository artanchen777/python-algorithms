# 檔名：

# highest_salary_department.py

# 題目：

from typing import List, Dict

def highest_salary_department(data: List[Dict]) -> str:
    """
    找出總薪資最高的部門

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
    ]

    Output:

    "RD"

    因為：

    RD = 100 + 300 = 400
    QA = 200
    """
    # time : 07:20 ~ 07:22
    # group by and sum
    total = {}
    for i in data:
        dept, salary = i["dept"], i["salary"]
        total[dept] = total.get(dept, 0) + salary
    
    return max (
        total, 
        key = lambda dept: total[dept]
    )
    
    
    

# 範例

# data = [
#     {"dept": "RD", "salary": 100},
#     {"dept": "QA", "salary": 200},
#     {"dept": "RD", "salary": 300},
# ]

# 輸出

# "RD"

# 提示 1

# 這半題你做過。

# {
#     "RD": 400,
#     "QA": 200
# }

# 應該很快能得到。

# 提示 2

# 昨天你寫過：

# max_count = None
# max_dept = None

# 那種版本。

# 完全可以。

# 提示 3（進階）

# 如果你做完基本版。

# 再試著思考：

# return max(
#     ???,
#     key=???
# )

# 要怎麼寫。

# 今天目標不是學會 lambda。

# 而是：

# 看懂 lambda 在解決什麼問題

# 你先寫你最直覺的版本。