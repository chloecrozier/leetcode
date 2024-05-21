# https://leetcode.com/problems/game-play-analysis-i/submissions/1254466976/
SELECT
    player_id, MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id
