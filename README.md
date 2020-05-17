# Masterclass

**Task 1**

Write shell command to find linux process for root user

**Task 2**

Set up github account and create a markdown file as seen on this page
    
**Task 3**
 * 3A 
    1. Explained the differences between a container and an image
    2. Give some advantages of using containers.
    3. How can security of containers be compromised?
    4. How is Docker different from Vagrant?
 * 3B 
    1. Install docker
    2. Pull rocker/rstudio image from [docker hub](https://hub.docker.com/r/rocker/rstudio/)
    3. Run the container and access the application from a browser
 * 3C
    1. Set up a docker-compose file for the image in task 3B
    2. Run docker container using docker-compose
    
**Task 4**
 * 4A - Using python, read the csv and extract only fields 3 and 1 in that order and output as JSON and XML. 
 **(No link was given in the masterclass slides)**
 * 4B - Using the same csv file, write a bash script to replace the ID with "xxxxx" using regular expression. Assuming IDs with 6-7 digits with an optional letter
 
**Task 5**
 * 5A 
     1. Pull the [postgres image](https://hub.docker.com/_/postgres) from docker hub,
     2. Clone the DB scripts from [github](https://github.com/jOOQ/jOOQ/tree/master/jOOQ-examples/Sakila/postgres-sakila-db)
     3. Run the SQL scripts to create a database schema and insert rows
 * 5B - From 5A
     1. Combine the tables actor, film_actor, and film
     2. Query the first 10 rows of ACtor_ID, First_NAME, LAST_NAME, TITLE, DESCRIPTION and RELEASE_YEAR
     3. May use psycopg
     
 **Task 6**
  * 6A
     1. write a function to reverse the sequence of input data
     2. Package the function into a Flask App that accepts user-input characters.
     3. Test the Flask app.
     4. Open the browser to load the app and test the application.
  * 6B
     1. Set up a docker container for Postgres **may use the same container from Task6**
     2. Set up a docker container for PostgresAPI **REST API Layer for Postgres**
     3. Show how the API can be queried to list the first 10 rows of a table **May use Postman**
