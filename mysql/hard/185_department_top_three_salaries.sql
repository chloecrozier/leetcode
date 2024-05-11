# https://leetcode.com/problems/department-top-three-salaries/description/
WITH Ranking AS (
    SELECT
        *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS `rank`
    FROM
        Employee
)
SELECT
    D.name AS Department, Ranking.name AS Employee, Ranking.salary AS Salary
FROM
    Ranking
JOIN
    Department AS D
ON
    Ranking.departmentId = D.id
WHERE
    `rank` <= 3;
