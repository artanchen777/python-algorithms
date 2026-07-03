# 檔名
# 2026-06-09_hackerrank_E_department_high_earner_count.py
# 題目
from typing import List, Dict


def department_high_earner_count(
    data: List[Dict],
    threshold: int
) -> Dict[str, int]:
    """
    計算每個部門薪資 >= threshold 的員工數量

    Input:

    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 600},
        {"dept": "HR", "salary": 250},
    ]

    threshold = 300

    Output:

    {
        "RD": 2,
        "QA": 1
    }

    說明：

    RD:
        300
        500

    QA:
        600

    HR:
        無符合條件

    所以不出現在結果中
    """
    result = {}
    # time : 23:09~23:11
    for d in data:
        dept, salary = d['dept'], d['salary']
        if salary >= threshold:
            result[dept] = result.get(dept, 0) + 1
    return result


if __name__ == "__main__":
    data = [
        {"dept": "RD", "salary": 100},
        {"dept": "RD", "salary": 300},
        {"dept": "RD", "salary": 500},
        {"dept": "QA", "salary": 200},
        {"dept": "QA", "salary": 600},
        {"dept": "HR", "salary": 250},
    ]

    print(
        department_high_earner_count(
            data,
            threshold=300
        )
    )
# 難度
# Platform : HackerRank
# Level    : Easy
# Tag       : Filter, Count, Dict
# 本題重點

# 今天的題目幾乎都是：

# for d in data:

# 就直接處理。

# 這題第一次出現：

# if salary >= threshold:

# 也就是：

# Filter
# ↓
# Aggregation

# 很像 SQL：

# select dept, count(*)
# from employee
# where salary >= 300
# group by dept

# 我想看你會不會自然想到：

# 先篩選
# 再統計

# 還是其實可以：

# 掃描時直接統計

# 這兩個思路。

# 記一下開始時間。

# 這題正常應該 2~5 分鐘。🐍🚀