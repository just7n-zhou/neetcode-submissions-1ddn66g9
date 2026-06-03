class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy > p:
                buy = p 
            profit = max(profit, p - buy)
        
        return profit