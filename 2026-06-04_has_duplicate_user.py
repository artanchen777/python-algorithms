# 檔名：

# has_duplicate_user.py

# 題目：

from typing import List

def has_duplicate_user(users: List[str]) -> bool:
    """
    判斷是否存在重複使用者

    Example 1:
        Input:
            ["tom", "jack", "mary"]

        Output:
            False

    Example 2:
        Input:
            ["tom", "jack", "mary", "tom"]

        Output:
            True
    """
    seen = set()
    for user in users:
        if user in seen:
            return True
        else:
            seen.add(user)

    return False
# Input 1
print('\n=====')

data1 = ["tom", "jack", "mary"]
print(has_duplicate_user(data1))
# Output

# False

# Input 2

data2 = ["tom", "jack", "mary", "tom"]

print(has_duplicate_user(data2))
# Output

# True

# 提示 1

# 這題和剛剛那題很像。

# 但有一個巨大差異：

# 不用找出誰重複

# 只需要：

# 有
# 或
# 沒有

# 提示 2

# 想想剛剛這段：

# if name in seen:

# 發生時，

# 是不是其實已經知道答案了？

# 提示 3

# 這題是經典 LeetCode：

# Contains Duplicate

# 的資料工程版本。

# 睡前目標：

# 理解為什麼：
# 存在問題 → set