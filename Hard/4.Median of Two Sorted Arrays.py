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

        total_len = nums1_length + nums2_length
        # if total_len is even
        midpoint = total_len // 2 - 1
        if total_len % 2 == 0:
            median = (merge_array[midpoint] + merge_array[midpoint + 1]) / 2.0
        else:
            median = merge_array[midpoint + 1]
        return median


class HighSolution:
    def findMedianSortedArrays(self, nums1, nums2):
        # if nums1 is longer, switch them to make sure nums1 is the shortest
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        total_length = len_nums1+len_nums2
        start = 0
        end = len_nums1
        # initially make sure cut_x is in the middle of slide window
        cut_x = (start+end)//2

        while start <= end:
            # make sure cut_y + cut_x is in the middle of total length
            # if total_length is odd, left has one more that right therefore +1
            # for example, total=5, cut at 5+1//2=3
            cut_y = (total_length+1)//2-cut_x

            # we want the max_leftX<=min_rightY and maxleftY<=minrightX
            # assign values
            if cut_x == 0:
                max_left_X = float('-inf')
            else:
                max_left_X = nums1[cut_x-1]
            if cut_x == len_nums1:
                min_right_X = float('inf')
            else:
                min_right_X = nums1[cut_x]
            # 这里 -inf 和 inf 的切换记得区分
            if cut_y == 0:
                max_left_Y = float('-inf')
            else:
                max_left_Y = nums2[cut_y-1]
            if cut_y == len_nums2:
                min_right_Y = float('inf')
            else:
                min_right_Y = nums2[cut_y]

            # we want the max_leftX<=min_rightY and maxleftY<=minrightX
            if max_left_X <= min_right_Y and max_left_Y <= min_right_X:
                if total_length % 2 == 0:
                    return (max(max_left_X, max_left_Y)+min(min_right_X, min_right_Y))/2.0
                else:
                    return (max(max_left_X, max_left_Y))
            elif max_left_X > min_right_Y:
                # move cut_x to the left
                cut_x -= 1
            else:
                # move cut_x to the right
                cut_x += 1


def test_solution():
    solution = HighSolution()

    # 测试用例1: 基本情况
    print(solution.findMedianSortedArrays([1, 3], [2]))  # == 2.0
    print(solution.findMedianSortedArrays(
        [1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]))  # == 11
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # == 2.5
    print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7]))  # == 4.0
    print(solution.findMedianSortedArrays([-1, 3], [-2, 5]))  # == 1.0
    print(solution.findMedianSortedArrays(
        [1], [2, 3, 4, 5, 6, 7, 8, 9, 10]))  # == 5.5    print(solution.findMedianSortedArrays(

    print(solution.findMedianSortedArrays(
        [3], [-2, -1]))  # == -1    print(solution.findMedianSortedArrays(
    print(solution.findMedianSortedArrays(
        [100001], [100000]))  # == -1    print(solution.findMedianSortedArrays(


# 运行测试
if __name__ == "__main__":
    test_solution()
