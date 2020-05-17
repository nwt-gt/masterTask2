# Task 5

## Task5A
Already cloned the DB scripts from this [link](https://github.com/jOOQ/jOOQ/blob/master/jOOQ-examples/Sakila/postgres-sakila-db)
into folder dbScripts

**Run syntax**

To run docker container
 * --rm - auto remove container when stopped
 * -d - detached
 * --name - naming container
 * -p - expose port 5450
 * --mount - bind mount volumne to /data of the container
 * -e - set password, user name and database
```
docker run --rm -d --name task5-postgres -p 5450:5432 --mount type=bind,source=/home/nwt/swgapp/docker/masterTask2/task5-postgres/dbscripts/,target=/data -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=testdb postgres:9.6
```

To execute docker container
```
docker exec -it task5-postgres bash
```

To create schema and insert data
```
psql -U postgres -d postgres -f /data/postgres-sakila-schema.sql
psql -U postgres -d postgres -f /data/postgres-sakila-insert-data.sql
```

Check if schema has be created
```
\dt
```

With output
```
 Schema |       Name       | Type  |  Owner
--------+------------------+-------+----------
 public | actor            | table | postgres
 public | address          | table | postgres
 public | category         | table | postgres
 public | city             | table | postgres
 public | country          | table | postgres
 public | customer         | table | postgres
 public | film             | table | postgres
 public | film_actor       | table | postgres
 public | film_category    | table | postgres
 public | inventory        | table | postgres
 public | language         | table | postgres
 public | payment          | table | postgres
 public | payment_p2007_01 | table | postgres
 public | payment_p2007_02 | table | postgres
 public | payment_p2007_03 | table | postgres
 public | payment_p2007_04 | table | postgres
 public | payment_p2007_05 | table | postgres
 public | payment_p2007_06 | table | postgres
 public | rental           | table | postgres
 public | staff            | table | postgres
 public | store            | table | postgres
(21 rows)
```

Check data 
```
select * from actor limit 5;
```
with output
```
 actor_id | first_name |  last_name   |     last_update
----------+------------+--------------+---------------------
        1 | PENELOPE   | GUINESS      | 2006-02-15 04:34:33
        2 | NICK       | WAHLBERG     | 2006-02-15 04:34:33
        3 | ED         | CHASE        | 2006-02-15 04:34:33
        4 | JENNIFER   | DAVIS        | 2006-02-15 04:34:33
        5 | JOHNNY     | LOLLOBRIGIDA | 2006-02-15 04:34:33

```

Details for postgres
```
POSTGRES_PASSWORD=postgres
POSTGRES_DB=testdb
POSTGRES_USER=postgres
```
## Task5B

Install python requirements
```
sudo apt-get install python-psycopg2
```

Run following syntax on command line to see output. [More information](https://pynative.com/python-postgresql-select-data-from-table/)

```
python connectDB.py
```

