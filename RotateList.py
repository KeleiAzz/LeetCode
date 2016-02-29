__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            n = 1
            node = head
            while node.next:
                n += 1
                node = node.next
            k = k % n
            if k == 0:
                # node.next = None
                return head
            node.next = head
            node = head
            for i in range(n-k-1):
                node = node.next
            res = node.next
            node.next = None
            return res
        else:
            return head
