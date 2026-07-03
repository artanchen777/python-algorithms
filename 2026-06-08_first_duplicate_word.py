# 我故意出個輕量 HackerRank 題型。

# 不用 group by。

# 不用 salary。

# 不用 dept。

# 檔名：

# first_duplicate_word.py
# from typing import List


def first_duplicate_word(words: List[str]) -> str:
    """
    找出第一個重複出現的單字

    Input:

    ["apple", "banana", "orange", "banana", "apple"]

    Output:

    "banana"

    說明：

    banana 是第一個再次出現的單字
    """
    seen = set()
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    
    return ''


if __name__ == "__main__":
    words = [
        "apple",
        "banana",
        "orange",
        "banana",
        "apple"
    ]

    print(first_duplicate_word(words))

# 提示只有一個：

# 你做過這個親戚。

# has_duplicate_user()

# 以及：

# find_first_duplicate_index()

# 所以這題其實是在告訴你：

# 題目換皮了
# 核心沒換

# 預估：

# 1~3 分鐘

# 做完我們就收工。