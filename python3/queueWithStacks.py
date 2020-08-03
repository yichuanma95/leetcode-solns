'''
Problem 232: Implementing Queue using Stacks

Implement the following operations of a queue using stacks.
-push(x) -- Push element x to the back of queue.
-pop() -- Removes the element from in front of queue.
-peek() -- Get the front element.
-empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
-You must use only standard operations of a stack -- which means only push to top, peek/pop
from top, size, and is empty operations are valid.
-Depending on your language, stack may not be supported natively. You may simulate a stack by
using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
-You may assume that all operations are valid (for example, no pop or peek operations will
be called on an empty queue).

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack1 = []
        self._stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self._stack2) == 0:
            self._move_all_to_stack2()
        return self._stack2.pop()
        
    def _move_all_to_stack2(self):
        stack1_len = len(self._stack1)
        for i in range(stack1_len):
            self._stack2.append(self._stack1.pop())

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self._stack1) == 0:
            return self._stack2[-1]
        return self._stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._stack1) == 0 and len(self._stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
