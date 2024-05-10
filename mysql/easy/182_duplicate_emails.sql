# https://leetcode.com/problems/duplicate-emails/description/
SELECT
    DISTINCT email as Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(email) > 1;
