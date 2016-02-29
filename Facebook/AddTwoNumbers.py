# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fix_head = ListNode(-1)
        p = fix_head
        carry = 0
        while l1 or l2 or carry:
            a = 0
            if l1:
                a = l1.val
                l1 = l1.next
            b = 0
            if l2:
                b = l2.val
                l2 = l2.next
            s = a + b + carry
            p.next = ListNode(s % 10)
            p = p.next
            carry = s / 10
        return fix_head.next