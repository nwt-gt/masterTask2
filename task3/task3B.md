#Set up rocker/rstudio using docker container

##Follow the steps below

'docker pull rocker/rstudio:3.6' getting the image from dockerhub. Here we are using version 3.6 <br />

'docker run --rm -d -p 8787:8787 --name rstudio -e USER=sammy -e PASSWORD=password rocker/rstudio:3.6' 
setting up the docker container to be in detached mode with the flag -d, in port 8787 with -p, customized name for the container --name, the username and password setup for the container -e, and remove container then stopped with --rm. <br />

'http://172.18.80.83:8787/' or 'localhost:8787' to enter application from browser. 
