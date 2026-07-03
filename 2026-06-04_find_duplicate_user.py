# 今天的目標只有一個：

# set

# 檔名：

# find_duplicate_user.py

# 題目：

# from typing import List

def find_duplicate_user(users: List[str]) -> List[str]:
    """
    找出重複出現的使用者名稱

    Example:
        Input:
            ["tom", "jack", "mary", "tom", "john", "jack"]

        Output:
            ["tom", "jack"]
    """
    seen = {}
    
    # count the number that i showing
    for name in users:
        seen[name] = seen.get(name, 0) + 1
        
    res = set() # remember init by set() not () or {}
    for name, count in seen.items():
        if count > 1:
            res.add(name) # add function is set only
    
    return list(res)

def find_duplicate_user_set(users: List[str]) -> List[str]:
    """
    找出重複出現的使用者名稱

    Example:
        Input:
            ["tom", "jack", "mary", "tom", "john", "jack"]

        Output:
            ["tom", "jack"]
    """
    seen = set()
    duplicate = set()
    # count the number that i showing
    for name in users:
        if name in seen:
            duplicate.add(name) # 先處理特殊情況
        else:
            seen.add(name)

    return list(duplicate)
# Input

users = [
    "tom",
    "jack",
    "mary",
    "tom",
    "john",
    "jack",
]

print('\n-----------')
print(find_duplicate_user(users))
print(find_duplicate_user_set(users))
# Output

# ["tom", "jack"]

# 限制

# 不能使用 count()

# 提示 1（一定要看）

# 你會需要兩個容器：

# seen
# duplicates

# 提示 2

# 當你看到：

# "tom"

# 第一次出現：

# seen.add("tom")

# 當你第二次看到：

# "tom"

# 時，

# 你其實是在判斷：

# if user in seen:

# 提示 3

# 這題其實就是 Contains Duplicate 的前身。

# 你今天下午做過：

# dept
# salary
# group by

# 那題是在練：

# dict

# 這題是在練：

# set

# 先寫。

# 不用追求最佳解。

# 我想先看看你對：

# set()
# add()
# in

# 目前直覺到哪裡了。🐍