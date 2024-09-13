# 189. Rotate Array
import copy
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


class Solution:
    def rotate_extra_space(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # Your code here
        if k > length:
            k = k % length

        start = length-k
        ans = []
        for num in nums[start:]:
            ans.append(num)

        for j in range(start):
            ans.append(nums[j])

        for i in range(length):
            nums[i] = ans[i]

    def rotate_reverse_array(self, nums: list[int], k: int) -> None:
        length = len(nums)
        if k > length:
            k = k % length

        def reverse_array(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        # reverse entire array
        reverse_array(0, length-1)
        reverse_array(0, k-1)
        reverse_array(k, length-1)


solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
solution.rotate_extra_space(nums1, k1)
print(nums1)  # Expected output: [5,6,7,1,2,3,4]

# Test case 2
nums2 = [-1, -100, 3, 99]
k2 = 2
solution.rotate_extra_space(nums2, k2)
print(nums2)  # Expected output: [3,99,-1,-100]

# Test case 2
nums2 = [1, 2]
k2 = 3
solution.rotate_extra_space(nums2, k2)
print(nums2)  # Expected output: [3,99,-1,-100]

# You can add more test cases here
# Test case 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
solution.rotate_reverse_array(nums1, k1)
print(nums1)  # Expected output: [5,6,7,1,2,3,4]

# Test case 2
nums2 = [-1, -100, 3, 99]
k2 = 2
solution.rotate_reverse_array(nums2, k2)
print(nums2)  # Expected output: [3,99,-1,-100]

# Test case 2
nums2 = [1, 2]
k2 = 3
solution.rotate_reverse_array(nums2, k2)
print(nums2)  # Expected output: [3,99,-1,-100]
