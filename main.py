import socket
import threading
import time
import argparse

start = time.time()

# Checks if a single port is open on the given host
def check_port(host,port):
    s = socket.socket() 
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

# Scans ports 1-1024 using threads and returns open ports
def scan(host):
    open_ports = []
    lock = threading.Lock()
    threads = []
    
    # Helper function: checks if port is open and safely adds it to list using a lock to prevent "race conditions".
    def check_and_add(port):
        if check_port(host,port):
            with lock:
                open_ports.append(port)
    

    for port in range(1,1025):
      t = threading.Thread(target=check_and_add, args=(port,))
      threads.append(t)
      t.start()

    for t in threads:
        t.join()

    print(f"A total of {len(open_ports)} open ports were found!")
    return open_ports
        
    
parser = argparse.ArgumentParser(description="Scan for open ports on the target")
parser.add_argument("-t",'--target',type=str, required=True, help="The name of the target")
args = parser.parse_args()

host_name = args.target
if("://" in host_name):
    host_name = host_name.split("://")[1]

result = scan(host_name)
for port in result:
    try:
        service = socket.getservbyport(port)
    except:
        service = "Unknown"
    print(f"Port {port} (Service: {service}): Open")
print(f"Scan completed in {time.time() - start:.2f} seconds")