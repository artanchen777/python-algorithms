# 題目名稱
# first_unique_char.py
# 題目：First Unique Character

# 給定一個字串 s

# 請找出：

# 第一個只出現一次的字元索引

# 如果不存在則回傳：

# -1
# 範例 1
# s = "leetcode"

# # l 只出現一次
# # index = 0

# return 0
# 範例 2
# s = "loveleetcode"

# # l 出現2次
# # o 出現2次
# # v 出現1次

# return 2
# 範例 3
# s = "aabb"

# return -1
# 框架


def count_char(s: str)-> Dict[str, int]:
    keep = {}
    
    for c in s:
        keep[c] = keep.get(c, 0) + 1 
        
    return keep
    
def first_unique_char(s: str) -> int:
    keep = count_char(s)
    
    index = 0
    for c in s:
        if keep[c]  == 1:
            return index 
        index += 1
    
    return -1

# ===== test =====

print('first_unique_char: ', first_unique_char("leetcode"))      # 0
print('first_unique_char: ', first_unique_char("loveleetcode"))  # 2
print('first_unique_char: ', first_unique_char("aabb"))          # -1


# 提示

# 你昨天剛寫完：

# count_map[c] = count_map.get(c, 0) + 1

# 的 Frequency Count。

# 這題其實是：

# Frequency Count
# +
# 再掃一次字串

# 就能解。

# 為什麼出這題

# 因為它是：

# Valid Anagram
# ↓
# Frequency Count
# ↓
# First Unique Character

# 同一條技能樹。

# 我想確認你是不是已經開始把：

# HashMap = 保存狀態

# 這件事內化了。

# 限制自己：

# 20 分鐘

# 不要追求完美。

# 寫完直接貼上來。