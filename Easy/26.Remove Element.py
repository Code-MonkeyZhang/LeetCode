class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Your code here
        k = 0  # 指向下一个要放置非val元素的位置
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



def test_remove_element():
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test case 1: k = {k1}, nums = {nums1[:k1]}")

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test case 2: k = {k2}, nums = {nums2[:k2]}")

    # Test case 3 (empty array)
    nums3 = []
    val3 = 0
    k3 = solution.removeElement(nums3, val3)
    print(f"Test case 3: k = {k3}, nums = {nums3[:k3]}")

    # Test case 4 (all elements are val)
    nums4 = [1, 1, 1]
    val4 = 1
    k4 = solution.removeElement(nums4, val4)
    print(f"Test case 4: k = {k4}, nums = {nums4[:k4]}")


# Run the tests
test_remove_element()
