import ipaddress as ip

#lay ra tat ca cac thong tin dia chi dau cuoi mang bat ki
CLASS_C ='192.168.0.0'
prefix = 25 #24-30
if __name__ == '__main__':
    # not_config = True
    # while not_config
    
    
    net_addr = CLASS_C+'/'+ str(prefix)
    print('network address:%s'%net_addr)    

    try:
        network = ip.ip_network(net_addr)
    except:
        raise Exception("Fail to create network")
    # print("network configuration")
    # print("\t network address: %s"%network.network_address)
    # print("number of IP address: %s"%network.num_addresses)
    # print("broastcast:%s"%network.broadcast_address)
    # fist_ip,last_ip = list(network.hosts())[0], list(network.hosts())[-1]
    # print("\t host IP from %s to %s"%(fist_ip, last_ip))
    
    print("network configuration")
    print(f"\tnetwork address: {network.network_address}")
    print(f"\tnumber of IP address: {network.num_addresses}")
    print(f"\tsubnet mask: {network.netmask}")
    print(f"\tbroadcast: {network.broadcast_address}")
    list_ip = list(network.hosts())
    print(f"\tfirst IP: {list_ip[0]}")
    print(f"\tlast IP: {list_ip[-1]}")

    for subnet in network.subnets(new_prefix=23):
        print(f"Subnet: {subnet}")
        print(f"first IP: {subnet[0]}")
        print(f"last IP: {subnet[-1]}")
    