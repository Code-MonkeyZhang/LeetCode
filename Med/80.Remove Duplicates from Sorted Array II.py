# LeetCode 80: Remove Duplicates from Sorted Array II

"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates 
in-place such that each unique element appears at most twice. The relative order 
of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the 
input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""
from typing import List


class High_Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2

        for i in range(2, len(nums)):
            # send out i, find something diff from memo
            if nums[i] != nums[k-2]:
                # replace
                nums[k] = nums[i]
                k += 1
        return k


def test_solution():
    solution = High_Solution()

    # Test case 1: Example 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 5, f"Test case 1 failed: expected 5, got {k1}"
    assert nums1[:k1] == [
        1, 1, 2, 2, 3], f"Test case 1 failed: expected [1,1,2,2,3], got {nums1[:k1]}"

    # Test case 2: Example 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 7, f"Test case 2 failed: expected 7, got {k2}"
    assert nums2[:k2] == [0, 0, 1, 1, 2, 3,
                          3], f"Test case 2 failed: expected [0,0,1,1,2,3,3], got {nums2[:k2]}"

    # Test case 3: Empty array
    nums3 = []
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 0, f"Test case 3 failed: expected 0, got {k3}"
    assert nums3 == [], f"Test case 3 failed: expected [], got {nums3}"

    # Test case 4: Single element
    nums4 = [1]
    k4 = solution.removeDuplicates(nums4)
    assert k4 == 1, f"Test case 4 failed: expected 1, got {k4}"
    assert nums4 == [1], f"Test case 4 failed: expected [1], got {nums4}"

    # Test case 5: Two elements
    nums5 = [1, 1]
    k5 = solution.removeDuplicates(nums5)
    assert k5 == 2, f"Test case 5 failed: expected 2, got {k5}"
    assert nums5 == [1, 1], f"Test case 5 failed: expected [1,1], got {nums5}"

    # Test case 6: All unique elements
    nums6 = [1, 2, 3, 4, 5]
    k6 = solution.removeDuplicates(nums6)
    assert k6 == 5, f"Test case 6 failed: expected 5, got {k6}"
    assert nums6 == [
        1, 2, 3, 4, 5], f"Test case 6 failed: expected [1,2,3,4,5], got {nums6}"

    # Test case 7: All same elements
    nums7 = [1, 1, 1, 1, 1]
    k7 = solution.removeDuplicates(nums7)
    assert k7 == 2, f"Test case 7 failed: expected 2, got {k7}"
    assert nums7[:k7] == [
        1, 1], f"Test case 7 failed: expected [1,1], got {nums7[:k7]}"

    # Test case 8: Multiple duplicates
    nums8 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    k8 = solution.removeDuplicates(nums8)
    assert k8 == 8, f"Test case 8 failed: expected 8, got {k8}"
    assert nums8[:k8] == [1, 1, 2, 2, 3, 3, 4,
                          4], f"Test case 8 failed: expected [1,1,2,2,3,3,4,4], got {nums8[:k8]}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
