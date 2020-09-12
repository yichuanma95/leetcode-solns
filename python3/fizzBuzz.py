'''
Problem 412: Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples
of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
For n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz = []
        for i in range(1, n + 1):
            self.fill_fizz_buzz(i, fizz_buzz)
        return fizz_buzz
    
    def fill_fizz_buzz(self, i, fizz_buzz):
        if i % 15 == 0:
            fizz_buzz.append("FizzBuzz")
        elif i % 3 == 0:
            fizz_buzz.append("Fizz")
        elif i % 5 == 0:
            fizz_buzz.append("Buzz")
        else:
            fizz_buzz.append(str(i))
