import socket
import threading

"""
basic port knocking technique
user needs to connect to each port in order for the real port to open up connections
"""
order = [1027,1026,1100,1025,1028,1029]
index = 0
mutex = threading.Lock()
is_open = False

# open multiple ports
# NOTE: can't open ports leq 1024 without root
threads = []


def actual_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} on port {port}")
        client_socket.sendall(f"Hello from the actual service on port {port}\n".encode())
        client_socket.close()


def start_server(port):
    global index
    global order
    global threads
    global is_open
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} on port {port}")
        with mutex:
            try:
                if(not is_open):
                    if(order[index] == port):
                        index += 1
                        if(index == len(order)):
                            # open actual service
                            thread = threading.Thread(target=actual_server, args=(8080,))
                            thread.start()
                            threads.append(thread)
                            is_open = True
                    elif(port == order[0]):
                        index = 1
                    else:
                        index = 0
                    print(f"Updated index to {index}")
            except Exception as e:
                print(f"Already open")
        try:
            client_socket.sendall(f"Hello from port {port}\n".encode())
            client_socket.close()
        except Exception as e:
            print(f"can't send message, conn reset by peer")


for port in order:
    thread = threading.Thread(target=start_server, args=(port,))
    thread.start()
    threads.append(thread)

# keep the main thread alive
for thread in threads:
    thread.join()
