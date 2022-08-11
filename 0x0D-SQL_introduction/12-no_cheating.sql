-- A script that updates the score of Bob to
-- 10 in the table second_table..
UPDATE second_table AS s
SET s.score = 10
WHERE s.name = 'Bob';