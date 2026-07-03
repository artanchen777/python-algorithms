# 題目名稱
# employee_salary_filter.py
# Phase
# V9 Phase 1
# (HashMap / Group By / Filtering)
# 題目
data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 300},
    {"dept": "C", "salary": 300},
    {"dept": "C", "salary": -200},
]

# 請實作：

def group_by_dept(data):
    
    keep = {}
    res = []
    # group by
    for obj in data:
        dept = obj['dept']
        salary = obj['salary']
        keep[dept] = keep.get(dept, 0) + salary
    
    # where codition
    
    for dept, salary in keep.items():
        if salary > 200:
            res.append({'dept' : dept, 'salary' : salary})
    
    return res
print('\n-------------')
print(group_by_dept(data))
# 需求
# 1. group by dept

# 2. 計算每個 dept 的 salary sum

# 3. 只保留 salary sum > 200 的部門

# 4. 回傳 dict
# 預期結果
# {
#     "A": 300,
#     "B": 300
# }

# 因為：

# A = 300
# B = 300
# C = 100
# 限制

# 先不要用：

# defaultdict
# Counter
# pandas

# 只用：

# dict
# for
# if
# get
# 額外挑戰（完成再做）

# 改成：

# [
#     {"dept": "A", "total_salary": 300},
#     {"dept": "B", "total_salary": 300},
# ]
# 為什麼出這題？

# 因為這題其實就是昨天那題的延伸。

# 昨天你練了：

# group by
# sum
# max

# 今天變成：

# group by
# sum
# filter

# 這是 Backend 最常見的資料處理套路。

# 時間目標：

# 10~15 分鐘

# 不要查資料。

# 不要追求漂亮。

# 直接寫。