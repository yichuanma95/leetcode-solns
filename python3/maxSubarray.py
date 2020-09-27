'''
Problem 53: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which\
has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up: If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ''' (Solution, list of int) -> int
        
        Find the contiguous subarray in nums with the largest sum and return it.
        
        >>> soln = Solution()
        >>> soln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        '''
        
        # The following is a dynamic programming approach to the problem
        
        nums_length = len(nums)
        
        # Initialize an array for storing the maximum subarray sum found so far at each index
        # i in nums.
        max_sums = [0] * nums_length
        
        # Start finding the max subarray sum with the base case: first number in nums
        max_sums[0] = nums[0]
        
        # Recursively find the max subarray sum at index i for 0 < i < nums_length.
        for i in range(1, nums_length):
            max_sums[i] = max(max_sums[i-1] + nums[i], nums[i])
        
        # Solution is the biggest element in max_sums
        return max(max_sums)
    