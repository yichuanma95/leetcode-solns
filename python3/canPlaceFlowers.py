'''
Problem 605: Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both
would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means
not empty), and a number n, return if n new flowers can be planted in it without violating
the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Notes:
1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. n is a non-negative integer which won't exceed the input array size.

Solution runtime: 156ms, faster than 98.89% of Python3 submissions
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        last_flower = -2
        for i, spot in enumerate(flowerbed):
            if spot == 1:
                planted += self.plant_flowers(i - last_flower - 1)
                last_flower = i
        planted = min(planted + self.plant_flowers(len(flowerbed) - last_flower), n)
        print(planted)
        return planted == n
    
    def plant_flowers(self, spaces):
        return max(0, (spaces - 1) // 2)
