#coding=utf-8
class Solution:
    '''
    dp表示,还剩i个硬币时,当前玩家最多能在之后那多少分.剩1个和剩2个时都是能直接全部拿掉就行.如果是两个以上,他可以选择拿1个或者拿两个,拿一个的
    话,拿的这个分数,加上剩下的硬币分数之和减去另一个玩家在剩下的硬币中最多能拿掉的分数,就是该玩家从现在开始能拿的分数.同理可以得到该玩家拿两个
    硬币的情况下可以拿掉的分数,这两个取较大的一个,就得到此时该玩家能拿掉的最大分数.
    '''
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n < 3:
            return True
        dp = [0] * n
        dp[-1] = values[-1]
        dp[-2] = values[-1] + values[-2]
        sum = [0] * n
        sum[-1] = values[-1]
        for i in range(0, n-1)[::-1]:
            sum[i] = values[i] + sum[i+1]
        for i in range(0,n-2)[::-1]:
            dp[i] = max(values[i]+sum[i+1]-dp[i+1], values[i]+values[i+1]+sum[i+2]-dp[i+2])
        return True if dp[0]>=sum[0]-dp[0] else False
s = Solution()
print s.firstWillWin([1,2,4])