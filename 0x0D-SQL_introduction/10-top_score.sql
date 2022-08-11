-- A script that lists all records of the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
SELECT s.score, s.name  FROM second_table as s
ORDER BY s.score DESC;
