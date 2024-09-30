class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        product = n
        while product not in seen:
            seen.append(product)

            digits = []
            while product != 0:
                digits.append(product % 10)
                product = product//10
            print(digits)

            for i in range(len(digits)):
                digits[i] = digits[i]**2

            product = sum(digits)
            if product == 1:
                return True

        return False

# 测试用例


def test_solution():
    sol = Solution()

    assert sol.isHappy(7) == False, "Test case 2 failed"

    # 测试用例 1
    assert sol.isHappy(19) == True, "Test case 1 failed"

    # 测试用例 2
    assert sol.isHappy(2) == False, "Test case 2 failed"

    # 可以添加更多测试用例

    print("All test cases passed!")


# 运行测试
test_solution()
