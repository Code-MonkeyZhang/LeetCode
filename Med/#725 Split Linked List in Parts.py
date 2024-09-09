# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListTok(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # edge cases:
        # - empty

        if head is None:
            return [None]*k

        # count length
        iter = head
        length = 0
        while iter is not None:
            iter = iter.next
            length += 1

        size = length//k
        remain = length % k

        group_size = [size]*k
        # assign remainder:
        for i in range(remain):
            group_size[i] += 1

        result = []
        iter = head
        for size in group_size:
            dummy = iter
            for _ in range(size):
                temp = iter
                iter = iter.next

            temp.next = None
            result.append(dummy)

        return result


def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# 辅助函数：将链表转换为列表（用于打印）


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # 测试用例
    solution = Solution()

    # 测试用例 1
    head1 = create_linked_list([1, 2, 3])
    k1 = 5
    result1 = solution.splitListTok(head1, k1)
    print("Test Case 1 ([1,2,3], k=5):")
    print([[val for val in linked_list_to_list(part)] if part else []
          for part in result1])

    # 测试用例 2
    head2 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k2 = 3
    result2 = solution.splitListTok(head2, k2)
    print("\nTest Case 2 ([1,2,3,4,5,6,7,8,9,10], k=3):")
    print([[val for val in linked_list_to_list(part)] if part else []
          for part in result2])
    # 测试用例 2
    head2 = create_linked_list([0, 1, 2, 3, 4])
    k2 = 3
    result2 = solution.splitListTok(head2, k2)
    print("\nTest Case 2 ([0,1,2,3,4], k=3):")
    print([[val for val in linked_list_to_list(part)] if part else []
          for part in result2])
