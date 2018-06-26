-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT states.id FROM states WHERE states.name = 'California') ORDER BY cities.id;
