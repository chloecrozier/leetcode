# https://leetcode.com/problems/delete-duplicate-emails/description/
DELETE 
    Dupe
FROM
    Person AS Dupe
JOIN
    Person AS First
ON
    First.email = Dupe.email
WHERE
    First.id < Dupe.id;
