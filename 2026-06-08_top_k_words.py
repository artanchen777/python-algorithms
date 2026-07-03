# 檔名：

# top_k_words.py
# from typing import List


def top_k_words(words: List[str], k: int) -> List[str]:
    """
    找出出現次數最多的前 k 個單字

    Input:

    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "kiwi",
        "banana",
        "grape"
    ]

    k = 3

    Output:

    ["apple", "banana", "orange"]

    因為：

    apple  = 3
    banana = 3
    orange = 1
    kiwi   = 1
    grape  = 1

    取前 3 名
    """
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
        
    return sorted(
        counter,
        key = lambda word: -counter[word]
    )[:k]


if __name__ == "__main__":
    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "kiwi",
        "banana",
        "grape"
    ]

    print(top_k_words(words, 3))
# 提示 1

# 你剛剛才寫過：

# top_two_words()
# 提示 2

# 這題其實只是：

# [:2]

# 變成：

# [:k]
# 提示 3

# 我故意把題目寫成：

# k

# 因為這是面試很常見的參數。

# 例如：

# Top 10
# Top 5
# Top 100

# 都會變成：

# k
# 本題目的

# 開始讓你感受到：

# Top K 題型

# 這是 HackerRank / LeetCode 很常見的一大族群。

# 我預估你這題：

# 2~4 分鐘

# 應該能解掉。

# 而且我很好奇你會不會直接把 top_two_words() 泛化成 top_k_words()。