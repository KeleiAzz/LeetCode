__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head and head.next is None:
            return []
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        if n == len(nodes):
            return nodes[1]
        target = nodes[0 - n]
        nodes[0 - n - 1].next = target.next
        return nodes[0]
