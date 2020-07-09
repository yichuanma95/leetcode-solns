'''
Problem 217: Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it
should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ''' (Solution, list of int) -> bool
        
        Returns True iff there exists a duplicate value in nums.
        
        >>> soln = Solution
        >>> soln.containsDuplicate([1, 2, 3, 1])
        True
        >>> soln.containsDuplicate([1, 2, 3, 4])
        False
        '''
        
        # Define a set which contains all distinct values in nums
        num_set = set(nums)
        
        # If the length of nums is different from that of the set, there is a duplicate
        # value in nums.
        return len(num_set) != len(nums)
