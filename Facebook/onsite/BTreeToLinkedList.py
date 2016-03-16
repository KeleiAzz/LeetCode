class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


def convertToLinkedList(root):
    '''
    convert a binary tree to linkedlist by using a stack to perform inorder traversal
    :param root:
    :return:
    '''
    if not root:
        return None
    node = root
    stack = []
    fix_head = ListNode(-1)
    ptr = fix_head
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            tmp = ListNode(node.val)
            tmp.pre = ptr
            ptr.next = tmp
            ptr = tmp
            node = node.right
    fix_head.next.pre = None
    return fix_head.next

def print_list(head):
    node = head
    while node:
        print node.val,
        node = node.next
    # while node:
    #     print node.val,
    #     node = node.pre
    print ''

def convertToDLL(root):
    '''
    convert a binary to doubly linkedlist by using a stack to perform a inorder traversal
    :param root:
    :return:
    '''
    if not root:
        return None
    node = root
    stack = []
    fix_head = TreeNode(-1)
    ptr = fix_head
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node.left = ptr
            ptr.right = node
            ptr = node
            node = node.right
    fix_head.right.left = None
    return fix_head.right


def convertToDLLRecur(root):
    '''
    convert binary tree to DLL in a recursive way.
    :param root:
    :return:
    '''
    fixPrePtr(root)
    return fixNextPtr(root)

prePtr = None
def fixPrePtr(root):
    '''
    Changes left pointers to work as previous pointers
    in converted DLL
    The function simply does inorder traversal of
    Binary Tree and updates
    left pointer using previously visited node
    :param root:
    :return:
    '''
    global prePtr
    if root is not None:
        fixPrePtr(root.left)
        root.left = prePtr
        prePtr = root
        fixPrePtr(root.right)

def fixNextPtr(root):
    # Changes right pointers to work as nexr pointers in
    # converted DLL
    prev = None
    # Find the right most node in BT or last node in DLL
    while(root and root.right != None):
        root = root.right

    # Start from the rightmost node, traverse back using
    # left pointers
    # While traversing, change right pointer of nodes
    while(root and root.left != None):
        prev = root
        root = root.left
        root.right = prev

    # The leftmost node is head of linked list, return it
    return root

def print_DLL(head):
    node = head
    while node:
        print node.val,
        node = node.right
    print ''
    node = head
    while node.right:
        node = node.right
    while node:
        print node.val,
        node = node.left
    print ''


root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right.left = TreeNode(36)
head = convertToLinkedList(root)
print_list(head)

head2 = convertToDLLRecur(root)
print_DLL(head2)