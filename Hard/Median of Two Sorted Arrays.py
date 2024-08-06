from typing import List


class BasicSolution:
    def findMedianSortedArrays(self, nums1, nums2):
        # O(m+n)
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        merge_array = []
        i, j = 0, 0

        while i < nums1_length and j < nums2_length:
            if nums1[i] <= nums2[j]:
                merge_array.append(nums1[i])
                i += 1
            else:
                merge_array.append(nums2[j])
                j += 1

        # 如果还有剩余元素，添加到 merged 数组
        merge_array.extend(nums1[i:])
        merge_array.extend(nums2[j:])

        total_len = nums1_length+nums2_length
        # if total_len is even
        midpoint = total_len//2-1
        if total_len % 2 == 0:
            median = (merge_array[midpoint]+merge_array[midpoint+1])/2.0
        else:
            median = merge_array[midpoint+1]
        return median


class HighSolution:
    def findMedianSortedArrays(self, nums1, nums2):
        pass


def test_solution():
    solution = HighSolution()

    # 测试用例1: 基本情况
    print(solution.findMedianSortedArrays([1, 3], [2]) == 2.0)
    print(solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
    print(solution.findMedianSortedArrays([], [1]) == 1.0)
    print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7]) == 4.0)
    print(solution.findMedianSortedArrays([-1, 3], [-2, 5]) == 1.0)
    print(solution.findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3]) == 2.0)
    print(solution.findMedianSortedArrays(
        [1], [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5)


# 运行测试
if __name__ == "__main__":
    test_solution()
