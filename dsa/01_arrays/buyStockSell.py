"""
Best Time to Buy and Sell Stock (LeetCode 121)

Problem:
    You are given `prices`, where prices[i] is the price of a stock on day i.
    Choose one day to buy and a later day to sell to make the maximum profit.

Rules:
    - Only one transaction: buy once, sell once.
    - You must buy before you sell (i < j).
    - If no profit is possible, return 0.

Examples:
    [7, 1, 5, 3, 6, 4] -> 5    (buy at 1 on day 1, sell at 6 on day 4)
    [7, 6, 4, 3, 1]    -> 0    (prices only fall, so never buy)

Approaches:
    | Approach    | Time   | Space | Key idea                                          |
    |-------------|--------|-------|---------------------------------------------------|
    | Brute force | O(n^2) | O(1)  | Try every (buy, sell) pair with i < j             |
    | Better      | O(n)   | O(n)  | Precompute the best future sell price for each day|
    | Optimal     | O(n)   | O(1)  | One pass: track the lowest price seen so far      |
"""

# 1. Brute Force
#
# Idea:
#   Try every (buy day i, sell day j) pair with i < j and keep the best profit.
#
# Steps:
#   1. max_profit = 0
#   2. for i from 0 to n-1:              # buy day
#        for j from i+1 to n-1:          # sell day (always after buy)
#            profit = prices[j] - prices[i]
#            update max_profit if profit is bigger
#   3. Return max_profit (stays 0 if prices only fall)
#
# Time: O(n^2)   Space: O(1)

def maxProfit_bruteForce(prices:list[int])->int:
    max_profit =0
    n = len(prices)
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i] 
            if profit > max_profit:
                max_profit = profit
    return max_profit


# 2. Optimal (One Pass)
#
# Idea:
#   The best sell on any day = today's price - lowest price BEFORE today.
#   So walk once, remembering the cheapest price seen so far.
#
# Steps:
#   1. min_price = infinity, max_profit = 0
#   2. for each price:
#        if price < min_price: min_price = price      # new best day to buy
#        elif price - min_price > max_profit:         # selling today beats best so far
#            max_profit = price - min_price
#   3. Return max_profit
#
# Dry run: prices = [7, 1, 5, 3, 6, 4]
#   7: min=7                 profit=0
#   1: min=1                 profit=0
#   5: 5-1=4 > 0             profit=4
#   3: 3-1=2 (no change)     profit=4
#   6: 6-1=5 > 4             profit=5
#   4: 4-1=3 (no change)     profit=5   -> answer 5 ✅
#
# Time: O(n)   Space: O(1)
def maxProfit_optimal(prices:list[int])->int:
    min_price= float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

    




print(maxProfit_optimal([7,1,5,3,6,4]))
