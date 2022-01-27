import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server = "192.168.11.6"
        self.port = 5555
        self.addr = (self.server, self.port)

        self.p = self.connect()  # self.p is player object for now
        self.recv_data = ""

    def get_player(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048*4).decode()
        except socket.error as e:
            print(e)

    def send_data(self, data):
        try:
            # sends data to server
            self.client.send(str.encode(data))

            # the recieved data is sent back to the client in "self.recv_data"
            return pickle.loads(self.client.recv(4096*4))

        except socket.error as e:
            print(e)
