class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 在这里实现你的解决方案
        length = len(s)
        char_seen = []
        iter = 0
        longest_step = 0
        step = 0

        while iter < length:
            if s[iter] not in char_seen:
                char_seen.append(s[iter])
                iter += 1
                step += 1
                if iter == length:
                    if step > longest_step:
                        longest_step = step
            elif s[iter] in char_seen:
                if step > longest_step:
                    longest_step = step
                iter = iter - step + 1
                step = 0
                char_seen = []
        return longest_step


# 测试用例
def test_solution():
    solution = Solution()

    # 测试用例 1
    # solution.lengthOfLongestSubstring("abcabcbb") == 3, "Test case 1 failed"
    # print(solution.lengthOfLongestSubstring("abcabcbb"))
    # # 测试用例 2
    # solution.lengthOfLongestSubstring("bbbbb") == 1, "Test case 2 failed"
    #
    # # 测试用例 3
    # solution.lengthOfLongestSubstring("pwwkew") == 3, "Test case 3 failed"
    #
    # # 额外的测试用例
    # solution.lengthOfLongestSubstring("") == 0, "Empty string test failed"
    # solution.lengthOfLongestSubstring("dvdf") == 3, "Test case 4 failed"
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("dvadf"))
    print(solution.lengthOfLongestSubstring("a"))
    print(solution.lengthOfLongestSubstring("au"))
    print(solution.lengthOfLongestSubstring(""))

    print("All test cases passed!")


# 运行测试
test_solution()
