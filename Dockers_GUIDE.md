## DockerFile Commands



FROM language:version

WORKDIR /app (Virtual Folder in Docker Environment)

COPY requirements.txt .(Copying files from your local system to docker environment)

RUN pip install -r requirements.txt (Runs while the image building)

COPY train.py .

COPY app.py .

EXPOSE 5000 (port number used in the docker container)

CMD \["python","app.py"] (Provide the same commands used to intiate the flask code/ Runs while the container starts)



## 

## Docker CMD Commands



docker build -t image\_name .(Creates a docker image)

docker image (Shows the images in your docker)



docker run -d -p 5000:5000 name container\_name image\_name (Running the docker environment while creating a docker container)

docker ps (Shows the containers in your docker environment)





docker build -t image\_name .	                                Builds a Docker image using the Dockerfile in the current directory.

docker images	                                                Displays the Docker images available on your system.

docker run -d -p 5000:5000 --name container\_name image\_name	Creates and starts a container using the specified image.

docker ps	                                                Displays currently running containers.

docker ps -a	                                                Displays all containers, including stopped containers.

docker stop container\_name	                                Stops a running container.

docker start container\_name	                                Starts an existing stopped container.

docker logs container\_name	                                Displays the container's application logs.

docker rm container\_name	                                Removes a stopped container.

docker rmi image\_name	                                        Removes a Docker image, provided no container is using it.

