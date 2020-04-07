/*
Problem 176: Second Highest Salary

Write a SQL query to get the second highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second
highest salary. If there is no second highest salary, then the query should return null.
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Solution runtime: 127ms, faster than 90.28% of MySQL submissions

Solution memory usage: 0B, less than 100% of MySQL submissions
*/

# Write your MySQL query statement below
select
    case when count(*) = 0 then null else max(Salary) end 'SecondHighestSalary'
from Employee
where Salary <> (
    select max(Salary) from Employee
);
