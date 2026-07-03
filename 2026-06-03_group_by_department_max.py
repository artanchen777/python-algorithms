# 題目
data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 300},
    {"dept": "C", "salary": 300},
    {"dept": "C", "salary": -200},
]

# 請實作：

def find_max_dept(data):
    # 23:52 ~ 11:59
    
    keep = {}
    
    # group by and sum
    for obj in data:
        dept = obj['dept']
        salary = obj['salary']
        keep[dept] = keep.get(dept, 0) + salary
    
    # find max
    max_value = None
    max_dept = None
    for key, value in keep.items():
        if max_value is None or value > max_value:
            max_value = value
            max_dept = key

    return {
        "dept": max_dept,
        "total_salary": max_value
    }

# 需求：

# 1. 依 dept group by
# 2. 計算每個 dept 的 salary sum
# 3. 回傳 salary sum 最大的 dept

# 預期：

print(find_max_dept(data))

# "A"

# 因為：

# A = 300
# B = 300
# C = 100

# 如果同分：

# 先出現的部門優先

# 所以：

# A
# Phase

# 這題我會歸在：

# V9 Python Phase 1

# 原因：

# dict
# for
# group by
# 累加

# 都是 Backend 基本功。

# 額外挑戰（可跳過）

# 如果你 5 分鐘就寫完。

# 再做第二版：

# return {
#     "dept": "A",
#     "total_salary": 300
# }