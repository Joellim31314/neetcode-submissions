class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0] #its fine to initialise the first day as smallest as it pass the if condition anyway
        profit = 0 #you can assume profit is 0 as in example 2 it explain "No profitable transactions can be made, thus the max profit is 0."
        for value in prices:
            if value < smallest:
                smallest = value 
            if value - smallest > profit:
                profit =  value - smallest
        return profit 
            

        