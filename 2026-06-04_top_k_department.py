# 這題開始有一點 HackerRank 味道。

# 但仍然是你熟悉的資料處理。

# 題目名稱：

# top_k_department.py

# 資料：

data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 500},
    {"dept": "C", "salary": 300},
    {"dept": "D", "salary": 700},
    {"dept": "E", "salary": 400},
]

# 請實作：

def top_k_department(data, k):
    # time : 16:14~16:19
    
    keep = {}
    
    # group by
    for i in data:
        d = i['dept']
        s = i['salary']
        keep[d] = keep.get(d, 0) + s

    my_list = []
    # to json
    for dept, salary in keep.items():
        my_list.append({'dept' : dept, 'salary' : salary})
    
    # order by desc
    my_list = sorted(my_list, key = lambda item: -item['salary'])
    
    my_list = my_list[:k]
    
    return my_list

print('\n----------------')
print(top_k_department(data, 3))
# 需求：

# Step1

# group by

# 得到：

# {
#     "A": 300,
#     "B": 500,
#     "C": 300,
#     "D": 700,
#     "E": 400
# }
# Step2

# 依 salary 由大到小排序

# Step3

# 只取前 k 名

# 例如：

# print(top_k_department(data, 3))

# 預期：

# [
#     {"dept": "D", "salary": 700},
#     {"dept": "B", "salary": 500},
#     {"dept": "E", "salary": 400},
# ]
# 提示

# 今天會自然碰到：

# sorted()

# 以及一個超重要的新東西：

# [:k]

# 這個東西在：

# LeetCode
# HackerRank
# Python面試

# 出現率非常高。

# 時間目標：

# 15分鐘內

# 這題如果你能獨立完成。

# 我會把你從：

# V9 Phase1

# 升到：

# V9 Phase1.5

# 因為已經開始接觸：

# Top K
# Sorting
# Ranking

# 這些中階題的基礎積木了。

# 來吧。