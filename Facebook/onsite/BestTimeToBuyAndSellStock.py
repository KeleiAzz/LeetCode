def maxProfit(prices):
    min_price = float('INF')
    profit = 0
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profit = max(profit, prices[i] - min_price)
    return profit

def maxProfitII(prices):
    profit = 0
    for i in range(1, len(prices)):
        profit += prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0
    return profit
    # return sum([max(0, j - i) for i, j in zip(prices[:-1], prices[1:])])

def maxProfitIII(prices):
    '''
    on the first run, first_max_profit represents up to day i, the maximum profit get by one transaction. on the second
    run, calculate the max profit can be after day i.
    :param prices:
    :return:
    '''
    first_max_profit = [0] * len(prices)
    min_price = float('inf')
    max_profit = 0
    for i, p in enumerate(prices):
        min_price = min(p, min_price)
        profit = p - min_price
        max_profit = max(profit, max_profit)
        first_max_profit[i] = max_profit

    max_price = -float('inf')
    for i in range(len(prices)-1,0,-1):
        max_price = max(prices[i], max_price)
        profit = max_price - prices[i]
        max_profit = max(max_profit, first_max_profit[i-1] + profit)
    return max_profit
