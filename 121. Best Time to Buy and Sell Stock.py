class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_of_price = float('inf')
        max_profit = 0
        for price in prices:
            min_of_price = min(min_of_price, price)
            profit = price - min_of_price
            max_profit = max(max_profit, profit)
        return max_profit