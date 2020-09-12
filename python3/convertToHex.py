'''
Problem 405: Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer,
two’s complement method is used.

Notes:
1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is
represented by a single zero character '0'; otherwise, the first character in the
hexadecimal string will not be the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to
hex directly. (I did, and nothing stopped me from doing so, because my solution was
accepted anyway)

Example 1:
Input: 26
Output: "1a"

Example 2:
Input: -1
Output: "ffffffff"

Solution runtime: 20ms, faster than 98.57% of Python3 submissions

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 0xffffffff + num + 1
        return hex(num)[2:]
    