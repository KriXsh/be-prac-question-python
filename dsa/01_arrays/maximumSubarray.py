"""
Maximum Subarray (LeetCode 53)

Given an integer array nums, find the contiguous subarray with the largest sum
and return its sum.

Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6  (subarray [4, -1, 2, 1])
"""


"""
1. Brute Force Approach

Logic:
    Check every possible contiguous subarray, calculate its sum, and track the
    maximum sum found. For an array of size N, there are O(N^2) possible subarrays.

Step-by-Step:
    1. Use an outer loop i to fix the starting index of the subarray.
    2. Use an inner loop j to fix the ending index of the subarray.
    3. Keep a running sum as j moves forward to avoid re-calculating the sum
       from scratch.
    4. Update max_sum whenever the current running sum is greater.

Time Complexity:  O(N^2)
Space Complexity: O(1)
"""

def maxSubarray(nums: list[int]) -> int:
    maxSum = float('-inf')
    n = len(nums)
    for i in range(n):                          # fix start index
        current_sum = 0
        for j in range(i, n):                   # extend end index
            current_sum += nums[j]              # running sum of nums[i..j]
            maxSum = max(maxSum, current_sum)
    return maxSum


"""
2. Optimal Approach (Kadane's Algorithm)

Logic:
    Kadane's Algorithm uses dynamic programming principles. As you traverse the
    array, maintain a running sum (current_sum). If current_sum becomes negative,
    reset it to 0 because a negative sum will only reduce the sum of any future
    subarray it joins.

Intuition:
    Accumulate numbers: [-2, 1, -3, 4]
    - nums[0] = -2: current_sum = -2. Negative, so carrying it forward harms any
      future subarray. Reset current_sum = 0.
    - nums[1] =  1: current_sum = 1. Positive, so it helps future subarrays.
    - nums[2] = -3: current_sum = -2. Reset to 0 again.
    - nums[3] =  4: current_sum = 4.

Note:
    Update max_sum BEFORE resetting, so an all-negative array (e.g. [-3, -1])
    correctly returns the largest element (-1) instead of 0.

Time Complexity:  O(N)
Space Complexity: O(1)
"""

def maxSubarrayKadane(nums: list[int]) -> int:
    maxSum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        maxSum = max(maxSum, current_sum)       # record best before reset
        if current_sum < 0:
            current_sum = 0                     # negative prefix only hurts; drop it
    return maxSum


print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))        # 6
print(maxSubarrayKadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSubarrayKadane([-3, -1, -2]))                     # -1
