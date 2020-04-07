'''
Problem 169: Majority Element

Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

Solution runtime: 176ms, faster than 93.83% of Python3 submissions

Solution memory usage: 14 MB, less than 100% of Python3 submissions
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}
        majorityFactor: int = len(nums) // 2
            
        for num in nums:
            if num not in elems:
                elems[num] = 1
            else:
                elems[num] += 1
            if elems[num] > majorityFactor:
                return num
        
        return -1
