'''
Problem 263: Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

Notes:
    1. 1 is typically treated as an ugly number.
    2. Input is within the 32-bit signed integer range: [−2^31,  (2^31) − 1].
'''

class Solution:
    def isUgly(self, num: int) -> bool:
        old_num = 0
        while num not in [1, 2, 3, 5] and num != old_num:
            old_num = num
            num = self.div_by_ugly_prime(old_num)
        return old_num != num
    
    def div_by_ugly_prime(self, num):
        ugly_primes = [2, 3, 5]
        if num in ugly_primes:
            return 1
        for prime in ugly_primes:
            if num % prime == 0:
                return num // prime
        return num
