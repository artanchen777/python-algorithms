# 1. 檔名
# 2026-06-14_01_backend_M_department_top_earner.py
# 2. Input
# data = [
#     {"dept": "A", "name": "Tom", "salary": 100},
#     {"dept": "A", "name": "Mary", "salary": 300},
#     {"dept": "A", "name": "Jack", "salary": 300},
#     {"dept": "B", "name": "Amy", "salary": 200},
#     {"dept": "B", "name": "John", "salary": 500},
# ]
# 3. Output
# [
#     {"dept": "A", "name": "Jack", "salary": 300},
#     {"dept": "B", "name": "John", "salary": 500},
# ]
# 4. 難度資訊 + 練習重點
# 難度：M

# 練習重點：
# - dict
# - 條件更新
# - 多條件比較
# - sorted
# - lambda
# 5. 題目目標、要求、限制
# 請找出每個部門薪資最高的員工。

# 若同部門有多人薪資相同：

# 保留名字字母排序較前面的員工。

# 回傳格式為 list[dict]。

# 最終結果依 dept 升冪排序。

# 不可使用 pandas。
# 6. 完整可執行範本
from typing import List

data = [
    {"dept": "A", "name": "Tom", "salary": 100},
    {"dept": "A", "name": "Mary", "salary": 300},
    {"dept": "A", "name": "Jack", "salary": 300},
    {"dept": "B", "name": "Amy", "salary": 200},
    {"dept": "B", "name": "John", "salary": 500},
]

def department_top_earner(data: List[dict]) -> List[dict]:
    # time : 09:30 ~ 09:46(first version and failed), 09:47(2rd round)~10:00(AC)
    summary = {}
    for d in data:
        dept, name, salary = d['dept'], d['name'], d['salary']
        summary.setdefault(dept, [])
        summary[dept].append({"name": name, "salary": salary})
    
    # sort the salary and name for every dept
    for dept in summary:
        summary[dept] = sorted(
            summary[dept],
            key = lambda item : (-item['salary'], item['name'])
        )[0] # [0] is for remove list to dict only
        
    
    return [
        {'dept' : dept, **info}
        for dept, info in sorted(
            summary.items(),
            key = lambda item: item[0]
        )
    ]

print(department_top_earner(data))
# 7. 不要含冗長提示

# 這題開始進入你現在剛好需要的區域：

# 資料結構仍然熟悉

# 但需要開始思考

# 「如果出現平手怎麼辦」

# 這就是從母語化往演算法思維跨出的第一步。