class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        for i in range(len(prices)-1):
            j = i+1
            while j<len(prices):
                profit = prices[j] - prices[i]
                j+=1
                profitMax = max(profitMax, profit)
        return profitMax
