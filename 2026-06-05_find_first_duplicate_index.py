# 今天開始偷偷導入：

# enumerate()

# 但我不會先教。

# 先讓你感受到：

# 為什麼會需要它。

# 檔名：

# find_first_duplicate_index.py

# 題目：

from typing import List

def find_first_duplicate_index(users: List[str]) -> int:
    """
    找出第一個重複出現的使用者索引

    Example:

    Input:
        ["tom", "jack", "mary", "tom"]

    Output:
        3

    因為 users[3] == "tom"
    且 tom 曾經出現過
    """
    # 11:26 ~ 11:27
    seen = set()
    for index, name in enumerate(users):
        if name in seen:
            return index
        seen.add(name)
    
    return -1

# 範例 1

# users = [
#     "tom",
#     "jack",
#     "mary",
#     "tom"
# ]

# 輸出：

# 3

# 範例 2

# users = [
#     "tom",
#     "jack",
#     "mary"
# ]

# 輸出：

# -1

# 提示 1

# 昨天的題目：

# if user in seen:

# 幾乎可以直接沿用。

# 提示 2

# 這次除了 user。

# 你還需要：

# 目前位置

# 提示 3

# 你一定可以先這樣寫：

# for user in users:

# 但你很快會發現：

# 我不知道自己現在在第幾格

# 提示 4（關鍵）

# Python 有個東西專門解決：

# 元素 + 索引
# 一起拿

# 叫做：

# enumerate()

# 如果想不起來怎麼用也沒關係。

# 你先寫。

# 卡住我再補。

# 這題其實是幫未來的：

# Two Sum

# 鋪路。🐍🚀