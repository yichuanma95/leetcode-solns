'''
Problem 189: Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:
* 1 <= nums.length <= 2 * 10^4
* It's guaranteed that nums[i] fits in a 32 bit-signed integer.
* k >= 0

Follow-ups:
-Try to come up as many solutions as you can; there are at least 3 different ways to solve
this problem.
-Could you do it in-place with O(1) extra space?

I have 3 different solutions to this problem.
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ (Solution, list of int, int) -> NoneType
        
        Preconditions:
        * k >= 0
        * Each number in nums is a 32-bit signed integer
        * nums has at least 1 element, but no more than 20,000
        
        Shifts each element in nums to the right by k steps. This function modifies the
        list in-place. This is the O(n) space solution.
        
        >>> soln = Solution()
        >>> soln.rotate([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
        >>> soln.rotate([-1, -100, 3, 99], 2)
        [3, 99, -1, -100]
        """
        
        nums_length = len(nums)
        
        # Create a new list that will contain all the elements in nums shifted to the right
        # by k steps. It will initially contain all 0's.
        nums_shifted = [0] * nums_length
        
        # Place each element in nums into the new list, shifted k spots.
        for i, num in enumerate(nums):
            nums_shifted[(i+k)%nums_length] = num
            
        # Move each element in the shifted list back to the original list
        for i, num in enumerate(nums_shifted):
            nums[i] = num


    def rotate_constant_space(self, nums: List[int], k: int) -> None:
        """
        This is the constant-space solution that uses the array reversal method.
        """
        
        k = k % len(nums)
        
        self.reverse_part(nums, 0)
        self.reverse_part(nums, 0, k - 1)
        self.reverse_part(nums, k)
        
    def reverse_part(self, nums, left, right = -2):
        ''' (Solution, list of int, int, int) -> NoneType
        
        Reverses the elements in nums from index left up to and including index right.
        
        soln = Solution()
        >>> xs = [1, 2, 3, 4, 5, 6, 7]
        >>> soln.reverse_part(xs, 0, 4)
        >>> xs = [5, 4, 3, 2, 1, 6, 7]
        '''
        
        if right == -2:
            right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    def rotate_short(self, nums: List[int], k: int) -> None:
        '''
        This is a short, Pythonic solution.
        '''

        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
