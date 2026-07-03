# 既然你還有一點電，我出一題剛好踩在：

# set
# dict
# 統計
# 排序

# 交界處。

# 而且開始有一點 HackerRank 味道。

# 檔名：

# most_common_word.py
from typing import List


def most_common_word(words: List[str]) -> str:
    """
    找出出現次數最多的單字

    Input:

    [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple"
    ]

    Output:

    "apple"

    因為：

    apple  出現 3 次
    banana 出現 2 次
    orange 出現 1 次
    """
    # time : 11:22 ~ 11:25
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    
    name, count = max(
        counter.items(),
        key = lambda item: item[1]
    )
    
    return name


if __name__ == "__main__":
    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple"
    ]

    print(most_common_word(words))
# 提示 1

# 第一步很熟悉：

# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }
# 提示 2

# 你今天已經寫過：

# max(
#     total,
#     key=lambda x: total[x]
# )

# 思考：

# total

# 如果變成：

# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }

# 還能不能直接用？

# 提示 3

# 這題有兩種寫法：

# 寫法 A
# max(
#     count,
#     key=lambda word: count[word]
# )
# 寫法 B
# max(
#     count.items(),
#     key=lambda item: item[1]
# )

# 我建議你先寫 A。

# 因為跟今天學的最接近。

# 本題學習點

# 你會發現：

# 部門
# 薪資

# 跟：

# 單字
# 次數

# 其實完全同一個題型。

# 只是換皮而已。

# 這題如果你 5 分鐘內寫出來。

# 我就認定：

# dict 統計
# +
# max(key=...)

# 已經正式進入你的工具箱了