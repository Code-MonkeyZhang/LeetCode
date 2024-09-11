def majorityElement_candidate(nums):
    """
    这里使用了candidate方法,是一种确定数组内最大元素数量的一种常用方法, 步骤如下：
    candidate = 2
    counter=0
     ^
    [2, 2, 1, 1, 1, 2, 2]

    遍历的时候,
    遇到与candidate相同的, counter+=1
    遇到不同搞得 counter-=1
    当counter 为0 时, 切换candidate为现在遍历的到的num

    candidate: 2 -> 1
    counter: 0
                 ^
    [2, 2, 1, 1, 1, 2, 2]

    其核心思想在于
    每次遇到相同的数字时,都会给candidate 添加"一条命"
    遇到不同数字时,会"减掉一条命"
    当"命"为0的时候, candidate就会被替换

              ^
    [2, 2, 1, 1, 1, 2, 2]

    比如在这时2的命已经被1用完
    这时2就会被1覆盖掉
    """
    candidate = nums[0]
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
        else:
            count -= 1

        if count <= 0:
            # change candidate
            candidate = num
            # reset count
            # count = 1
    return candidate


"""
当然还有一种更简便的方法
那就是将数组排序之后,从(n/2)的地方切开
    [2, 2, 1, 1, 1, 2, 2]
             7/2
->  [1, 1, 1, 2, 2, 2, 2]

其背后的直觉在于
假如有个major_num的数量大于n>2
那么这个数组在排序之后, major_num必然占据了中间的位置 nums[n//2]
想象一下三种情况
- 当major_num是数组中的最大 3
sort之后,3就会堆积在后排,
由于3的数量大于n/2, 3一定会挤占中间的位置[n//2]
            n//2
[1, 1, 1, 2, 3, 3, 3, 3]
- major_num是数组中最小时同理

- major_num 既不是最小,也不是最大时
它也一定会占据中间位置
"""

"""
注意这个方法在复杂度上不如candidate的方法
因为排序需要O(nlogn),而condidate只需要O(n)

正好复习一下排序算法
"""


def majorityElement_sort(nums):
    # sort
    """
    a  b
    2, 2, 1, 1, 1, 2, 2
    """
    length = len(nums)
    for i in range(length):

        for j in range(length-i-1):  # as wall
            if nums[j] > nums[j+1]:
                # swap
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp

    # pick n//2
    return nums[length//2]


test_cases = [
    ([3, 2, 3], 3),  # Basic case
    ([2, 2, 1, 1, 1, 2, 2], 2),  # Even length array
    ([1, 1, 2, 2, 1, 1, 1], 1),  # Odd length array
    ([1], 1),  # Single element array
    ([1, 2, 1, 2, 1], 1),  # Majority element appears exactly n/2 + 1 times
    ([1, 1, 1, 1, 2, 2, 2], 1),  # Majority element at the beginning
    ([2, 2, 2, 1, 1, 1, 1], 1),  # Majority element at the end
    # Majority element after several different elements
    ([1, 2, 3, 4, 5, 5, 5, 5, 5], 5),
    # Majority element followed by several different elements
    ([1, 1, 1, 1, 1, 2, 3, 4, 5], 1),
    ([1, 2, 1, 2, 1, 2, 1], 1),  # Alternating elements with majority
    ([1, 1, 1, 1, 1, 1, 1], 1),  # All elements are the same
    ([-1, -1, -1, 2, 3], -1),  # Negative numbers
    ([2147483647, 2147483647], 2147483647),  # Maximum 32-bit integer
    ([-2147483648, -2147483648], -2147483648),  # Minimum 32-bit integer
]
# Running the tests
for nums, expected in test_cases:
    result = majorityElement_candidate(nums)
    print(f"Input: {nums}, Computed: {result}, Expected: {expected}", end=" ")
    if result == expected:
        print("Pass", end="")
    else:
        print("Fail", end="")
    print()  # New line after each test case

    result = majorityElement_sort(nums)
    print(f"Input: {nums}, Computed: {result}, Expected: {expected}", end=" ")
    if result == expected:
        print("Pass", end="")
    else:
        print("Fail", end="")
    print()  # New line after each test case

    print()  # Extra new line for separation between test cases
