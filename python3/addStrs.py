'''
Problem 415: Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1
and num2.

Notes:
1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        sum_str = ""
        shorter_len = min(len(num1), len(num2))
        for i in range(shorter_len):
            reverse_ind = -(i + 1)
            digit_sum = int(num1[reverse_ind]) + int(num2[reverse_ind]) + carry
            carry = digit_sum // 10
            sum_str += str(digit_sum % 10)
        if len(num1) > len(num2):
            return self.finish_addition(num1[:len(num1)-shorter_len], carry) + sum_str[::-1]
        return self.finish_addition(num2[:len(num2)-shorter_len], carry) + sum_str[::-1]
    
    def finish_addition(self, num, carry):
        if len(num) == 0 and carry > 0:
            return str(carry)
        if carry > 0:
            return self.addStrings(num, str(carry))
        return num
