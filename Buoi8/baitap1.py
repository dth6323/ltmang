#khi nao client bye thi server ngat ket noi -> check data co bye thi ngat ket noi

import socket

if __name__ == '__main__':
    s= socket.socket( socket.AF_INET ,socket.SOCK_STREAM ,0)
    s.connect(('127.0.0.1',9050))
    # data = "hello server"
    while True:
        data = s.recv(4096)
        print("receive from server:")
        print(data.decode('utf-8'))
        
        if(data.decode('utf-8')== "bye"):
            break
        
        data= input("input text: ")
        s.send(data.encode('utf-8'))
    
    s.close()
    
    