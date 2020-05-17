# task 5

Already cloned the DB scripts from this [link](https://github.com/jOOQ/jOOQ/blob/master/jOOQ-examples/Sakila/postgres-sakila-db)
into folder dbScripts

**Run syntax**

```
docker volume create post5-volume
docker run --rm -d --name post5 --mount source=post5-volume,target=/data -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=weetong postgres
psql -U weetong
```

Details for postgres
```
POSTGRES_PASSWORD=postgres
POSTGRES_DB=testdb
POSTGRES_USER=weetong
```
