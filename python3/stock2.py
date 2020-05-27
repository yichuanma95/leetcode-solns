'''
Problem 122: Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the
stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy
on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging
multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
* 1 <= prices.length <= 3 * 10 ^ 4
* 0 <= prices[i] <= 10 ^ 4
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' (Solution, list of int) -> int
        
        Returns the max profit that can be achieved over multiple transactions given a list
        of stock prices.
        
        >>> soln = Solution()
        >>> soln.maxProfit([7, 1, 5, 3, 6, 4])
        7
        >>> soln.maxProfit([1, 2, 3, 4, 5])
        4
        >>> soln.maxProfit([7, 6, 4, 3, 1])
        0
        '''
        
        # Price at previous purchase, to determine the profit from selling next time
        buying_price = 10001
        selling_price = 10001
        profits = 0
        
        # For each price, if the price is lower than the current selling price, the
        # stock should be sold the previous day, then purchased again on the current day.
        # Selling price is updated each day to be price on previous day.
        for price in prices:
            if price < selling_price:
                profits += (selling_price - buying_price)
                buying_price = price
            selling_price = price
            
        return profits + selling_price - buying_price
