# 1. 檔名
# 2026-06-10_backend_Eplus_department_top_salary_employee.py
# 2. Input
# data = [
#     {"dept": "RD", "name": "Tom", "salary": 100},
#     {"dept": "RD", "name": "Mary", "salary": 500},
#     {"dept": "RD", "name": "John", "salary": 300},

#     {"dept": "QA", "name": "Jack", "salary": 400},
#     {"dept": "QA", "name": "Amy", "salary": 200},

#     {"dept": "HR", "name": "David", "salary": 350},
# ]
# 3. Output
# [
#     {
#         "dept": "RD",
#         "name": "Mary",
#         "salary": 500
#     },
#     {
#         "dept": "QA",
#         "name": "Jack",
#         "salary": 400
#     },
#     {
#         "dept": "HR",
#         "name": "David",
#         "salary": 350
#     }
# ]
# 4. 難度資訊
# Platform : Backend
# Level    : Easy+
# Tag      : Group By, Max, Nested Dict
# 練習重點
# 1. 維護最大值
# 2. 同時保留關聯資料
# 3. Dict[Dict]
# 4. Aggregate Record
# 5. 題目要求
# 找出每個部門薪資最高的員工

# 輸出：

# {
#     "dept": 部門,
#     "name": 員工姓名,
#     "salary": 最高薪資
# }

# 輸出順序不限
# 6. 完整可執行範本
from typing import List, Dict


def department_top_salary_employee(
    data: List[Dict]
) -> List[Dict]:
    # time : 22:39 ~ 22:47
    
    find_max = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        find_max.setdefault(dept, {'name' : None, 'salary' : float('-inf')})
        if salary > find_max[dept]['salary']:
            # 標準寫法
            # find_max[dept]['name'], find_max[dept]['salary'] = name, salary
            
            # 進階寫法
            find_max[dept] = {
                'name' : name,
                'salary' : salary
            }
    return [
        {'dept' : dept, 'name' : find_max[dept]['name'], 'salary' : find_max[dept]['salary']}
        for dept in find_max
    ]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom", "salary": 100},
        {"dept": "RD", "name": "Mary", "salary": 500},
        {"dept": "RD", "name": "John", "salary": 300},

        {"dept": "QA", "name": "Jack", "salary": 400},
        {"dept": "QA", "name": "Amy", "salary": 200},

        {"dept": "HR", "name": "David", "salary": 350},
    ]

    print(
        department_top_salary_employee(data)
    )

# 這題開始有一點：

# 最高薪資
# +
# 關聯資料一起保留

# 的味道。

# 以前你會維護：

# find_max[dept] = salary

# 這次會發現：

# 光存 salary 不夠

# 因為最後還要知道：

# 是誰

# 這就是 Backend 報表題很常見的進階點。

# 第 14 題，開始。🐍🚀