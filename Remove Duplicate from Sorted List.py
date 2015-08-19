__author__ = 'keleigong'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        node = head
        nd = node
        while nd:
            while nd.next and nd.val == nd.next.val:
                nd.next = nd.next.next
            nd = nd.next
        return node
