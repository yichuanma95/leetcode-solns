'''
Problem 167. Two Sum II-Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that
they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the
target, where index1 must be less than index2.

Note: Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same
element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Solution runtime: 44ms, faster than 93.73% of Python submissions
'''

class Solution(object):
    def twoSum(self, numbers, target):
        ''' (Solution, list of ints, int) -> list of ints
        
        Return the indices of two numbers in the given list such that those two numbers in
        the list add up to the given target.
        
        >>> soln = Solution()
        >>> soln.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        '''
        
        # Set up a dictionary to store numbers and their respective indices in nums.
        num_to_index = {}
        
        # Loop through nums to find a pair of indices that refer to numbers in nums that add
        # up to target.
        length = len(numbers)
        for i in range(length):
            num = numbers[i]
            diff_from_target = target - num
            
            # If the difference between the current number and target is in num_to_index,
            # a solution has been found.
            if diff_from_target in num_to_index:
                result = [num_to_index[diff_from_target] + 1, i + 1]
                result.sort()
                return result
            
            # Otherwise, add the current number and its index to num_to_index.
            num_to_index[num] = i
