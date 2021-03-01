-- Script that lists records of second_table as long as rows have a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
