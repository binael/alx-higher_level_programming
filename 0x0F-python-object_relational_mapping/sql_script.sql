-- Create states table in hbtn_0e_4_usa with some data
SELECT c.name 
FROM cities AS c 
LEFT JOIN states AS s
ON c.state_id = s.id
WHERE BINARY s.name = 'Nevada'
ORDER BY c.id ASC
