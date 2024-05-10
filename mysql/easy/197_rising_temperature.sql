# https://leetcode.com/problems/rising-temperature/submissions/1254440200/
SELECT
    Curr.id
FROM
    Weather AS Curr, Weather AS PREV
WHERE
    Curr.temperature > Prev.temperature
    AND Prev.recordDate = DATE_SUB(Curr.recordDate, INTERVAL 1 DAY)
