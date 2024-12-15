import socket
host = "127.0.0.1"

#lay ip
ip_addr = socket.gethostbyname(host)

#kiem tra xem 1 port co mo khong
while 1: 
    port_n = int(input("enter port:"))
    try:
        s = socket.socket()
        r = s.connect((ip_addr, port_n))
        print("Port {}: open".format(port_n))
    except :
        print("Port {}: close".format(port_n))
    
#lam vong for get cac cong pho bien
        