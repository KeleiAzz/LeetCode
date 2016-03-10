class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LinkedList(object):
    '''
    Double linked list
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        # self.capacity = capacity

    def appendHead(self, node):
        node.pre, node. next = None, self.head
        if self.head:
            self.head.pre = node

        self.head = node

        if not self.tail:
            self.tail = self.head
        self.size += 1

    def remove(self, node):
        if not node:
            return None
        pre, next = node.pre, node.next
        if pre:
            pre.next = next
        if next:
            next.pre = pre

        if node == self.head:
            self.head = next
        if node == self.tail:
            self.tail = pre
        self.size -= 1
        return node

    def removeTail(self):
        return self.remove(self.tail)

    def advance(self, node):
        self.remove(node)
        self.appendHead(node)


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.record = {}
        self.linkedlist = LinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.record:
            return -1
        self.linkedlist.advance(self.record[key])
        return self.record[key].val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.record:
            node = ListNode(key, value)
            self.linkedlist.appendHead(node)
            self.record[key] = node
            if self.linkedlist.size > self.capacity:
                del self.record[self.linkedlist.removeTail().key]
        else:
            self.record[key].val = value
            self.linkedlist.advance(self.record[key])
