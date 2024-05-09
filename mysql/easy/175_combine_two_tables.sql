# https://leetcode.com/problems/combine-two-tables/description/
SELECT
	P.firstName, P.lastName, A.city, A.states
FROM
	Person AS P
LEFT JOIN
	ADDRESS AS A
ON
	P.personId = A.personId;
