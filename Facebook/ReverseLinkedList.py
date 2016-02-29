# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fix_head = ListNode(0)
        fix_head.next = head
        ptr = head.next
        # head.next = None
        while ptr is not None:
            print 'current node:', ptr.val
            tmp = ptr.next
            ptr.next = fix_head.next
            fix_head.next = ptr
            ptr = tmp

        return fix_head.next

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        nxt = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return nxt

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

s = Solution()

s.reverseList(a)
