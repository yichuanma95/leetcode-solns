'''
Problem 11: Container With Most Water

Given n non-negative integers a_1, a_2, ...a_n, where each represents a point at coordinate
(i, a_i). n vertical lines are drawn such that the two endpoints of line i is at (i, a_i) and
(i, 0). Find two lines, which together with x-axis forms a container, such that the
container contains the most water.

Note: You may not slant the container and n is at least 2.

  ^
  |
8 +   #         X
7 +   #---------X---#
6 +   # X       X   #
5 +   # X   X   X   #
4 +   # X   X X X   #
3 +   # X   X X X X #
2 +   # X X X X X X #
1 + X # X X X X X X #
0 +------------------->

Figure 1: The above vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7]. In
this case, the max area of water (blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ''' (Solution, list of int) -> int
        
        Precondition: length of height is >= 2
        
        Returns the max area possible with the given height list.
        
        >>> soln = Solution()
        >>> soln.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        '''
        
        # Keep track of the largest area found so far.
        max_area = 0
        
        # Initialize two pointers: one at index 0 and the other at index len(height) - 1
        left = 0
        right = len(height) - 1
        
        # While the two pointers don't meet, if the value of the left pointer is less than
        # or equal to that at the right pointer, move the left pointer right one spot.
        # Otherwise, move the right pointer left one spot.
        while left != right:
            area = (right - left) * min(height[right], height[left])
            # Update the max area along the way!
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
