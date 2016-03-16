# TODO maybe implement the heap instead of using heapq module.
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        fix_head = ListNode(-1)
        p = fix_head
        queue = [(l.val, l) for l in lists if l]
        heapq.heapify(queue)
        while queue:
            val, node = heapq.heappop(queue)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(queue, (node.next.val, node.next))
        return fix_head.next


