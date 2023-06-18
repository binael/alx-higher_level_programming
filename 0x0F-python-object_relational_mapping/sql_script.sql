-- Create states table in hbtn_0e_4_usa with some data
SELECT c.id, s.name, c.name
FROM cities AS c
INNER JOIN states AS s 
ON c.state_id = s.id 
ORDER BY c.id
