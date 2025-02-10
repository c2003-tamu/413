import socket
import concurrent.futures

"""
tool to mock nmap, scans for open ports on a given ip
to check which ports are open:
    1. enumerate ports
    2. iterate over enumerated ports, try to connect with TCP
    3. if able to connect, port is open, report as such
implemented with multithreading for performance
"""

"""
ip - ip to check
port - port to check
timeout - how long to try to connect via TCP before giving up
"""
def scan_port(ip, port, timeout=1):
    # attempts to connect to the given IP and port to check if it's open.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        if s.connect_ex((ip, port)) == 0:
            return port
    return None

"""
ip - ip to check
ports - list of ports to check
max_threads - maximum number of threads for execution
"""
def scan_ports(ip, ports, max_threads=50):
    # scans a list of ports on the given IP using multithreading.
    def port_worker(p):
        return scan_port(ip, p)

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        results = executor.map(port_worker , ports)
    
    return list(filter(None, results))

if __name__ == "__main__":
    target_ip = input("enter target IP or hostname: ")
    target_ports = range(1,1201) 
    
    print(f"scanning {target_ip} for open ports...\n")
    
    open_ports = scan_ports(target_ip, target_ports)
    
    if open_ports:
        print(f"open ports: {', '.join(map(str, open_ports))}")
    else:
        print("no open ports found.")

