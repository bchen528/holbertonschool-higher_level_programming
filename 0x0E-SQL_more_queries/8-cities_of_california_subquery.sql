
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM hbtn_0d_usa.cities WHERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY cities.id ASC;
