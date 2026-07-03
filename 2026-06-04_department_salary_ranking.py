# 題目名稱
# department_salary_ranking.py
# Phase
# V9 Phase 1.5
# (HashMap + Sorting)
# 題目
data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 300},
    {"dept": "C", "salary": 300},
    {"dept": "C", "salary": -200},
]

# 請實作：

def department_salary_ranking(data):
    
    keep = {}
    
    # sum
    for obj in data:
        dept = obj['dept']
        salary = obj['salary']
        keep[dept] = keep.get(dept, 0) + salary
    
    my_list = []
    
    # zip
    for key, value in keep.items():
        my_list.append({'dept' : key, 'salary' : value})
    
    # 寫法1
    # my_list = sorted(
    #     my_list,
    #     key = lambda item: item['salary'], # order by salary DESC, dept
    #     reverse = True
    # )
    
    # 寫法2
    my_list = sorted(
        my_list,
        key = lambda item: (-item['salary'], item['dept'])
    )
    
    
    return my_list

print('\n----------------')
print(department_salary_ranking(data))

# 需求
# Step 1

# group by dept

# A = 300
# B = 300
# C = 100
# Step 2

# 轉成

# [
#     {"dept": "A", "total_salary": 300},
#     {"dept": "B", "total_salary": 300},
#     {"dept": "C", "total_salary": 100},
# ]
# Step 3

# 依照

# total_salary

# 由大到小排序

# 預期結果
# [
#     {"dept": "A", "total_salary": 300},
#     {"dept": "B", "total_salary": 300},
#     {"dept": "C", "total_salary": 100},
# ]
# 額外挑戰

# 如果：

# data = [
#     {"dept": "A", "salary": 100},
#     {"dept": "A", "salary": 200},
#     {"dept": "B", "salary": 500},
#     {"dept": "C", "salary": 300},
# ]

# 結果要變：

# [
#     {"dept": "B", "total_salary": 500},
#     {"dept": "A", "total_salary": 300},
#     {"dept": "C", "total_salary": 300},
# ]
# 提示

# 今天故意讓你碰這個：

# sorted(...)

# 但先不要查。

# 先憑感覺寫。

# 寫到卡住為止。

# 我想看你目前對排序的直覺是什麼。

# 目標時間：

# 15 分鐘

# 完成度比漂亮度重要。

# 寫完直接貼上來。

# 今天開始把：

# dict
# list
# group by

# 接到下一個常用武器：

# sorting