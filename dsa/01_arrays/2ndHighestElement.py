"""
Find the second highest element in the array

Example:
    Input: arr = [1,2,3,4,5,6,7,8,9,10]
    Output: 9

Approach (single pass):
    Keep two variables: first (highest) and second (second highest).
    - If num > first: old first becomes second, num becomes first.
    - Else if first > num > second: num becomes second.
    Duplicates of the highest are skipped, so [5,5,4] gives 4.
    Time: O(n), Space: O(1)
"""


def secondHighest(arr:list[int])->int:
    first = second = float('-inf')
    for num in arr:
        # new highest found -> shift old highest down to second
        if num > first:
            second = first
            first = num
        # between first and second (and not equal to first)
        elif first > num > second:
            second = num
    # no second highest (empty array or all elements equal)
    return second if second != float('-inf') else -1


arr = [1,2,3,4,5,6,7,8,9,10]
print(secondHighest(arr))        # 9
print(secondHighest([5,5,4]))    # 4
print(secondHighest([7,7,7]))    # -1
