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
        ''' (Solution, int) -> int
        
        Counts and returns the number of primes less than n.
        
        >>> soln = Solution()
        >>> soln.countPrimes(10)
        4
        '''
        
        isPrime = [False] * n
        for i in range(2, n):
            isPrime[i] = True
        
        # Loop's ending condition is i * i < n instead of i < sqrt(n) to avoid
        # repeatedly calling sqrt().
        i = 2
        while i * i < n:
            if not isPrime[i]:
                i += 1
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False
            i += 1
            
        return len(list(filter(lambda x: x, isPrime)))
    