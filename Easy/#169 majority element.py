def majorityElement(nums):
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


# Test cases
test_cases = [
    ([3, 2, 3], 3),  # Expected output: 3
    ([2, 2, 1, 1, 1, 2, 2], 2),  # Expected output: 2
    ([1, 1, 2, 2, 1, 1, 1], 1),  # Expected output: 1
]

# Running the tests
for nums, expected in test_cases:
    result = majorityElement(nums)
    print(f"Input: {nums}, Computed: {result}, Expected: {expected}")
