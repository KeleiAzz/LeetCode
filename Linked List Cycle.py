__author__ = 'keleigong'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        nd = head
        visited = []
        while nd:
            if nd.val == 'visited':
                return True
            nd.val = 'visited'
            nd = nd.next

        return False


