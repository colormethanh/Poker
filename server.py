import socket
from _thread import start_new_thread

# defining server ip and port
server = "192.168.11.2"
port = 5555

# creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)
    print(e)

# server is running and waitin for a connection
s.listen()
print("Server started, waiting for a connection...")

connected = set()
idCount = 0


def threaded_client(conn, id):

    global idCount
    conn.send(str.encode("Connected"))
    reply = ""

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode()

            if not data:
                print("Disconnected")
                break
            else:
                print("recieving")
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            print("something happened")
            break
    print("lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1

    start_new_thread(threaded_client, (conn, idCount))
