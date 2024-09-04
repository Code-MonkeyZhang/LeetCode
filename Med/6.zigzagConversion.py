class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s

        # create rows list to store str for each row
        rows = [""]*numRows
        current_row = 0
        step = 1

        for char in s:
            rows[current_row] += char

            # if it reaches the last char in the str
            if current_row == numRows-1:
                # step becomes going backward
                step = -1
            # if it returns to the begining
            elif current_row == 0:
                # step becomes moving forward again
                step = 1

            current_row += step

        # finally combine all rows to one str
        return ''.join(rows)


def test_solution():
    solution = Solution()

    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("ABCDEF", 2, "ACEBDF"),
    ]

    for i, (s, numRows, expected) in enumerate(test_cases, 1):
        result = solution.convert(s, numRows)
        print(f"Test Case {i}:")
        print(f"Input: s = '{s}', numRows = {numRows}")
        print(f"Expected Output: '{expected}'")
        print(f"Actual Output: '{result}'")
        print("Status: ", "PASS" if result == expected else "FAIL")
        print()


if __name__ == "__main__":
    test_solution()
