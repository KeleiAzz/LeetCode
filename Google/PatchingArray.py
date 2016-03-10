# coding=utf-8
#TODO figure out how it works
def minPatches(nums, n):
    '''
    Need some more understanding of this problem
    假设目前为止通过index之前的数相加所有小于等于sum的数都能得到,那么如果index这个位置上的数x小于等于sum,通过加上已经有的sum,则所有
    小于等于sum+x的数都可以得到,再看index下一个数是什么.如果x-sum=1,那么也是sum+x都可以得到.但是如果x-sum>1,那么很显然,sum+1这个数就
    肯定得不到了.所以这个时候就需要添加一个sum+1这个数到nums里面,然后sum+sum+1之内的数就都可以得到了
    :param nums:
    :param n:
    :return:
    '''
    sum = 0
    ans = 0
    index = 0

    while sum < n:
        while index < len(nums) and nums[index] <= sum:
            sum += nums[index]
            index += 1
        if sum < n:
            if index < len(nums) and nums[index] == sum + 1:
                index += 1
            else:
                ans += 1

            sum = 2 * sum + 1
    return ans
