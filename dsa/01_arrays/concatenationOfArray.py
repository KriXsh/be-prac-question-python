"""
1929. Concatenation of Array (Easy)

Problem:
    Given an integer array nums of length n, create an array ans of length 2n
    where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.
    In short: ans is nums concatenated with itself.

Examples:
    [1, 2, 1]    -> [1, 2, 1, 1, 2, 1]
    [1, 3, 2, 1] -> [1, 3, 2, 1, 1, 3, 2, 1]

Approaches:
    1. Manual Fill (index-based)
       Idea: Make ans of size 2n, write each nums[i] into two places.
       Steps:
           1. n = len(nums), ans = [0] * (2 * n)
           2. for i from 0 to n-1:
                  ans[i]     = nums[i]     # first copy
                  ans[i + n] = nums[i]     # second copy
           3. Return ans
       Dry run: nums = [1, 2, 1], n = 3
           i=0: ans[0]=1, ans[3]=1
           i=1: ans[1]=2, ans[4]=2
           i=2: ans[2]=1, ans[5]=1   -> [1, 2, 1, 1, 2, 1] ✅
       Time: O(n)   Space: O(n) (output)

    2. Append Twice
       Idea: Loop over nums two times, appending each element to ans.
       Steps:
           1. ans = []
           2. repeat 2 times: for num in nums: ans.append(num)
           3. Return ans
       Time: O(n)   Space: O(n) (output)

    3. Pythonic (used below)
       Idea: List `+` already concatenates -> nums + nums (or nums * 2).
       Time: O(n)   Space: O(n) (output)

    Note: Every approach is O(n), since you must write 2n elements anyway.
          The manual fill is what interviewers usually want to see.
"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums