# Set up rocker/rstudio using docker container

**Follow the steps below**

Getting the image from dockerhub. Here we are using version 3.6 
```
docker pull rocker/rstudio:3.6
``` 

Setting up the docker container to be in detached mode with the flag -d, expose port 8787 with -p, customized name for the container --name, the username and password setup for the container -e, and remove container then stopped with --rm. 

```
docker run --rm -d -p 8787:8787 --name rstudio -e USER=sammy -e PASSWORD=password rocker/rstudio:3.6
``` 

To enter application from browser

```
localhost:8787
```
