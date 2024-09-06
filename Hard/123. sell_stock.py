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
        total_profit = 0

        return total_profit


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
