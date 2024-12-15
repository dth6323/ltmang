import socket
import threading

import datetime


def handle_client(socket):
    command = socket.recv(1024).decode()
    if command == "Get_time":
        client.sendall(str(datetime.datetime.now()).encode('utf-8'))
    elif command == "Max":
        a, b = client.recv(1024).decode('utf-8').split('_')
        client.sendall(str(max(int(a), int(b))).encode('utf-8'))
    elif command == "Min":
        a, b = client.recv(1024).decode('utf-8').split('_')
        client.sendall(str(min(int(a), int(b))).encode('utf-8'))
    else:
        client.sendall(str(len(command)).encode('utf-8'))
    client.close()
if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    while True:
        client, address = server.accept()
        print('Connected by', address)
        threading.Thread(target=handle_client, args=(client,)).start()
    server.close()