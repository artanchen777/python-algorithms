# 🔥 題目 3：Two Sum II（排序版）
# 題目

# 給一個 已排序 的陣列 nums（遞增），

# 找出兩個數字加起來等於 target，

# 回傳它們的 index。

# 但這次：

# 👉 只能用 O(n)
# 👉 不能用 dict

# 範例
# nums = [1,2,3,4,6]
# target = 6

# 答案：

# [1,3]  # 2 + 4
# 🎯 這題重點
# 不用雙層 for
# 不用 hash map
# 用雙指標（two pointers）
# 🔥 為什麼出這題？

# 因為金融後端常考：

# 雙指標
# 排序特性利用
# 時間複雜度優化
# 💡 提示（不給完整答案）

# 設：

# left = 0
# right = len(nums) - 1

# 然後：

# 如果 sum 太小 → left++
# 如果 sum 太大 → right--
# 如果剛好 → return

def twoSumPointer(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    left = 0
    right = length - 1
    sum = 0
    
    if length < 2:
        return []
    
    while left < right:
        sum = nums[left] + nums[right]
        
        if sum > target:
            right = right - 1
        elif sum < target:
            left = left + 1
        else:
            return [left, right]
    return []
print(twoSumPointer([1,2,3,4,6], 6))



# 現在給你一個更重要的觀察：

# 當 target 很大時，
# 雙指標其實退化成：

# 單向線性掃描

# 因為每次都只會 left++。

# 但時間複雜度仍然是 O(n)。

# 這裡有一個真正成熟工程師會意識到的點：

# 雙指標不是魔法。

# 它只是：

# 善用排序，避免回頭。