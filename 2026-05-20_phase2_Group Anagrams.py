# Group Anagrams

# 原因：

# hash map 題
# 輕量
# 不太燒腦
# 很像資料 grouping
# 很適合現在狀態
# 題目

# 給定：

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 回傳：

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
# 核心概念

# 因為：

# eat
# tea
# ate

# 排序後都會變：

# "aet"

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    result = {}
    
    for s in strs:
        s_order = ''.join(sorted(s))
        if s_order not in result:
            result[s_order] = []
        
        result[s_order].append(s)

    return list(result.values())

