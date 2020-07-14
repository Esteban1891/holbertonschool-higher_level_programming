-- lists all records of table second_table
-- sorting by score, name in descending order
SELECT score, name FROM second_table 
	WHERE name IS NOT NULL
	ORDER BY score DESC;
