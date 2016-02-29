__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        if head.next and head.next.next:
            head.next = self.swapPairs(head.next)
        return tmp
