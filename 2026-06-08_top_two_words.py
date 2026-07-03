# 檔名：

# top_two_words.py
from typing import List


def top_two_words(words: List[str]) -> List[str]:
    """
    找出出現次數最多的前兩個單字

    Input:

    [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "kiwi",
        "banana"
    ]

    Output:

    ["apple", "banana"]

    因為：

    apple  = 3
    banana = 3
    orange = 1
    kiwi   = 1

    若次數相同，
    維持 sorted 後的結果即可
    """

    total = {}
    for w in words:
        total[w] = total.get(w, 0) + 1
        
    return sorted(
        total,
        key = lambda word: -total[word]
    )[:2]


if __name__ == "__main__":
    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "kiwi",
        "banana"
    ]

    print(top_two_words(words))
# 提示 1

# 先得到：

# {
#     "apple": 3,
#     "banana": 3,
#     "orange": 1,
#     "kiwi": 1
# }
# 提示 2

# 今天你已經寫過：

# sorted(
#     total.items(),
#     key=lambda item: -item[1]
# )
# 提示 3

# 最後可能會得到：

# [
#     ("apple", 3),
#     ("banana", 3),
#     ("orange", 1),
#     ("kiwi", 1)
# ]

# 你真正要思考的是：

# 如何變成

# ["apple", "banana"]

# 這題其實是：

# most_common_word
# +
# top_two_departments

# 的混血版。

# 預估 5 分鐘內。

# 做完貼上來，我再看你是不是已經把：

# dict
# items()
# sorted()
# lambda
# tuple unpacking

# 串成一條線了。🐍🚀