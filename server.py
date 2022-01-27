import socket
from _thread import start_new_thread
import pickle
from game import Game

# defining server ip and port
server = "192.168.11.6"
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

    game.players_mstr[user_num - 1].active = True
    game.active_plyrs.append(game.players_mstr[user_num - 1])

    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break

            else:

                if data == "Ready":
                    game.players_mstr[user_num - 1].ready = True
                    print(f"User {user_num} is ready")
                    game.action_log.insert(0, f"User {user_num} is ready")

                    if game.chk_ready():
                        if len(game.active_plyrs) >= 2:
                            game.action_log.insert(0, "All players are ready, Dealing cards...")
                            print("All players ready! Dealing Cards...")
                            game.deal_cards()

                        # assign blinds

                        # player's ante's are collected

                        # Pre-blind bet loop

                elif data == "get":
                    pass

            conn.sendall(pickle.dumps(game))
        except:
            print("something happened")
            break
    print("lost connection")

    user_count -= 1
    if user_count == 1:
        game.reset()

    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    user_count += 1

    start_new_thread(threaded_client, (conn, user_count, game))
