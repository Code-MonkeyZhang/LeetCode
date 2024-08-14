class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p2 >= 0:
            if nums1[p1] > nums2[p2] and p1 >= 0:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1


def test_merge_sorted_array():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 1: {nums1}")

    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 2: {nums1}")

    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 3: {nums1}")

    # Test case 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 3: {nums1}")


# Run the tests
test_merge_sorted_array()
