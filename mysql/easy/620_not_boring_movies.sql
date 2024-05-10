# https://leetcode.com/problems/not-boring-movies/description/
SELECT
    *
FROM
    Cinema
WHERE
    description != "boring" AND MOD(id, 2) = 1
ORDER BY
    id DESC;
