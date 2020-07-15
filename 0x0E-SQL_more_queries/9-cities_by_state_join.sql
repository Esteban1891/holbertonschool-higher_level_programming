-- using JOIN to query a database
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON states.id=cities.state_id
ORDER BY cities.id ASC;
