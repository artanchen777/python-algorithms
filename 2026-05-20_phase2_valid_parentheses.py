# 題目

# 給一個字串，只包含：

# ( ) { } [ ]

# 判斷括號是否正確配對。

# 範例
# "()" → True
# "()[]{}" → True
# "(]" → False
# "([)]" → False
# "{[]}" → True
# 限制
# O(n)
# 使用 stack
# 不可遞迴
# 骨架（你填）
# def isValid(s: str) -> bool:
#     stack = []
#     mapping = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }

#     for char in s:
#         ...
    
#     return ...

# 計時 12 分鐘。


def isValid(s: str) -> bool:
    left_bracket = set(['(', '{', '['])
    stack = []
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    for char in s:
        if char in left_bracket:
            stack.append(char)
        elif char in mapping:
            if not stack:
                return False
            pop_obj = stack.pop()
            if mapping[char] != pop_obj:
                return False
        else:
            continue # 若是非邊界符號，跳過
    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("[[["))
print(isValid("]]]"))
print(isValid("["))
print(isValid("]"))

