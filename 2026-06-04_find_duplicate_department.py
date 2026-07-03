# 我想出一題。

# 這題已經有點 LeetCode 味道了。

# 題目名稱：

# find_duplicate_department.py

# 資料：

data = [
    "A",
    "B",
    "C",
    "A",
    "D",
    "B"
]

# 請實作：

def find_duplicate_department(data):
    # time : 17:25 ~ 17:30
    keep = {}
    
    # count showing times
    for i in data:
        keep[i] = keep.get(i, 0) + 1
        
    my_list = []
    for dept, count in keep.items():
        if count > 1:
            my_list.append(dept)

    return my_list

print('\n-----')
print(find_duplicate_department(data))

# 需求：

# 找出所有重複出現過的部門。

# 結果：

# ["A", "B"]

# 順序不限。

# 限制：

# 不要用：

# Counter
# set(data)

# 直接秒解。

# 只用：

# dict
# set
# for
# if

# 這題為什麼重要？

# 因為它其實就是：

# Contains Duplicate

# 的業務版。

# 你寫完會發現：

# 欸？
# 這不就是我平常在寫的 HashMap？

# 🤣