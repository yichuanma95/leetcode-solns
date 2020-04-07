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
        digits1: List[int] = list(map(lambda x: int(x), num1))
        digits2: List[int] = list(map(lambda x: int(x), num2))
        resultNum: List[int] = []
        if len(digits1) > len(digits2):
            bigger = digits1
        else:
            bigger = digits2
        minDigits: int = min(len(num1), len(num2))
        diff: int = max(len(num1), len(num2)) - minDigits
        carry: int = 0

        for i in range(minDigits):
            tempSum: int = digits1[-(i+1)] + digits2[-(i+1)] + carry
            carry = tempSum // 10
            resultNum.insert(0, tempSum % 10)
        for i in range(diff):
            tempSum = bigger[-(i+minDigits+1)] + carry
            carry = tempSum // 10
            resultNum.insert(0, tempSum % 10)
        if carry != 0:
            resultNum.insert(0, carry)
        
        return ''.join(list(map(lambda x: str(x), resultNum)))
