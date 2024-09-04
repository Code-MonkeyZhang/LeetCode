class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_length = 0

        for i in range(len(s)):
            # 奇数长度回文
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    result = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1

            # 偶数长度回文
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    result = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1

        return result

def test_solution():
    solution = Solution()
    test_cases = [
        ("babad", "bab"),  # 或 "aba"
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),  # 或 "c"
        ("abb", "bb")
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(input_str)
        print(f"Test case {i}:")
        print(f"Input: {input_str}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'PASS' if result == expected or len(result) == len(expected) else 'FAIL'}")
        print()

if __name__ == "__main__":
    test_solution()