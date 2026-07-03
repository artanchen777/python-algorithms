# Two Sum - 變形版（稍微更接近實戰）
# nums = [2, 7, 11, 15, 3, 6]
# target = 9

# 請你：

# 回傳所有符合 target 的 index pair

# 預期：

# [(0, 1), (4, 5)]

# 因為：

# nums[0] + nums[1] = 2 + 7 = 9
# nums[4] + nums[5] = 3 + 6 = 9

# 限制：

# 不可重複使用同一 index
# 時間複雜度盡量 O(n)
# 可以使用 hash map

from typing import List, Tuple


def two_sum_all_pairs(nums: List[int], target: int) -> List[Tuple[int, int]]:
    # 在這裡實作
    
    keep = {}
    result = []
    for index, num in enumerate(nums):
        keep_num = target - num
        if keep_num in keep:
            result.append((keep[keep_num], index))
        else:
            keep[num] = index
    return result


# ===== test case =====

nums = [2, 7, 11, 15, 3, 6]
target = 9

result = two_sum_all_pairs(nums, target)

print(result)

# expected:
# [(0, 1), (4, 5)]