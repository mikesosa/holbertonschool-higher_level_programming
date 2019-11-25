-- Write a script that lists the number of records with the same score in the table 
-- find number of occurances
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY COUNT(score) DESC;
