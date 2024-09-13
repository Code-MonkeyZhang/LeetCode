from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dests = []
        dests.append(len(nums)-1)
        for i in reversed(range(len(nums)-1)):
            num = nums[i]
            for dest in dests:
                if num >= dest-i:
                    dests.append(i)
                    break

        for num in dests:
            if num == 0:
                return True

        return False


solution = Solution()

# 测试用例 1
print(solution.canJump([2, 3, 1, 1, 4]))  # 应该返回 True

# 测试用例 2
print(solution.canJump([3, 2, 1, 0, 4]))  # 应该返回 False
