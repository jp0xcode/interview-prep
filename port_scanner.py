"""
Port Scanner using ThreadPoolExecutor
-------------------------------------
This script performs a basic TCP port scan on localhost (127.0.0.1), checking ports 1 through 1023.

Key features:
- Uses Python's ThreadPoolExecutor for efficient multithreaded scanning
- Identifies open ports by attempting TCP connections with a short timeout
- Demonstrates fundamental networking concepts and concurrent programming in Python

Ideal for interview prep topics like:
- Working with sockets and low-level networking
- Utilizing the concurrent.futures module
- Writing efficient I/O-bound scripts using thread pools
"""

from concurrent.futures import ThreadPoolExecutor
import socket

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex(("127.0.0.1",port))
    if result == 0:
        print(f"The port {port} is open")
    s.close()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(port_scan,range(1,1024))
