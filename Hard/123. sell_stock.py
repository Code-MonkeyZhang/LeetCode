# LeetCode 123: Best Time to Buy and Sell Stock III
from typing import List  # Add this import


class Solution:
    def shortest_solution(self, prices: List[int]) -> int:
        # edge case: return 0 when no price or there's only one data
        if len(prices) == 0 or len(prices) == 1:
            return 0
        # init variables
        buy_price = float('inf')
        total_cost = float('inf')

        profit = 0
        total_profit = 0

        # [3, 5, 0, 0, 3, 1, 4]

        # start loop:
        for price in prices:
            # purchase
            buy_price = min(buy_price, price)
            profit = max(profit, price-buy_price)
            total_cost = min(total_cost, price-profit)
            total_profit = max(total_profit, price-total_cost)

        return total_profit

    def dp_solution(self, prices: List[int]) -> int:
        # deal with special edge cases:
        # 1. empty list
        # 2. only one element
        if len(prices) == 0 or len(prices) == 1:
            return 0

        # init variables
        min_buy_price = float("inf")
        max_left_profit = [0]*len(prices)

        max_sell_price = float("-inf")
        max_right_profit = [0]*len(prices)

        # looping from left to right
        for i in range(len(prices)):
            price = prices[i]
            min_buy_price = min(min_buy_price, price)
            # 与前一次的profit做比较
            # 当i=0的时候，由于max_left_profit[-1]是最后一个元素，所以并不会超出范围
            max_left_profit[i] = max(max_left_profit[i-1], price-min_buy_price)

        # looping from right to left
        for i in reversed(range(len(prices))):
            price = prices[i]
            max_sell_price = max(max_sell_price, price)
            max_right_profit[i] = max(
                max_right_profit[i-1], max_sell_price-price)

        # pick the highest profit
        max_total_profit = 0
        for i in range(len(prices)):
            total_profit = max_left_profit[i]+max_right_profit[i]
            if total_profit > max_total_profit:
                max_total_profit = total_profit

        return max_total_profit


def test_solution():
    sol = Solution()

    assert sol.shortest_solution([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert sol.shortest_solution([1, 2, 3, 4, 5]) == 4
    assert sol.shortest_solution([7, 6, 4, 3, 1]) == 0

    assert sol.dp_solution([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert sol.dp_solution([1, 2, 3, 4, 5]) == 4
    assert sol.dp_solution([7, 6, 4, 3, 1]) == 0

    print("All test cases passed!")


# Uncomment the following line to run the test cases
test_solution()
