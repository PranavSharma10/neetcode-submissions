class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            profitMax = max(profitMax, price - minPrice)
        return profitMax
