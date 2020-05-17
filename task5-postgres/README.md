# task 5

Clone the DB scripts from this [link](https://github.com/jOOQ/jOOQ/blob/master/jOOQ-examples/Sakila/postgres-sakila-db)

**Run syntax**

```
docker volume create post5
docker run --rm -d --name post5 --mount source=post5,target=/data postgres
docker run --rm -d --name post5 --mount source=post5,target=/data -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=weetong postgres
psql -U weetong
```

Details for postgres
```
POSTGRES_PASSWORD=postgres
POSTGRES_DB=testdb
POSTGRES_USER=weetong
```
