class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = float('INF')
        sell = -float('INF')
        max_profit = 0
        for p in prices:
            if p > sell:
                sell = p
                max_profit = max(sell-buy, max_profit)
            if buy > p:
                buy = p
                sell = p
        return max_profit