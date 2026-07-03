# 題意

# 判斷：

# s

# 跟

# t

# 是否由：

# 完全相同字元組成

# 只是順序不同。

# 例如：

# anagram
# nagaram

# 是同一組字母。

# 所以：

# True

# 例如：

# rat
# car

# 因為：

# t != c

# 所以：

# False
# 額外限制

# 不要用：

# sorted()

# 也就是：

# sorted(s) == sorted(t)

# 不算。

# Hint

# 你最近剛練過：

# dict
# get()
# state retention

# 所以可以思考：

# 如何記錄每個字元出現次數？

# 這題其實跟：

# First Unique Character

# 有血緣關係。

from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    
    count_map = {}
    
    for c in s:
        count_map[c] = count_map.get(c, 0) + 1
            
    for c2 in t:
        if c2 in count_map:
            count_map[c2] = count_map.get(c2, 1) - 1 # default 1 為了避免變負數
        else:
            return False
    
    for v in count_map.values():
        if v != 0:
            return False
    return True

# ===== test =====

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("abc", "cba"))          # True
print(is_anagram("aacc", "ccac"))        # False