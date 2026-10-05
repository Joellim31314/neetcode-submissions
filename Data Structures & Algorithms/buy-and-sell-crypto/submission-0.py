class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for i, value in enumerate(prices):
            if value < smallest:
                smallest = value 
            if value - smallest > profit:
                profit =  value - smallest
        return profit 
            

        