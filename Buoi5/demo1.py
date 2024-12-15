import socket

def get_host_name_ip():
    try:
        host_name = 'www.utc.edu.vn'
        host_ip = socket.gethostbyname(host_name)
        print(host_name)
        print(host_ip)
    except:
        raise Exception("Fail")