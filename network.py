import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.11.2"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.d = self.connect()
        self.data = ""
        print(self.d)

    def get_data(self):
        return self.d

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send_data(self, data):
        try:
            self.client.send(str.encode(data))
            self.data = self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


"""n = Network()
n.send_data("hello")
print(n.data)"""
