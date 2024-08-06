class BasicSolution:
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


class HighSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用字典存储每个字符最后出现的索引
        char_seen = {}
        # 当前无重复子串的起始位置
        start = 0
        # 最长无重复子串的长度
        longest_step = 0
        # 当前无重复子串的长度
        current_step = 0
        # 遍历字符串，i 是索引，char 是字符
        for i, char in enumerate(s):
            # 如果字符已经在当前子串中出现过, 并且出现的位置在当前子串的起始位置之后
            if char in char_seen and char_seen[char] >= start:
                # 更新起始位置到重复字符的下一个位置
                start = char_seen[char] + 1
                # 重新计算当前子串长度
                current_step = i - start + 1
            else:
                # 如果是新字符或者在当前子串起始位置之前出现过
                # 增加当前子串长度
                current_step += 1
                # 更新最长子串长度（如果当前子串更长）
                longest_step = max(longest_step, current_step)

            # 更新字符最后出现的位置
            char_seen[char] = i

        # 返回最长无重复子串的长度
        return longest_step


# 测试用例
def HighSolution():
    solution = BasicSolution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("dvadf"))
    print(solution.lengthOfLongestSubstring("a"))
    print(solution.lengthOfLongestSubstring("au"))
    print(solution.lengthOfLongestSubstring(""))

    print("All test cases passed!")


def test_solution():
    solution = HighSolution()


# 运行测试
test_solution()
