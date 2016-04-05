class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(arr, s, e):
    if s >= len(arr) or e >= len(arr):
        return arr
    for i in range((e-s+1)/2):
        print ' '
        arr[s+i], arr[e-i] = arr[e-i], arr[s+i]
    print arr
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(arr, 1, 4)


def reverseLinkedList(head, s, e):
    if s >= e:
        return head
    dummy_head = ListNode(-1)
    dummy_head.next = head
    tmp = dummy_head
    fix_head = start = None
    for i in range(e+1):
        if i == s - 1:
            fix_head = tmp
        if i == s:
            start = tmp
        if tmp is None:
            return head
        tmp = tmp.next
    if not start or not fix_head:
        return head
    cur = start.next
    for i in range(e-s):
        start.next = cur.next
        cur.next = fix_head.next
        fix_head.next = cur
        cur = start.next
    return dummy_head.next
