# coding=utf-8
class Solution:
    '''
    dp[i]表示还剩i个硬币时,此时先手的人的输赢情况.如果他要赢,只要他拿一个或者拿两个这两种方式中,有一种能使他稳赢就行.而他要稳赢的话,就是他
    拿完这一个或者两个之后,另外一个人不论拿一个还是拿两个都赢不了.
    '''
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n == 1:
            return True
        if n == 2:
            return True
        if n == 3:
            return False
        if n == 4:
            return True
        dp = [False] * (n + 1)
        dp[1:5] = [True, True, False, True]
        for i in range(5, n+1):
            dp[i] = (dp[i-2] and dp[i-3]) or (dp[i-3] and dp[i-4])
        return dp[n]