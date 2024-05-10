# https://leetcode.com/problems/biggest-single-number/description/
SELECT
    MAX(num) AS num
FROM (
    SELECT
        Derived.num
    FROM
        MyNumbers as Derived
    GROUP BY
        Derived.num
    HAVING
        COUNT(num) = 1
    )
    AS Derived;
