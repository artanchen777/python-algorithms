# 題目名稱
# group_anagrams.py

# 你先不要被名字嚇到。

# 這其實是：

# LeetCode 經典題
# 台積 HackerRank 可能出現的等級

# 但我已經把難度降到適合你目前的位置。

# 題目
from typing import List, Dict


def group_anagrams(words: List[str]) -> Dict[str, List[str]]:
    """
    將字母組成相同的單字分組

    Input:

    [
        "eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat"
    ]

    Output:

    {
        "aet": ["eat", "tea", "ate"],
        "ant": ["tan", "nat"],
        "abt": ["bat"]
    }

    說明：

    eat
    tea
    ate

    字母排序後都是：

    aet

    所以放同一組
    """
    # time : 15:22 ~ 15:26
    group_list = {}
    for w in words:
        sorted_w = ''.join(sorted(w))
        if sorted_w not in group_list:
            group_list[sorted_w] = [w]
        else:
            group_list[sorted_w].append(w)
    
    return group_list


if __name__ == "__main__":
    words = [
        "eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat"
    ]

    print(group_anagrams(words))
# 提示 1

# 你之前其實做過親戚題。

# 國泰筆試前我們有碰過：

# Group Anagrams

# 但那時候比較像背答案。

# 這次是自己寫。

# 提示 2

# 先思考：

# eat

# 如何變成：

# aet

# 提示：

# sorted("eat")

# 會得到：

# ['a', 'e', 't']
# 提示 3

# dict key 必須是：

# str

# 所以可能需要：

# ''.join(...)

# 例如：

# ''.join(sorted("eat"))

# 得到：

# "aet"
# 提示 4

# 這題本質其實是：

# group by

# 你熟悉的領域。

# 例如：

# {
#     "aet": ["eat", "tea", "ate"]
# }

# 其實很像：

# {
#     "RD": [Tom, Mary, John]
# }
# 本題目的

# 讓你第一次接觸：

# sorted(str)
# join()

# 以及：

# 字串轉換成可分組的 key

# 這是很多演算法題的核心技巧。

# 如果你寫到一半卡住。

# 不用硬想。

# 直接把目前版本貼上來。

# 這題我預期你會卡一下。

# 因為它不再是單純：

# 統計
# 排序
# Top K

# 而是開始碰：

# 資料轉換
# → 當作 key
# → group by

# 這是一個很值得跨過去的門檻。🐍🚀