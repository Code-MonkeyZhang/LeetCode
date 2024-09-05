class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """

        # edge case: x is one digit
        if x < 10 and x > -10:
            return x

        # edge case: x is neg
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        num = x
        digit = 0
        reverseNum = 0
        while num != 0:
            # take the last digit of num
            digit = num % 10
            # update number
            reverseNum = reverseNum*10+digit
            # move num to left by one digit
            num = num//10

        # edge case: x out of 32bits bounds
        if reverseNum > 2**31 - 1 or reverseNum < -2**31:
            return 0

        return sign*reverseNum


# 测试用例


def test_solution():
    solution = Solution()

    # 测试用例1
    assert solution.reverse(123) == 321

    # 测试用例2
    assert solution.reverse(-123) == -321

    # 测试用例3
    assert solution.reverse(120) == 21

    # 测试用例4: 溢出情况
    assert solution.reverse(1534236469) == 0

    print("所有测试用例通过!")


# 运行测试
test_solution()
