import socket
from _thread import *
from player import Player
import pickle


def threaded_client(conn, players, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


def main():
    
    
    server = ""
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        print(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    players = [Player((0,0,80,90)), Player((250,250, 80, 90))]
    currentPlayer = 0
    
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, players, currentPlayer))
        currentPlayer += 1
        
if __name__ == "__main__":
    main()