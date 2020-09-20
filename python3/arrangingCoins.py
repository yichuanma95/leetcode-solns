'''
Problem 441: Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every kth row
must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.find_coin_rows(0, n, n)
    
    def find_coin_rows(self, low, high, n):
        if low > high:
            return -1
        middle = (low + high) // 2
        y = (middle * (middle + 1)) // 2
        y_plus = ((middle + 1) * (middle + 2)) // 2
        y_minus = (middle * (middle - 1)) // 2
        if n == y or n > y and n < y_plus:
            return middle
        if n < y and n > y_minus:
            return middle - 1
        if n < y:
            return self.find_coin_rows(low, middle - 1, n)
        return self.find_coin_rows(middle + 1, high, n)
