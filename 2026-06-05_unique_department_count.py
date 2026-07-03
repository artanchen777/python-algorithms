# 檔名：

# unique_department_count.py

# 題目：

from typing import List, Dict

def unique_department_count(employees: List[Dict]) -> int:
    """
    計算總共有幾個不同部門

    Example:

    Input:
    [
        {"name": "Tom", "dept": "RD"},
        {"name": "Jack", "dept": "QA"},
        {"name": "Mary", "dept": "RD"},
        {"name": "John", "dept": "HR"},
    ]

    Output:
    3
    """
    # time : 10:54 ~ 10:57
    seen = set()
    for employee in employees:
        seen.add(employee['dept']) # set 會自動去重複
    
    return len(seen)

# Input

# employees = [
#     {"name": "Tom", "dept": "RD"},
#     {"name": "Jack", "dept": "QA"},
#     {"name": "Mary", "dept": "RD"},
#     {"name": "John", "dept": "HR"},
# ]

# Output

# 3

# 提示 1

# 昨天我們在找：

# 重複的人

# 今天換成：

# 不同的部門

# 提示 2

# 你可能會很想寫：

# dept_count = {}

# 但先想一下：

# 題目真的需要：

# 次數

# 嗎？

# 還是只需要：

# 有哪些？

# 提示 3

# 最後答案其實只有：

# len(...)

# 這題我預期你 5 分鐘內能完成。

# 如果真的 5 分鐘 AC。

# 我下一題就開始偷偷導入：

# enumerate()

# 準備進入下一個工具。🐍🚀