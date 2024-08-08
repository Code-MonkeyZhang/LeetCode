import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 请在此处编写您的代码
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        self.assertEqual(self.solution.longestPalindrome("babad"), "bab")

    def test_case2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_case3(self):
        self.assertEqual(self.solution.longestPalindrome("a"), "a")

    def test_case4(self):
        self.assertEqual(self.solution.longestPalindrome("ac"), "a")

    def test_case5(self):
        self.assertEqual(self.solution.longestPalindrome("abb"), "bb")


if __name__ == "__main__":
    unittest.main()
