# 檔名：

# 2026-06-13_002_backend_department_top_employee.py

# Input

# data = [
#     {"dept": "A", "name": "Tom", "salary": 100},
#     {"dept": "A", "name": "Jack", "salary": 300},
#     {"dept": "A", "name": "Mary", "salary": 200},
#     {"dept": "B", "name": "John", "salary": 500},
#     {"dept": "B", "name": "Amy", "salary": 400},
# ]

# Output

# [
#     {"dept": "A", "name": "Jack", "salary": 300},
#     {"dept": "B", "name": "John", "salary": 500},
# ]

# 難度

# Phase 1 ~ Phase 2 交界

# 重點：
# dict
# group by
# 比較大小
# 資料保留

# 題目要求

# 找出每個部門薪資最高的員工

# 回傳 list[dict]

# 依 dept ASC 排序

# 禁止使用 max()
# 禁止先把資料排序後再取第一筆

# 必須自己在迴圈中維護目前最高薪員工

# 完整範本

# # time : 21:13 ~ 21:18

data = [
    {"dept": "A", "name": "Tom", "salary": 100},
    {"dept": "A", "name": "Jack", "salary": 300},
    {"dept": "A", "name": "Mary", "salary": 200},
    {"dept": "B", "name": "John", "salary": 500},
    {"dept": "B", "name": "Amy", "salary": 400},
]


def department_top_employee(data: list[dict]) -> list[dict]:
    find_max = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        find_max.setdefault(dept, {'name' : '', 'salary' : float('-inf')})
        if salary > find_max[dept]['salary']:
            find_max[dept] = {'name' : name, 'salary' : salary}
            
    return [
        {'dept' : dept, **info}
        for dept, info in sorted(find_max.items())
    ]
    


print(department_top_employee(data))

# 這題是故意出的。

# 因為你前面幾題都在累積：

# group by
# ↓
# count
# ↓
# sum
# ↓
# avg

# 現在開始進入：

# group by
# ↓
# 保留最佳紀錄

# 這是資料工程非常常見的模式。

# 做完貼上來，我看你有沒有真正掌握「group by + state maintenance（狀態維護）」的核心。