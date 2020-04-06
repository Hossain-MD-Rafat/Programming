#arr[7,1,5,3,6,4]

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if (prices[i] - prices[i - 1]) > 0:
            max_profit += (prices[i] - prices[i - 1])

    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))






    #
    # max_profit = profit = 0
    # low = prices[0]
    # for price in prices:
    #     if low < price:
    #         profit = price - low
    #         max_profit += profit
    #         low = price
    #     else:
    #         low = price
    #
    # return max_profit


