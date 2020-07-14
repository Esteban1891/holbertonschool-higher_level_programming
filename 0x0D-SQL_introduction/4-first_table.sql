-- create table called first_table in the current database in your MySQL server.
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	NAME VARCHAR(256)
);
