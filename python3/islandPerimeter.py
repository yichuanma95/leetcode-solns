'''
Problem 463: Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and
0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the
island). One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
Image for explanation is actually on LeetCode.
'''

import collections

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cells = collections.defaultdict(int)
        total = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 4
                    cells[(i,j)] = self.findNeighbours(i, j, grid)
        
        return total - sum(cells.values())
    
    def findNeighbours(self, i, j, grid):
        neighbors = 0
        
        if i > 0: # north
            neighbors += grid[i-1][j]
        try: # east
            neighbors += grid[i][j+1]
        except IndexError:
            pass
        try: # south
            neighbors += grid[i+1][j]
        except IndexError:
            pass
        if j > 0: # west
            neighbors += grid[i][j-1]
        
        return neighbors
