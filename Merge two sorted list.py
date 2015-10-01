__author__ = 'keleigong'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        # pointer = head.next
        # head.next = pointer
        prev = head
        while True:
            if l1 and l2:
                if l1.val > l2.val:
                    prev.next = l2
                    # pointer.next = None
                    # pointer = pointer.next
                    l2 = l2.next
                else:
                    prev.next = l1
                    l1 = l1.next
                prev = prev.next
            elif l1:
                prev.next = l1
                break
            elif l2:
                prev.next = l2
                break
            else:
                break
        return head.next


