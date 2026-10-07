"""
217. Contains Duplicate

Problem:
    Given an integer array nums, return True if any value appears at least
    twice in the array, and False if every element is distinct.

Key Intuition:
    We just need to know: "Have I seen this number before?"
    - Brute force answers it by comparing every pair.
    - Optimal answers it instantly using a set (O(1) lookup).
"""


# 1. Brute Force Approach
#
# Idea:
#   Compare every element with every element after it.
#   If any pair is equal -> duplicate found.
#
# Steps:
#   1. n = len(nums)
#   2. for i from 0 to n-1:
#        for j from i+1 to n-1:        # start at i+1 -> skip self & already-checked pairs
#            if nums[i] == nums[j]: return True
#   3. No pair matched -> return False
#
# Dry run: nums = [1, 2, 3, 1]
#   i=0 (1): compare with 2, 3, 1 -> nums[0] == nums[3] ✅ return True
#
# Time: O(n^2)   Space: O(1)
def containsDuplicate(nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False


# 2. Optimal Approach (Hash Set)
#
# Idea:
#   Keep a set of numbers seen so far. Set lookup is O(1) on average,
#   so each number is checked in constant time instead of scanning the array.
#
# Steps:
#   1. seen = empty set
#   2. for each num in nums:
#        if num in seen: return True   # seen before -> duplicate
#        else: add num to seen
#   3. Loop finished, nothing repeated -> return False
#
# Dry run: nums = [1, 2, 3, 1]
#   num=1: not in {}         -> seen = {1}
#   num=2: not in {1}        -> seen = {1, 2}
#   num=3: not in {1, 2}     -> seen = {1, 2, 3}
#   num=1: in {1, 2, 3} ✅   -> return True
#
# Time: O(n)   Space: O(n) (set can hold up to n elements)
#
# Alternatives:
#   - Sorting: sort nums, then check neighbours nums[i] == nums[i+1]
#     -> Time O(n log n), Space O(1) (if sorted in place)
#   - One-liner: return len(set(nums)) != len(nums)
#     -> O(n), but no early exit (always builds the full set)
def containsDuplicateOptimal(nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

print(containsDuplicateOptimal([1,1,1,3,3,4,3,2,4,2]))
