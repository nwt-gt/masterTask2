import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5450",
                                  database="postgres")
   cursor = connection.cursor()
   postgreSQL_select_Query = """SELECT actor.actor_id, actor.first_name, actor.last_name, 
                film.title, film.description, film.release_year
                From 
                film INNER JOIN film_actor ON film_actor.film_id = film.film_id
                INNER JOIN actor ON film_actor.actor_id = actor.actor_id
                limit 10
"""

   cursor.execute(postgreSQL_select_Query)
   print("Selecting 10 rows using cursor.fetchmany")
   #records = cursor.fetchall() 
   records = cursor.fetchmany(10) 
   
   print("Print each row and it's columns values")
   for row in records:
       print("ACTOR_ID:   ", row[0])
       print("FIRST_NAME:   ", row[1])
       print("LAST_NAME:    ", row[2])
       print("TITLE:   ", row[3])
       print("DESCRIPTION:   ", row[4])
       print("RELEASE_YEAR:   ", row[5], "\n")
       print("")
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
