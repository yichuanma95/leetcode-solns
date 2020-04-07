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

import functools

def strCompare(x: str, y: str) -> int:
    if x == y:
        return 0
    
    if x + y > y + x:
        return 1
    else:
        return -1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs: List[str] = list(map(lambda x: str(x), nums))
        strs.sort(key = functools.cmp_to_key(strCompare), reverse = True)
        if strs[0] == '0':
            return '0'
        
        return ''.join(strs)
