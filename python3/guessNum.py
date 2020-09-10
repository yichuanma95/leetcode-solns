'''
Problem 374: Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6

Solution memory usage: 13.6 MB, less than 93.08% of Python3 submissions
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.binary_search_for_guessing(1, n)
    
    def binary_search_for_guessing(self, low, high):
        if low > high:
            return -1
        middle = (low + high) // 2
        if guess(middle) == 0:
            return middle
        if guess(middle) < 0:
            return self.binary_search_for_guessing(low, middle - 1)
        return self.binary_search_for_guessing(middle + 1, high)
    