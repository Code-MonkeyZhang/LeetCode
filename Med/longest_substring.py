class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 在这里实现你的解决方案
        pass


# 测试用例
def test_solution():
    solution = Solution()

    # 测试用例 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3, "Test case 1 failed"

    # 测试用例 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1, "Test case 2 failed"

    # 测试用例 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3, "Test case 3 failed"

    # 额外的测试用例
    assert solution.lengthOfLongestSubstring("") == 0, "Empty string test failed"
    assert solution.lengthOfLongestSubstring("dvdf") == 3, "Test case 4 failed"

    print("All test cases passed!")


# 运行测试
test_solution()