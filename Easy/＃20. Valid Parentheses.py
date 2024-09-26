class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # 如果是左括号
            if char not in mapping:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if mapping[char] != top:
                    return False

        return len(stack) == 0


def run_tests():
    solution = Solution()
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "(((",
        ")))",
        ""
    ]

    for i, case in enumerate(test_cases, 1):
        result = solution.isValid(case)
        print(f"Test case {i}: '{case}' -> {'Valid' if result else 'Invalid'}")


# Run the tests
if __name__ == "__main__":
    run_tests()
