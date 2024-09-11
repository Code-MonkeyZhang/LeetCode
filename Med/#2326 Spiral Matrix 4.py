from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
"""


class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        row_Min, row_Max = 0, n-1
        column_Min, column_Max = 1, m-1

        row_index, column_index = 0, 0

        result = [[-1]*n for _ in range(m)]
        iter = head
        while iter is not None:
            # moving right
            while row_index <= row_Max and iter is not None:
                result[column_index][row_index] = iter.val
                # increment row_index
                iter = iter.next
                row_index += 1

            row_index -= 1
            # move down by 1 position
            column_index += 1

            # down
            while column_index <= column_Max and iter is not None:
                result[column_index][row_index] = iter.val
                iter = iter.next
                column_index += 1

            column_index -= 1
            row_index -= 1
            # left
            while row_index >= row_Min and iter is not None:
                result[column_index][row_index] = iter.val
                iter = iter.next
                row_index -= 1

            row_index += 1
            column_index -= 1

            # up
            while column_index >= column_Min and iter is not None:
                result[column_index][row_index] = iter.val
                iter = iter.next
                column_index -= 1

            column_index += 1
            row_index += 1

            row_Max -= 1
            column_Max -= 1
            row_Min += 1
            column_Min += 1

        return result


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Test the solution
solution = Solution()

# Test case 1
m1, n1 = 3, 5
head1 = create_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
result1 = solution.spiralMatrix(m1, n1, head1)
print("Test case 1 result:")
for row in result1:
    print(row)

# Test case 2
m2, n2 = 1, 4
head2 = create_linked_list([0, 1, 2])
result2 = solution.spiralMatrix(m2, n2, head2)
print("\nTest case 2 result:")
for row in result2:
    print(row)

# Test case 3
m2, n2 = 10, 1
head2 = create_linked_list([8, 24, 5, 21, 10, 11, 11, 12, 6, 17])
result2 = solution.spiralMatrix(m2, n2, head2)
print("\nTest case 2 result:")
for row in result2:
    print(row)
