# 題目：top_salary_department.py

# 主題：

# group by
# sum
# max
# lambda

# 這題是剛剛那題的兄弟題。

from typing import List, Dict


def top_salary_department(data: List[Dict]) -> Dict:
    """
    找出總薪資最高的部門與薪資

    Input:

    [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
    ]

    Output:

    {
        "dept": "RD",
        "salary": 400
    }

    因為：

    RD = 400
    QA = 200
    HR = 250
    """
    
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary

    max_dept = max(
        total,
        key = lambda dept: total[dept]
    )
    
    max_salary = total[max_dept]
    
    return {
        'dept' : max_dept,
        'salary' : max_salary
    }

if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
    ]

    print(top_salary_department(data))
# 提示 1

# 第一步你應該很熟：

# {
#     "RD": 400,
#     "QA": 200,
#     "HR": 250
# }
# 提示 2

# 這次不要自己維護：

# max_count
# max_dept

# 試著用：

# max(...)

# 來做。

# 提示 3

# 昨天我們討論過：

# max(total.items(), ...)

# 裡面的：

# item

# 其實長這樣：

# ("RD", 400)

# 思考：

# item[0]

# 是什麼？

# item[1]

# 又是什麼？

# 預期學習點

# 這題不是練 group by。

# 你已經會了。

# 真正目的是第一次練：

# max(
#     total.items(),
#     key=lambda item: item[1]
# )

# 這個面試超常出現的寫法。

# 預估時間：

# 5~10 分鐘

# 做完貼上來，我帶你拆解 items() + tuple + lambda 三個東西是怎麼串起來的。