class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def generate(nums, l, r):
    if l > r:
        return None
    min_num, min_idx = nums[l], l
    for i in range(l, r+1):
        if nums[i] < min_num:
            min_num = nums[i]
            min_idx = i

    root = TreeNode(min_num)
    root.left = generate(nums, l, min_idx - 1)
    root.right = generate(nums, min_idx + 1, r)

    return root



def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)


nums = [2,4,1,6,3,5,0,8,9]
root = generate(nums, 0, len(nums)-1)
inorder(root)