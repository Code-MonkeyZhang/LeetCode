# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def reverseBetween(self, head, left, right):
        # 在这里粘贴您的reverseBetween函数的实现
        if head.next is None and left == right:
            return head

        dummy = ListNode(0, head)
        start = dummy
        curr = start.next
        for _ in range(left-1):
            start = start.next
            curr = curr.next
        end = curr.next

        for _ in range(right-left):
            temp = end.next
            end.next = curr
            curr = end
            end = temp

        temp = start.next
        start.next = curr
        temp.next = end

        return dummy.next


# 测试用例
def test_reverse_between():
    solution = Solution()

    # 测试用例 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseBetween(head1, 2, 4)
    assert linked_list_to_list(result1) == [
        1, 4, 3, 2, 5], "Test case 1 failed"

    # 测试用例 2
    head2 = create_linked_list([5])
    result2 = solution.reverseBetween(head2, 1, 1)
    assert linked_list_to_list(result2) == [5], "Test case 2 failed"

    # 测试用例 3: 反转整个链表
    head3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = solution.reverseBetween(head3, 1, 5)
    assert linked_list_to_list(result3) == [
        5, 4, 3, 2, 1], "Test case 3 failed"

    # 测试用例 4: 反转中间部分
    head4 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    result4 = solution.reverseBetween(head4, 3, 5)
    assert linked_list_to_list(result4) == [
        1, 2, 5, 4, 3, 6, 7], "Test case 4 failed"

    print("All test cases passed!")


# 运行测试
if __name__ == "__main__":
    test_reverse_between()
