# 檔名：

# department_unique_employee.py
from typing import List, Dict


def department_unique_employee(data: List[Dict]) -> Dict[str, int]:
    """
    計算每個部門有多少位不重複員工

    Input:

    [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "Jack"},
    ]

    Output:

    {
        "RD": 2,
        "QA": 1
    }

    因為：

    RD -> Tom, Mary
    QA -> Jack
    """
    # time : 07:32 ~ 07:34(first version) ~ 07:37(debug)
    
    seen = {}
    for d in data:
        dept, name = d['dept'], d['name']
        if dept not in seen:
            seen[dept] = set()
        seen[dept].add(name)
    
    res = {}
    for dept, name in seen.items():
        res[dept] = len(seen[dept])
    
    return res


if __name__ == "__main__":
    data = [
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Tom"},
        {"dept": "RD", "name": "Mary"},
        {"dept": "QA", "name": "Jack"},
        {"dept": "QA", "name": "Jack"},
    ]

    print(department_unique_employee(data))
# 提示 1

# 你以前做過：

# {
#     "RD": 400,
#     "QA": 200
# }

# 這題會變成：

# {
#     "RD": {"Tom", "Mary"},
#     "QA": {"Jack"}
# }
# 提示 2

# 你前幾天有寫過很像的：

# keep[dept] = set()

# 那題找重複員工名稱的部門。

# 提示 3

# 最後別忘了：

# len(...)

# 這題如果是今天的你。

# 我預估：

# 2~4 分鐘

# 而且做完你會發現：

# dict 裡面放 set

# 其實跟：

# dict 裡面放 list

# 是同一個概念。