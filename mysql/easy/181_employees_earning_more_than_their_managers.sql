# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
SELECT
    E.name AS Employee
FROM
    Employee E
JOIN
    Employee M
ON
    E.managerID = M.id
WHERE
    E.salary > M.salary;
