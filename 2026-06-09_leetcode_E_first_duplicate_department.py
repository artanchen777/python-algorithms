# 但我要開始偷渡真正的面試套路了。

# 你現在的狀態已經不是：

# dict.get 練習

# 了。

# 開始進入：

# Hash Set 反射
# 檔名
# 2026-06-09_leetcode_E_first_duplicate_department.py
# 題目
from typing import List, Dict


def first_duplicate_department(data: List[Dict]) -> str:
    """
    找出第一個重複出現的部門

    Input:

    [
        {"dept": "RD"},
        {"dept": "QA"},
        {"dept": "HR"},
        {"dept": "QA"},
        {"dept": "RD"},
    ]

    Output:

    "QA"

    說明：

    RD 第一次出現

    QA 第一次出現

    HR 第一次出現

    QA 再次出現

    因此回傳：

    "QA"
    """
    # time : 23:17~23:20
    seen = set()
    for d in data:
        if d['dept'] not in seen:
            seen.add(d['dept'])
        else:
            return d['dept']
    


if __name__ == "__main__":
    data = [
        {"dept": "RD"},
        {"dept": "QA"},
        {"dept": "HR"},
        {"dept": "QA"},
        {"dept": "RD"},
    ]

    print(first_duplicate_department(data))
# 難度
# Platform : LeetCode
# Level    : Easy
# Tag       : Hash Set, O(n)
# 為什麼出這題

# 其實你做過。

# 今天下午的：

# first_duplicate_word()

# 幾乎同一題。

# 但我要驗證的是：

# 看到：

# 第一個重複

# 你的大腦會不會直接出現：

# seen = set()

# 而不是：

# count = {}

# 這就是反射。

# 目標時間：

# 1~2 分鐘

# 如果超過 2 分鐘。

# 代表還沒母語化。

# 如果 30 秒就寫完。

# 代表這類 Hash Set 題型已經進腦了。