-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM hbtn_0d_usa.cities WHERE cities.state_id = (SELECT states.id FROM hbtn_0d_usa.states WHERE states.name = 'California') ORDER BY cities.id ASC;
