docker build -t mitm-server .
docker run --rm -it --name server --network mitm-net mitm-server
docker image rm mitm-server
