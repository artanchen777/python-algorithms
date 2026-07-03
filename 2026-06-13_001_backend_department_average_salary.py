# 檔名
# 2026-06-13_001_backend_department_average_salary.py
# Input
# data = [
#     {"dept": "A", "salary": 100},
#     {"dept": "A", "salary": 200},
#     {"dept": "B", "salary": 300},
#     {"dept": "C", "salary": 300},
#     {"dept": "C", "salary": -200},
# ]
# Output
# [
#     {"dept": "B", "avg_salary": 300.0},
#     {"dept": "A", "avg_salary": 150.0},
#     {"dept": "C", "avg_salary": 50.0},
# ]
# 難度
# ★★★☆☆
# Phase 1
# 題目要求
# 1. 依 dept 分組
# 2. 計算平均薪資
# 3. 回傳 list[dict]
# 4. 依 avg_salary DESC 排序
# 5. 若 avg_salary 相同，dept ASC 排序
# 6. 禁止使用：
#    - collections
#    - pandas
#    - numpy
#    - itertools
# 7. 僅可使用：
#    - dict
#    - list
#    - for
#    - if
#    - sorted
# 範本
# # time :

data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 300},
    {"dept": "C", "salary": 300},
    {"dept": "C", "salary": -200},
]

def department_average_salary(data: list[dict]) -> list[dict]:
    summary = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        summary.setdefault(dept, {'count' : 0, 'total' : 0})
        summary[dept]['count'] += 1
        summary[dept]['total'] += salary
        
    return [
        {'dept' : dept, 'avg_salary' : info['total'] / info['count']}
        for dept, info in sorted(
            summary.items(),
            key = lambda item : (-item[1]['total'] / item[1]['count'], item[0])
        )
    ]
    

print(department_average_salary(data))

# 這樣比較像真正的 HackerRank / 公司筆試格式。