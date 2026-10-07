"""
Problem: Two Sum
Link:    https://leetcode.com/problems/two-sum/
Level:   Easy

Given nums and target, return indices of the two numbers that add up to target.

Approach:
    One pass with a hashmap value -> index; for each x check if target - x was seen.

Complexity:
    Time  O(n)
    Space O(n)
"""
##brute force

def twoSumBrute(nums:list[int], target:int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []
    

#better approach 
def twoSumOptimal(nums:list[int], target:int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] =i
    return []
    

# def two_sum(nums: list[int], target: int) -> list[int]:
#     seen: dict[int, int] = {}
#     for i, x in enumerate(nums):
#         if target - x in seen:
#             return [seen[target - x], i]
#         seen[x] = i
#     return []


# # ---------------- tests ----------------
# def test_two_sum():
#     assert two_sum([2, 7, 11, 15], 9) == [0, 1]
#     assert two_sum([3, 2, 4], 6) == [1, 2]
#     assert two_sum([3, 3], 6) == [0, 1]
#     assert two_sum([1, 2], 10) == []


if __name__ == "__main__":
    print(twoSumOptimal([2, 7, 11, 15], 9))
