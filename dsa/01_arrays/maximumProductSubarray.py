
"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray with the largest product
and return its product.

Example:
    Input: nums = [2, 3, -2, 4]
    Output: 6
    Explanation: The subarray [2, 3] has the largest product 6.

Time Complexity:  O(N)
Space Complexity: O(1)
"""

def maxProductBruteForce(nums: list[int]) -> int:
    max_product = float('-inf')
    n = len(nums)
    for i in range(n):
        current_product=1
        for j in range(i,n):
            current_product *= nums[j]
            max_product = max(max_product,current_product)
    return max_product


def max_product_optimal(nums:list[int])->int:
    ans=nums[0]
    curr_min =nums[0]
    curr_max = nums[0]
    for i in range(1, len(nums)):
        num= nums[i]
        if num<0:
            curr_max, curr_min = curr_max, curr_min
        curr_max = max(num, curr_max*num)
        curr_min = min(num, curr_min*num)
        ans = max(ans,curr_max)
    return ans




# Example usage
nums = [2, 3, -2, 4]
print(f"Array: {nums}")
print(f"Maximum Product: {max_product_optimal(nums)}")  # Output: 6

nums = [-2, 0, -1]
print(f"Array: {nums}")
print(f"Maximum Product: {max_product_optimal(nums)}")  # Output: 0

#nums3 = [-2, 3, -4]
#print(f"Array: {nums3}")
#print(f"Maximum Product: {maxProduct(nums3)}")  # Output: 24