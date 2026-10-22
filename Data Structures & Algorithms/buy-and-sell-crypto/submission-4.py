class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        sellDay = 1
        profit = 0

        while sellDay < len(prices):
            if prices[buyDay] >= prices[sellDay]:
                buyDay = sellDay 
            else:
                profit = max(profit, prices[sellDay] - prices[buyDay])
            sellDay += 1
        
        return profit