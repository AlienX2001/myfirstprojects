import socket

ip_address=input("Enter IP to scan:-")
limiting_port=int(input("Enter last port"))

for port in range(75,limiting_port+1):
    dst=[ip_address,port]
    s = socket.socket()
    s.settimeout(10)
    #s.connect(dst)
    try:
        s.connect(tuple(dst))
    except socket.timeout:
        print("Port "+str(port)+" Closed")
    else:
        print("Port "+str(port)+" is open!!")
        s.close()