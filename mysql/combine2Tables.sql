/*
Problem 175: Combine Two Tables

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in
the Person table, regardless if there is an address for each of those people:
FirstName, LastName, City, State

Solution runtime: 192ms, faster than 99.62% of MySQL submissions

Solution memory usageL 0B, less than 100% of MySQL submissions
*/

# Write your MySQL query statement below
select 
    FirstName,
    LastName,
    City,
    State
from Person left join Address using (PersonId);
