# 題目：second_highest_salary_department.py

# 主題：

# group by
# sorted
# tuple
# items()

from typing import List, Dict


def second_highest_salary_department(data: List[Dict]) -> Dict:
    """
    找出總薪資第二高的部門

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
    ]

    Output:

    {
        "dept": "RD",
        "salary": 400
    }

    排名：

    IT = 500
    RD = 400
    HR = 250
    QA = 200

    所以第二名是 RD
    """
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    
    dept, salary = sorted(
        total.items(),
        key = lambda item: -item[1]
    )[1]
    
    return {
        'dept' : dept,
        'salary' : salary
    }
    

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
    ]

    print(second_highest_salary_department(data))
    
    
# 提示 1

# 先得到：

# {
#     "RD": 400,
#     "QA": 200,
#     "HR": 250,
#     "IT": 500
# }
# 提示 2

# 這次我希望你試著用：

# total.items()

# 而不是：

# total
# 提示 3

# 你可以先印看看：

# print(total.items())

# 看看它長什麼樣。

# 提示 4

# 你最近剛學會：

# sorted(...)[0]
# sorted(...)[1]
# sorted(...)[ :2 ]

# 這題剛好用得到。

# 本題目的

# 不是第二名。

# 而是讓你親手看到：

# sorted(
#     total.items(),
#     key=lambda item: item[1]
# )

# 時，

# item

# 到底是不是你腦中想的：

# ("RD", 400)

# 預估：

# 5~8 分鐘

# 這題做完，我們就可以開始慢慢脫離薪資部門題，進入字串與陣列了。🐍🚀