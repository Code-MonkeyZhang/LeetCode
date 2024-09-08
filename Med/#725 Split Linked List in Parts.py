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
        # - only one element
        # - k > length

        # edge case: empty
        if head is None:
            return [None]*k

        # 创建输出的结果，根据描述 一共有k个元素
        result = [None]*k

        # edge case: only 1 element
        if head.next is None:
            return [head]+[None]*(k-1)

        # 先数len是多少
        iter = head
        length = 0
        while iter is not None:
            iter = iter.next
            length += 1

        # edge case: k比链表的长度还长
        # 根据问题描述，直接剁成一个个
        if k > length:
            iter = head
            for i in range(len(result)):
                if iter is not None:
                    # 赋值
                    result[i] = iter
                    # 切尾
                    temp = result[i].next
                    result[i].next = None
                    # 推进到下一个
                    iter = temp
            return result

        # split_len代表每个元素应该有的数量
        # 举例
        # length=9 k=3
        # split_length=9//3=3
        split_len = length//k

        # remainder：要多分配的个数
        # 比如 length=10, k=3 那么 remainder=1
        remainder = length % k

        iter = head
        # 遍历输出中的每一个元素
        for i in range(len(result)):
            result[i] = iter

            current_len = split_len + (1 if i < remainder else 0)

            # 移动到当前部分的最后一个节点
            for _ in range(current_len - 1):
                if iter:
                    iter = iter.next

            # 切断链接并移动到下一部分的开始
            if iter:
                temp = iter.next
                iter.next = None
                iter = temp

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
