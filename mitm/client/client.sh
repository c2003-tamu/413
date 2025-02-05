docker build -t mitm-client .
docker run --rm -it --name client --network mitm-net mitm-client
docker image rm mitm-client
