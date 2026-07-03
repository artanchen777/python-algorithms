# 檔名
# 2026-06-09_hackerrank_department_employee_names.py
# 題目
from typing import List, Dict


def department_employee_names(data: List[Dict]) -> Dict[str, List[str]]:
    """
    將員工依部門分組，並依名字排序

    Input:

    [
        {"dept": "RD", "name": "Tom"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "RD", "name": "Andy"},
    ]

    Output:

    {
        "RD": ["Andy", "Mary", "Tom"],
        "QA": ["Jack"]
    }

    說明：

    RD 部門有：

    Tom
    Mary
    Andy

    排序後：

    Andy
    Mary
    Tom
    """
    # time: 10:16~10:23
    group = {}
    for d in data:
        dept, name = d['dept'], d['name']
        if dept not in group:
            group[dept] = set()
        group[dept].add(name)
        
    res = {}
    for dept_key, names in group.items():
        res[dept_key] = sorted(list(names))
    
    return res

if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "RD", "name": "Andy"},
    ]

    print(department_employee_names(data))
# 本題重點

# 第一次正式練：

# dict[str, list]

# 例如：

# {
#     "RD": ["Tom", "Mary", "Andy"],
#     "QA": ["Jack"]
# }

# 以及：

# append()

# 跟：

# sorted()

# 或：

# .sort()
# 預期時間

# 以你昨天的狀態來看：

# 3~5 分鐘

# 應該能完成。