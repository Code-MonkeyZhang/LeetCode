from typing import List


class Solution:
    """
    思路:
    这道题和之前的区别在于,现在可以在同一天买和卖
    [1, 2, 3, 4, 5]
       1  1  1  1 
    total profit=4
    因此连续的交易成为可能

    突破口:
    这道题的突破口在于,简单的贪心算法就能凑效
    只要尽可能地比较两天股价的差值,一天买一天卖
    就能实现最大利润
    """

    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        total_profit = 0
        while end < len(prices):
            profit = prices[end]-prices[start]
            if profit >= 0:
                total_profit += profit
            start += 1
            end += 1

        return total_profit


        # Test cases
solution = Solution()

# Test case 1
prices1 = [7, 1, 5, 3, 6, 4]
print(f"Test case 1: {solution.maxProfit(prices1)}")  # Expected output: 7

# Test case 2
prices2 = [1, 2, 3, 4, 5]
print(f"Test case 2: {solution.maxProfit(prices2)}")  # Expected output: 4

# Test case 3
prices3 = [7, 6, 4, 3, 1]
print(f"Test case 3: {solution.maxProfit(prices3)}")  # Expected output: 0
