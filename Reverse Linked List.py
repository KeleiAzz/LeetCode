__author__ = 'keleigong'
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
        if head:
            node = head.next
            head.next =None
            prev = head
            while True:
                if node:
                    temp = node.next
                    node.next = prev
                    prev = node
                    node = temp
                else:
                    return prev
        else:
            return head