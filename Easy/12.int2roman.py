def intToRoman(num):
    romanMap = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }
    roman_list = list(romanMap.items())
    # 1994 MCMXCIV
    result = ""
    for (key, value) in roman_list:
        if num >= value:
            num -= value
            result += key

    return result


def intToRoman_sample(num: int) -> str:
    Roman = ""
    storeIntRoman = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"]
    ]

    for i in range(len(storeIntRoman)):
        while num >= storeIntRoman[i][0]:
            Roman += storeIntRoman[i][1]
            num -= storeIntRoman[i][0]
    return Roman


if __name__ == '__main__':
    """
    Example 1:
    Input: num = 3
    Output: "III"
    Explanation: 3 is represented as 3 ones.
    
    Example 2:
    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.
    
    Example 3:
    Input: num = 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    # print(intToRoman(3))
    # print(intToRoman(58))
    print(intToRoman_sample(1994))
