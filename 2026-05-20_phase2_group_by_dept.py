data = [
    {"dept": "A", "salary": 100},
    {"dept": "A", "salary": 200},
    {"dept": "B", "salary": 300},
    {"dept": "C", "salary": 300},
    {"dept": "C", "salary": -200},
]

# 請用 Python 實現：

# group by dept
# 求 sum
# 只保留 sum > 200 的部門


def group_by_dept(data: List[dict]) -> List[dict]:
    temp = {}
    result = {}

    for row in data:
        dept = row['dept']
    
        if dept not in temp:
            temp[dept] = 0
            
        temp[dept] += row['salary']
        
    for dept, salary in temp.items():
        if salary > 200:
            result[dept] = salary
    
    return result

print(group_by_dept(data))