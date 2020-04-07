'''
Problem 485: Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Notes:
-The input array will only contain 0 and 1.
-The length of input array is a positive integer and will not exceed 10,000

Solution memory usage: 12.6 MB, less than 100% of Python3 submissions
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStreak = 0
        currentStreak = 0
        
        for n in nums:
            if n == 1:
                currentStreak += 1
            else:
                if currentStreak > maxStreak:
                    maxStreak = currentStreak
                currentStreak = 0
        
        return max(maxStreak, currentStreak)
