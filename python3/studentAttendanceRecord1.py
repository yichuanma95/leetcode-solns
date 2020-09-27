'''
Problem 551: Student Attendance Record I

You are given a string representing an attendance record for a student. The record only
contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        current_late_streak = 0
        longest_late_streak = 0
        absences = 0
        for c in s:
            absences += (1 if c == 'A' else 0)
            if c == 'L':
                current_late_streak += 1
            else:
                longest_late_streak = max(current_late_streak, longest_late_streak)
                current_late_streak = 0
        longest_late_streak = max(current_late_streak, longest_late_streak)
        return absences <= 1 and longest_late_streak <= 2
    