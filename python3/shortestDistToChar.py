'''
Problem 821: Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest
distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 
Notes:
1. S string length is in [1, 10000].
2. C is a single character, and guaranteed to be in string S.
3. All letters in S and C are lowercase.
'''

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        dists: List[int] = [0 if s == C else len(S) + 1 for s in list(S)]
        dist: int = 1
        
        for i in range(len(dists)):
            if dists[i] == 0:
                for j in range(1, i + 1):
                    if dists[i - j] == 0:
                        break
                    dists[i - j] = min(j, dists[i - j])
                try:
                    while dists[i + dist] != 0:
                        dists[i + dist] = min(dist, dists[i + dist])
                        dist += 1
                    dist = 1
                except IndexError:
                    break
    
        return dists
