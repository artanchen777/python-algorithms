# 我準備開始埋一顆真正 LeetCode Easy 的種子。

# 但我會用你熟悉的商業資料包裝。

# 檔名
# 2026-06-09_hackerrank_E_top_k_departments.py
# 題目
# from typing import List, Dict


def top_k_departments(
    data: List[Dict],
    k: int
) -> List[str]:
    """
    找出總薪資最高的前 k 個部門

    Input:

    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
        {"dept": "IT", "salary": 100},
    ]

    k = 2

    Output:

    ["IT", "RD"]

    說明：

    RD = 400
    QA = 200
    HR = 250
    IT = 600

    排序後：

    IT = 600
    RD = 400
    HR = 250
    QA = 200

    取前 2 名
    """
    # time : 23:13~23:15
    total = {}
    for d in data:
        dept, salary = d['dept'], d['salary']
        total[dept] = total.get(dept, 0) + salary
    return sorted(
        total,
        key = lambda dept: -total[dept]
    )[:k]


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "QA", "salary": 200},
        {"dept": "RD", "salary": 300},
        {"dept": "HR", "salary": 250},
        {"dept": "IT", "salary": 500},
        {"dept": "IT", "salary": 100},
    ]

    print(top_k_departments(data, 2))
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Top K, Group By, Sorting
# 為什麼出這題

# 你今天其實已經做過：

# top_two_departments()

# 但那是固定：

# [:2]

# 這題變成：

# [:k]

# 看起來只差一個字母。

# 但這其實是：

# 固定需求
# ↓
# 參數化需求

# 的轉換。

# 而且未來你碰到：

# Top K Frequent Words
# Top K Frequent Elements

# 幾乎都是這個套路。

# 我先不給提示。

# 因為我覺得以你今天的狀態：

# 2~4 分鐘

# 應該能直接秒掉。

# 記一下開始時間。🐍🚀