# Write your MySQL query statement below
SELECT 
ip,
COUNT(*) AS invalid_count
FROM logs
WHERE
-- Not exactly 4 octets (must have exactly 3 dots)
(LENGTH(ip) - LENGTH(REPLACE(ip, '.', ''))) != 3
OR

    -- Any octet > 255
    CAST(SUBSTRING_INDEX(ip, '.', 1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(ip, '.', -1) AS UNSIGNED) > 255

    OR

    -- Any octet has leading zeros (but not "0")
    SUBSTRING_INDEX(ip, '.', 1) REGEXP '^0[0-9]+'
    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) REGEXP '^0[0-9]+'
    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) REGEXP '^0[0-9]+'
    OR SUBSTRING_INDEX(ip, '.', -1) REGEXP '^0[0-9]+'
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
