'''
Problem 204: Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primeList: List[bool] = [False] * n
        for i in range(2, n):
            primeList[i] = True
        
        i: int = 2
        while i * i < n:
            if primeList[i]:
                for j in range(i * i, n, i):
                    primeList[j] = False
            i += 1
        
        return len(list(filter(lambda x: x, primeList)))
