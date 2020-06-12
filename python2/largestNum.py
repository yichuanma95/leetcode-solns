'''
Problem 179: Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
'''

def strCompare(x, y):
    if x == y:
        return 0
    
    if x + y > y + x:
        return -1
    else:
        return 1

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = map(lambda x: str(x), nums)
        strs.sort(cmp = strCompare)
        if strs[0] == '0':
            return '0'
        
        return ''.join(strs)
