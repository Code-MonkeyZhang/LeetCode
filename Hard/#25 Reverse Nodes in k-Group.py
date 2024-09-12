# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def getKth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # 反转组内节点
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 辅助函数：打印链表


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


# 测试代码
if __name__ == "__main__":
    # 测试用例
    values = [1, 2, 3, 4, 5]
    k = 2

    # 创建链表
    head = create_linked_list(values)

    # 打印原始链表
    print("Original list:")
    print_linked_list(head)

    # 执行翻转
    solution = Solution()
    reversed_head = solution.reverseKGroup(head, k)

    # 打印翻转后的链表
    print(f"List after reversing every {k} nodes:")
    print_linked_list(reversed_head)