import socket
from _thread import start_new_thread
import pickle
from game import Game

# defining server ip and port
server = "192.168.11.14"
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

user_count = 0

game = Game()


def threaded_client(conn, player_obj, game):
    global user_count

    conn.send(str.encode(f"{player_obj.ID}"))

    player_obj.active = True
    game.active_plyrs.append(player_obj)

    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break

            else:

                if data == "Ready":
                    player_obj.ready = True
                    print(f"User {player_obj.ID} is ready")
                    game.action_log.insert(0, f"User {player_obj.ID} is ready")

                if data == "get":
                    conn.sendall(pickle.dumps(game))

                game_phase = game.chk_phase()

                if game_phase == "pre-pocket":  # if in pre-pocket phase
                    if not game.active:
                        print("game is now active")
                        game.action_log.insert(0, "All players are ready, starting game...")
                        game.active = True

                    if not game.blind_assnd:
                        print("assigning blinds")
                        game.assign_blinds(game_start=True)

                    game.players_mstr[0].turn = True

                    game.pre_pocket_bet(player_obj)

                elif game_phase == "pre-flop":
                    print("game phase is ", game_phase)
                    if not game.pocket_dealt:
                        print("dealing cards")
                        game.deal_cards()

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
    player_obj = game.players_mstr[user_count - 1]
    start_new_thread(threaded_client, (conn, player_obj, game))
