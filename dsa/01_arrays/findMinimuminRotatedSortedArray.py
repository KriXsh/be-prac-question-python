"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order (with unique elements)
is rotated between 1 and n times, e.g. [0,1,2,4,5,6,7] might become
[4,5,6,7,0,1,2] if it was rotated 4 times.

Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0

Approach (linear scan):
    Keep track of the smallest value seen so far while walking through the array.
    Time: O(n), Space: O(1)
    Note: the problem asks for O(log n), which needs a binary search comparing
    nums[mid] with nums[right] to find which side the minimum is on.
"""


def findMinimum(nums:list[int])->int:
    # start by assuming the first element is the smallest
    min_value=nums[0]
    for num in nums:
        # found a smaller value -> update the minimum
        if min_value>num:
            min_value = num
    return min_value

print(findMinimum([3,4,5,6,7,1,8,9,1,2]))  # 1
