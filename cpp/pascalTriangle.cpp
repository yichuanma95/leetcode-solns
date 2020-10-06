/*
Problem 118: Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Solution runtime: 0ms, faster than 100% of C++ submissions
*/

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascalsTriangle;
        if (numRows == 0)
            return pascalsTriangle;
        vector<int> row1{1};
        pascalsTriangle.push_back(row1);
        if (numRows == 1)
            return pascalsTriangle;
        vector<int> row2{1, 1}, newRow{1}, prevRow;
        pascalsTriangle.push_back(row2);
        for (int r = 2; r < numRows; r++) {
            newRow.clear();
            newRow.push_back(1);
            prevRow = pascalsTriangle.back();
            for (int i = 0; i < r - 1; i++) {
                newRow.push_back(prevRow[i] + prevRow[i+1]);
            }
            newRow.push_back(1);
            pascalsTriangle.push_back(newRow);
        }
        return pascalsTriangle;
    }
};
