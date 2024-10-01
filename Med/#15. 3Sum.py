# 三数之和问题


class Solution:
    def slow_threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        while len(nums) >= 2:
            threeNums = []
            num1 = nums[0]
            nums = nums[1:]
            for i in range(len(nums)):
                num2 = nums[i]
                right = i+1
                while right < len(nums):
                    num3 = nums[right]
                    if num1+num2+num3 == 0:
                        threeNums.append(num1)
                        threeNums.append(num2)
                        threeNums.append(num3)
                        if threeNums not in ans:
                            ans.append(threeNums)
                        threeNums = []
                        break
                    right += 1

        return ans

    def fast_threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = num1+nums[left]+nums[right]
                if threeSum == 0:
                    ans.append([num1, nums[left], nums[right]])
                    # skip repeating num
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1

        return ans


def run_tests():
    solution = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([], [])
    ]

    for i, (input_nums, expected_output) in enumerate(test_cases):
        result = solution.fast_threeSum(input_nums)
        print(f"Test Case {i + 1}:")
        print(f"Input: {input_nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected_output}")
        print(f"Passed: {sorted(result) == sorted(expected_output)}\n")


if __name__ == "__main__":
    run_tests()
