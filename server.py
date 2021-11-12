import socket
import threading


sock = socket.socket()
sock.bind(("localhost", 9090))
sock.listen(1)


def connection(conn, addr):
    print("Connnect client from:", addr)
    while True:
        data = conn.recv(1024).decode()
        print("Receive data from", addr, ":", data)
        if not data:
            conn.close()
            break

        conn.send(data.upper().encode())


while True:
    conn, addr = sock.accept()
    c = threading.Thread(target=connection, args=[conn, addr])
    c.start()