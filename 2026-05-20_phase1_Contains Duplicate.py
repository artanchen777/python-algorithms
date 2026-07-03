# 題目 1（暖機強化）
# 🧩 Contains Duplicate

# 給你一個整數陣列 nums
# 如果任何數字出現兩次，回傳 True
# 否則回傳 False

# 範例：
# Input: [1,2,3,1]
# Output: True

# Input: [1,2,3,4]
# Output: False
# 🎯 要求
# 時間複雜度 O(n)
# 不要排序
# 不要雙迴圈
# 用你熟悉的 dict / set
# 🧠 提醒

# 這題本質是在考：

# set 的特性
# 或 dict 查詢
# in 的使用

def detectDuplicate(nums: List[int]) -> bool:
    keep = {}
    
    for index, value in enumerate(nums):
        if value in keep:
            return True
        keep[value] = index
    return False

print('\n題目 1（暖機強化）')
print(detectDuplicate([1,2,3,1]), sep='\n')

def detectDuplicate2(nums: List[int]) -> bool:
    keep = set()
    
    for value in nums:
        if value in keep:
            return True
        keep.add(value)
    return False

print('\n題目 1（暖機強化）')
print(detectDuplicate2([1,2,3,1]), sep='\n')