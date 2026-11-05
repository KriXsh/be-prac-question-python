"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Before being passed to your function, nums is possibly rotated at an unknown
pivot index k, e.g. [0,1,2,4,5,6,7] rotated at index 3 becomes [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Approach (linear scan):
    Walk through the array and return the first index whose value equals target.
    Time: O(n), Space: O(1)
    Note: the problem asks for O(log n), which needs a modified binary search
    (at each step one half of the array is always sorted).
"""

def searchinRotatedSortedArray(nums:list[int],target:int)->int:
    # check every element one by one
    for i in range(len(nums)):
        # found the target -> return its index
        if nums[i]==target:
            return i
    # target not present in the array
    return -1


print(searchinRotatedSortedArray([4,5,6,7,0,1,2],0))  # 4
print(searchinRotatedSortedArray([4,5,6,7,0,1,2],3))  # -1
