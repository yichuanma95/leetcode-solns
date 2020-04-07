'''
Problem 136: Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Solution runtime: 88ms, faster than 96.93% of Python3 submissions
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqueNums = {}
        
        for num in nums:
            if num in uniqueNums:
                uniqueNums[num] += 1
            else:
                uniqueNums[num] = 1
        
        for key in uniqueNums.keys():
            if uniqueNums[key] == 1:
                return key
        
        return -1
