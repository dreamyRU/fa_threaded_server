import socket
from random import randint

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket()

        client_port = randint(2000, 8000)
        while True:
            try:
                self.sock.bind(("localhost", client_port))
                break
            except OSError:
                client_port = randint(2000, 8000)

        self.sock.connect((host, port))

    def connect(self):
        while True:
            self.sock.send("Hello".encode())

            data = self.sock.recv(1024)
            print(data.decode())
            break

if __name__ == "__main__":
    clients = []
    for i in range(100):
        clients.append(Client("localhost", 9090))
    
    for client in clients:
        client.connect()
        client.sock.close()