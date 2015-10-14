__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        # fixHead = ListNode(0)
        # fixHead = head
        pointer = head
        # previous = head
        while pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        if head.val == val:
            return head.next
        return head
