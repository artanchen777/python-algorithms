# 題目

# 給定一個整數陣列 nums
# 請回傳出現頻率最高的數字。

# 若有多個數字頻率相同，回傳「數值較小」的那個。

# 範例
# Input:  [1,1,1,2,2,3]
# Output: 1
# Input:  [4,4,1,1]
# Output: 1
# 條件
# O(n)
# 不可排序整個陣列
# 使用 dict
# 至少有 1 個元素
# 筆試提醒

# 這題金融常出，因為：

# 檢查 dict 熟練度
# 檢查 tie-break 處理
# 檢查邏輯完整度

# 寫法提示（不是答案）：

# 1️⃣ 先建立頻率表
# 2️⃣ 用一個變數記錄目前最高頻率
# 3️⃣ 同頻率時比較數值大小

def most_frequent(nums: List[int]) -> int:
    if len(nums) == 0:
        return -1
    
    if len(nums) == 1:
        return nums[0]
    
    # make map
    frequent_map = {}
    for value in nums:
        if value not in frequent_map:
            frequent_map[value] = 1
        else:
            frequent_map[value] += 1
    
    # count 
    max_freq = 0
    target = None
    
    for value, freq in frequent_map.items():
        
        if freq > max_freq:
            max_freq = freq
            target = value
        elif freq == max_freq:
            target = min(target, value)
            
    return target


print(most_frequent([1,1,1,2,2,3]))
print(most_frequent([4,4,1,1]))
