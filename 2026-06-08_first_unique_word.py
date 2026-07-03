# 檔名：

# first_unique_word.py
# from typing import List


def first_unique_word(words: List[str]) -> str:
    """
    找出第一個只出現一次的單字

    Input:

    [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "kiwi"
    ]

    Output:

    "orange"

    因為：

    apple  出現 2 次
    banana 出現 2 次
    orange 出現 1 次
    kiwi   出現 1 次

    而 orange 是第一個只出現一次的單字
    """
    # time : 15:08 ~ 15:11
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
        
    for s in words:
        if counter[s] == 1:
            return s
        
    return ''


if __name__ == "__main__":
    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "kiwi"
    ]

    print(first_unique_word(words))
# 提示 1

# 你一定會先得到：

# {
#     "apple": 2,
#     "banana": 2,
#     "orange": 1,
#     "kiwi": 1
# }
# 提示 2

# 這題不要急著用：

# sorted()
# max()
# 提示 3

# 題目在意的是：

# 第一個

# 不是：

# 字典序
# 次數最高
# 思考方向

# 先統計：

# count[word]

# 再回頭看原始：

# words

# 找第一個：

# count[word] == 1

# 的單字。

# 這題做完。

# 今天就真的可以收工了。

# 因為這題開始有一點：

# 統計
# +
# 保留原始順序

# 的味道。

# 這是 HackerRank 很常出的套路。🐍🚀