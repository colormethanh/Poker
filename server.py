import socket
from _thread import start_new_thread
from player import Player
import pickle
from game import Game

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

""" ### End of server creation ### """

connected = set()

user_count = 0

game = Game()


def threaded_client(conn, user_num, game):
    global user_count

    conn.send(str.encode(f"{user_num}"))

    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break

            else:
                if data == "clicked":
                    if game.check_deck(2):
                        game.deal(user_num)
                        print(f"Player {user_num}",
                              "clicked the button and was dealt a card"
                              )
                    else:
                        print("Not enough cards to deal")
                elif data == "get":
                    pass

            conn.sendall(pickle.dumps(game))
        except:
            print("something happened")
            break
    print("lost connection")

    user_count -= 1
    if user_count == 0:
        game.reset()

    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    user_count += 1

    start_new_thread(threaded_client, (conn, user_count, game))
