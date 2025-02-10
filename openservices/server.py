import socket
import threading

"""
script to open up multiple ports on local machine
utilizes multithreading in order to do so
"""

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} on port {port}")
        client_socket.sendall(f"Hello from port {port}\n".encode())
        client_socket.close()

# open multiple ports
# NOTE: can't open ports leq 1024 without root
ports = [1025,1026,1027,1100,1200]
threads = []

for port in ports:
    thread = threading.Thread(target=start_server, args=(port,))
    thread.start()
    threads.append(thread)

# keep the main thread alive
for thread in threads:
    thread.join()
