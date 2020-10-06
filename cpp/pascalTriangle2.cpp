/*
Problem 119: Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up: Could you optimize your algorithm to use only O(k) extra space?

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
* 0 <= rowIndex <= 40

Solution runtime: 0ms, faster than 100% of C++ submissions
*/

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> newRow{1}, prevRow{1, 1};
        if (rowIndex == 0)
            return newRow;
        for (int r = 1; r < rowIndex; r++) {
            newRow.clear();
            newRow.push_back(1);
            for (int i = 0; i < r; i++) {
                newRow.push_back(prevRow[i] + prevRow[i+1]);
            }
            newRow.push_back(1);
            prevRow = newRow;
        }
        return prevRow;
    }
};
