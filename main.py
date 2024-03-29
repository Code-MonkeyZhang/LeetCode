def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # reverse the num
    temp = x
    reverse_num = 0
    while temp != 0:
        digit = temp % 10  # get the last digit
        reverse_num = 10 * reverse_num + digit  # move the digit to the left
        temp = temp // 10  # update the original number 

    return reverse_num == x


def isPalindrome_half(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    # reverse the num
    temp = x
    reverse_num = 0
    while temp > reverse_num:
        digit = temp % 10  # get the last digit
        reverse_num = 10 * reverse_num + digit  # move the digit to the left
        temp = temp // 10  # update the original number

    return reverse_num == temp or reverse_num // 10 == temp


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # create hashtable
    numMap = {}
    size = len(nums)

    # range(0,4): 0,1,2,3,4
    for i in range(size):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(size):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []


def test_twoSum():
    test1 = [2, 7, 11, 15]
    target1 = 9
    test2 = [3, 2, 4]
    target2 = 6
    test3 = [3, 3]
    target3 = 6

    print(twoSum(test1, target1))
    print(twoSum(test2, target2))
    print(twoSum(test3, target3))


def test_isPalindrome():
    test1 = 13231
    test2 = 123
    test3 = 1001
    result1 = isPalindrome(test1)
    result2 = isPalindrome(test2)
    result3 = isPalindrome(test3)
    print(result1)
    print(result2)
    print(result3)

    result1 = isPalindrome_half(test1)
    result2 = isPalindrome_half(test2)
    result3 = isPalindrome_half(test3)
    print(result1)
    print(result2)
    print(result3)


def roman2Int(s: str):
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    skip_next = False
    for i in range(len(s)):
        if skip_next:
            skip_next = False
            continue
        if len(s) == 1:
            return romanMap[s[i]]
        # compare it to the next one
        # if it's smaller, do the sub rule
        if ((i+1) in range(len(s))) and romanMap[s[i]] < romanMap[s[i + 1]]:
            result += romanMap[s[i + 1]] - romanMap[s[i]]
            skip_next = True
        else:
            result += romanMap[s[i]]

    return result


if __name__ == '__main__':
    # test_twoSum()
    # test_isPalindrome()
    result1 = roman2Int('III')
    result2 = roman2Int('LVIII')
    result3 = roman2Int('MCMXCIV')
    print(result1)
    print(result2)
    print(result3)
