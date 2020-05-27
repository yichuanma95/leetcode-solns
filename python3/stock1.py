'''
Problem 121: Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share
of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Not
7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' (Solution, list of int) -> int
        
        Return the maximum profit that can be achieved from buying and selling once given
        a list of stock prices.
        
        >>> soln = Solution()
        >>> soln.maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> soln.maxProfit([7, 6, 4, 3, 1])
        0
        '''
        
        if len(prices) == 0:
            return 0
        
        # Keep track of the best profit found so far
        max_profit = 0
        # Keep track of the best price to buy stock.
        best_buying_price = prices[0]
        
        # For each price, the max profit is the max between the current max so far and
        # the profit (or loss) if the stock was sold at the current price (after it was
        # purchased). If the current  price is lower than the best purchase price so far,
        # this price will become the new best purchase price.
        prices_length = len(prices)
        for i in range(1, prices_length):
            price = prices[i]
            max_profit = max(max_profit, price - best_buying_price)
            best_buying_price = min(best_buying_price, price)
        
        return max_profit
