# 🔥 題目：Valid Anagram

# 給兩個字串 s 和 t
# 如果 t 是 s 的字母重組（每個字元出現次數完全一樣），回傳 True。

# 範例
# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False
# 🎯 限制
# 不准用 sorted()
# 不准用 Counter
# 用 dict 計數
# O(n)
# 🧠 提醒

# 典型解法流程：

# 1️⃣ 先檢查長度
# 2️⃣ 用 dict 統計 s
# 3️⃣ 遍歷 t 扣掉
# 4️⃣ 如果有負數或不存在 → False

# 給你骨架（你自己補）
# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = {}

#     # 統計 s
    
#     # 遍歷 t 扣減

#     return True

def isAnagram(source: str, target: str) -> bool:
    if len(source) != len(target):
        return False
    
    keep = {}
    
    for value in source:
        if value in keep:
            keep[value] += 1 # same as keep[value] = keep.get(value, 0) + 1
        else:
            keep[value] = 1
    
    for value in target:
        if value in keep:
            keep[value] -= 1
        else:
            return False
        
    for value in keep.values():
        if value != 0:
            return False
    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
