'''
Problem 1013: Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into
three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with
(A[0] + A[1] + ... + A[i] ==
A[i+1] + A[i+2] + ... + A[j-1] ==
A[j] + A[j-1] + ... + A[A.length - 1]) 

Example 1:
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Notes:
1. 3 <= A.length <= 50000
2. -10000 <= A[i] <= 10000
'''

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total: int = sum(A)

        if total % 3 != 0:
            return False
        
        partSum: int = total // 3
        firstInd: int = -1
        firstSum: int = 0
        secondInd: int = -1
        secondSum: int = 0
        
        for i in range(len(A)):
            firstSum += A[i]
            if firstSum == partSum:
                firstInd = i + 1
                break
        if firstInd < 0:
            return False
        
        for i in range(firstInd, len(A)):
            secondSum += A[i]
            if secondSum == partSum:
                secondInd = i + 1
                break
        
        if secondInd < 0:
            return False
        
        return True
