import socket
import threading
import time

open_ports = []
def scanner(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)

    sock.close()


def threads_scanner(host, threads_count = 10):
    threads = []
    for port in range(1, 65536):
        progress = int(port*100/65535)
        print(f"\rExecution | {progress * '█'}{(100-progress) * '░'} |  {progress}%", end="")
        while threading.active_count() > threads_count:
            pass

        t = threading.Thread(target=scanner, args=[host, port])
        threads.append(t)
        t.start()

    for t in threads:
        t.join()



hostName = input("Enter hostname or IP address for scanning:")

start = time.time()      
threads_scanner(hostName, 100)
print('\nExecution time:', round(time.time() - start, 2), 'seconds')
print('Open ports:', sorted(open_ports))