docker run -it --rm --name mitm --network mitm-net mitmproxy/mitmproxy \
    mitmproxy --mode reverse:http://server:5000 --listen-host 0.0.0.0 --listen-port 8080
docker image rm mitmproxy/mitmproxy
