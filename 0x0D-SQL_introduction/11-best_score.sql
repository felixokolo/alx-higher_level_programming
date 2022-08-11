-- A script that lists all records with a score >= 10
-- in the table second_table of the database hbtn_0c_0
-- in your MySQL server
SELECT s.score, s.name from second_table AS s
WHERE s.score >= 10
ORDER BY s.score DESC;
