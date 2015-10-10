__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1 = headA
        node2 = headB
        while node1 and node2:
            if node1.val > node2.val:
                node2 = node2.next
            elif node1.val < node2.val:
                node1 = node1.next
            else:
                return node1
        return None