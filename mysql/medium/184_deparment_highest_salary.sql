# https://leetcode.com/problems/department-highest-salary/description/
SELECT
    D.name AS Department, E.name AS Employee, E.salary AS Salary 
FROM
    Employee AS E
JOIN
    Department AS D
ON
    E.departmentId = D.id
WHERE
    E.salary = (
        SELECT MAX(E.salary)
        FROM Employee AS E
        WHERE E.departmentId = D.Id 
    );
