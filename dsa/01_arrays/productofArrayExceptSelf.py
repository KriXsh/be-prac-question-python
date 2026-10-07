"""
238. Product of Array Except Self

Problem:
    You are given an integer array nums.
    Goal: Return an array answer where answer[i] equals the product of all
    elements in nums except nums[i].

Key Constraints:
    - Must run in O(n) time.
    - No division allowed (can't compute total product and divide by nums[i]).
    - Output space does not count toward auxiliary space complexity.

Key Intuition (across approaches):
    For any index i, the product of all elements except nums[i] is:

        answer[i] = (product of all elements left of i) * (product of all elements right of i)
        answer[i] = prefix_product[i] * suffix_product[i]

1. Brute Force Approach
    Concept:
        For each element at index i, loop through the array and multiply
        every other element (excluding nums[i]).

    Algorithm Steps:
        1. Initialize an output array `answer` of size n filled with 1s.
        2. For each index i from 0 to n-1:
             - Iterate through every index j from 0 to n-1.
             - If i != j, multiply answer[i] *= nums[j].
        3. Return answer.

    Time: O(n^2)   Space: O(1) auxiliary
"""

#brute force 
def productOfArrayExceptSelf(nums:list[int])->list[int]:
    n= len(nums)
    answer =[1] * n
    for i in range(n):
        for j in range(n):
            if i !=j:
                answer[i] *= nums[j]
    return answer


#optimal
# Optimal Approach (Prefix + Suffix, O(1) extra space)
#{Total Product Except Self} = {Prefix Product (Left side)} * {Suffix Product (Right side)}
# Idea:
#   answer[i] = (product of everything LEFT of i) * (product of everything RIGHT of i)
#   - Pass 1 (left -> right): store the LEFT product in answer[i].
#   - Pass 2 (right -> left): multiply in the RIGHT product, kept in a single
#     running variable `suffix` (no extra array needed).
#
# Steps:
#   1. n = len(nums), answer = [1] * n
#   2. Pass 1 (left -> right), keep `prefix = 1`:
#        for i from 0 to n-1:
#            answer[i] = prefix        # product of everything before i
#            prefix *= nums[i]         # include nums[i] for the next index
#   3. Pass 2 (right -> left), keep `suffix = 1`:
#        for i from n-1 down to 0:
#            answer[i] *= suffix       # multiply by product of everything after i
#            suffix *= nums[i]         # include nums[i] for the next index
#   4. Return answer
#
# Dry run: nums = [1, 2, 3, 4]
#   Pass 1 (prefix):
#     i=0: answer[0] = 1          prefix = 1*1 = 1
#     i=1: answer[1] = 1          prefix = 1*2 = 2
#     i=2: answer[2] = 2          prefix = 2*3 = 6
#     i=3: answer[3] = 6          prefix = 6*4 = 24
#     answer = [1, 1, 2, 6]
#
#   Pass 2 (suffix):
#     i=3: answer[3] = 6*1  = 6   suffix = 1*4  = 4
#     i=2: answer[2] = 2*4  = 8   suffix = 4*3  = 12
#     i=1: answer[1] = 1*12 = 12  suffix = 12*2 = 24
#     i=0: answer[0] = 1*24 = 24  suffix = 24*1 = 24
#     answer = [24, 12, 8, 6]  ✅
#
# Time: O(n)   Space: O(1) extra (output array doesn't count)
# Tip: always use answer[i] BEFORE updating prefix/suffix with nums[i].


def productOfArrayExceptSelfOptimal(nums:list[int])->list[int]:
  n = len(nums)
  answer =[1] * n
  prefix = 1
  for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]
  suffix =1
  for i in range(n-1,-1,-1):
    answer[i] *= suffix
    suffix *= nums[i]
  return answer


print(productOfArrayExceptSelfOptimal([1,2,3,4]))