class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit = 0
        if len(prices) <= 1:
            return 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

s = Solution()
print(s.maxProfit([0, 5, 5, 6, 2, 1, 1, 3]))