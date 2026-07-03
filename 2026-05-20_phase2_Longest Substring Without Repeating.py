# 題目：Longest Substring Without Repeating Characters

# 給定字串：

# s = "abcabcbb"

# 請回傳：

# 3

# 因為最長不重複 substring 是：

# "abc"

# 長度為 3。

# 範例 2
# s = "bbbbb"

# 回傳：

# 1
# 範例 3
# s = "pwwkew"

# 回傳：

# 3

# 因為：

# "wke"
# 要求
# O(n)
# 使用 sliding window
# 不准暴力雙迴圈
# 今天的重點（很重要）

# 你現在先不要急著打。

# 先回答我：

# 你會準備哪些變數？

# 例如：

# left
# right
# seen
# max_len

# 你先口述。

# 然後再回答：

# 當：

# s[right] 已經在 seen

# 時。


# def longestSubstring(s: str) -> int:
#     left = 0
#     right = 0
#     seen = {}
#     str_len = len(s)
#     max_len = 0
    
#     while left < str_len and right < str_len:
#         if s[right] not in seen:
#             seen[s[right]] = right
#             right += 1
#             max_len = max(max_len, right - left)
#         else:
#             del seen[s[left]]
#             left += 1
#     return max_len

# print(longestSubstring("abcabcbb"))
# print(longestSubstring("bbbbb"))
# print(longestSubstring("pwwkew"))
            
def longestSubstring(s: str) -> int:
    left = 0
    right = 0
    str_len = len(s)
    res_max_len = 0
    seen = set()
    
    while left < str_len and right < str_len:
        if s[right] in seen:
            seen.remove(s[left])
            left += 1
        else:
            seen.add(s[right]) # 進階版可以用跳的
            right += 1
            res_max_len = max(res_max_len, right - left)
    return res_max_len

print('\n')
print(longestSubstring("abcabcbb"))
print(longestSubstring("bbbbb"))
print(longestSubstring("pwwkew"))