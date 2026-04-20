class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')     # starts "infinitely high" so first price beats it
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit