# cache = {}
def addOperator(nums, target):
    '''
    Seems work, how to optimize?
    :param nums:
    :param target:
    :return:
    '''
    if int(nums) == target or int(nums) == -target:
        return True
    for i in range(1, len(nums)):
        subnum = int(nums[:i])
        if addOperator(nums[i:], target - subnum) or addOperator(nums[i:], target + subnum):
            return True
    return False

print addOperator('43868643', 52)

