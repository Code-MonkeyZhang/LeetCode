# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)

        return max_profit


# Example usage:
solution = Solution()

# Test cases
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))    # Expected output: 0

# You can add more test cases here
