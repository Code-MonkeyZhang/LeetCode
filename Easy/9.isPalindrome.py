"""
Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false

Example 3:
Input: x = 10
Output: false
"""

"""
Ideas/thoughts:
1. reverse the entire number, see if it is equal to the original number
2. how to reverse?

complexity: O(n)
"""

def isPalindrome(x):

    # reverse the num
    temp = x
    reverse_num = 0
    while temp != 0:
        digit = temp % 10  # get the last digit
        reverse_num = 10 * reverse_num + digit  # move the digit to the left
        temp = temp // 10  # update the original number

    return reverse_num == x

def isPalindrome_half(x):

    # basic case: neg num & ending with 0
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    # reverse the num
    temp = x
    reverse_num = 0
    while temp > reverse_num:
        digit = temp % 10  # get the last digit
        reverse_num = 10 * reverse_num + digit  # move the digit to the left
        temp = temp // 10  # update the original number, //是整除

    """
    why or reverse_num // 10 == temp?? 
    because when the number is odd, like 12321
    After while the loop:
    temp: 12
    reverse num: 123 
    reverse_num // 10 can get rid of that 3
    """
    return reverse_num == temp or reverse_num // 10 == temp

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

if __name__ == '__main__':
    # test_twoSum()
    test_isPalindrome()

