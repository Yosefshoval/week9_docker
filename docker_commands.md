# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash
docker cp shopping_list.tar fastapi-db:/app/db   #I'm not sure is the correct syntax 
```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -it -v fastapi-db:/app/db shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1
```

### Run the container

```bash
docker run -it --mount type=bind,source=./server2/data,target=/app/data shopping-server2:v1
```

