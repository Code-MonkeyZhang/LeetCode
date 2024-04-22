"""
Example 1:

Input: s = "III"
Output: 3

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

def roman2Int(s: str):
    romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    skip_next = False

    for i in range(len(s)):
        if skip_next:
            skip_next = False
            continue
        # basic case: 如果只有一个数字,是啥就是啥
        if len(s) == 1:
            return romanMap[s[i]]

        # compare it to the next one
        # if it's smaller, do the sub rule
        if ((i + 1) in range(len(s))) and romanMap[s[i]] < romanMap[s[i + 1]]:
            result += romanMap[s[i + 1]] - romanMap[s[i]]
            skip_next = True
        else:
            result += romanMap[s[i]]

    return result

def roman2Int2(s: str):
    romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(s)):
        # basic case: 如果只有一个数字,是啥就是啥
        if len(s) == 1:
            return romanMap[s[i]]

        # compare it to the next one
        # make sure i is not the last index
        # then if it's smaller, do the sub, otherwise add
        if ((i + 1) in range(len(s))) and romanMap[s[i]] < romanMap[s[i + 1]]:
            result -= romanMap[s[i]]
        else:
            result += romanMap[s[i]]

    return result


if __name__ == '__main__':
    result1 = roman2Int('III')
    result2 = roman2Int('LVIII')
    result3 = roman2Int('MCMXCIV')
    print(result1)
    print(result2)
    print(result3)
