# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0, None)
        head = l3
        carry = 0

        while True:
            a = l1.val
            b = l2.val
            addition = a + b + carry
            if addition >= 10:
                addition -= 10
                carry = 1
            else:
                carry = 0
            head.val = addition

            # When reach the end of both arrays
            if l1.next is None and l2.next is None:
                if carry == 1:
                    head.next = ListNode(1, None)
                return l3
            else:
                # when one of them is None，意味着有的算
                # 给L1 L2 和 head 赋值
                l1 = l1.next if l1.next is not None else ListNode(0, None)
                l2 = l2.next if l2.next is not None else ListNode(0, None)
                head.next = ListNode(0, None)
                head = head.next


def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Test cases
sol = Solution()

# Test case 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = sol.addTwoNumbers(l1, l2)
print("Test case 1 result:")
print_list(result)  # Expected: 7 -> 0 -> 8

# Test case 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = sol.addTwoNumbers(l1, l2)
print("Test case 2 result:")
print_list(result)  # Expected: 0

# Test case 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = sol.addTwoNumbers(l1, l2)
print("Test case 3 result:")
print_list(result)  # Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1

# Additional test cases

# Test case 4: Different lengths
l1 = create_linked_list([1, 8])
l2 = create_linked_list([0])
result = sol.addTwoNumbers(l1, l2)
print("Test case 4 result:")
print_list(result)  # Expected: 1 -> 8

# Test case 5: One list is longer
l1 = create_linked_list([5])
l2 = create_linked_list([5, 9, 9])
result = sol.addTwoNumbers(l1, l2)
print("Test case 5 result:")
print_list(result)  # Expected: 0 -> 0 -> 0 -> 1

# Test case 6: Carry at the end
l1 = create_linked_list([9, 9, 9])
l2 = create_linked_list([1])
result = sol.addTwoNumbers(l1, l2)
print("Test case 6 result:")
print_list(result)  # Expected: 0 -> 0 -> 0 -> 1

# Test case 7: Both lists with multiple carries
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = sol.addTwoNumbers(l1, l2)
print("Test case 7 result:")
print_list(result)  # [8,9,9,9,0,0,0,1]
