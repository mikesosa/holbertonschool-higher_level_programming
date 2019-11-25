-- Write a script that lists all records of the table second_table
-- Select column where not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
