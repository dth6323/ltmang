import socket
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    data = input("what you want to send? ")
    client.sendall(data.encode('utf-8'))
    if data == "Max" or data == "Min":
        number = input("what number to send? ")
        client.sendall(number.encode('utf-8'))
    res = client.recv(1024).decode('utf-8')
    print(res)