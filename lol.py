import socket




n = input("would u like UDP or TCP?")

if n == "tcp":
    target_host = input("what is the TCP ip?")
    target_port = 80
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # connect the clientv 
    client.connect((target_host,target_port))# send some dataw 
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.recv(4096) 


if n == "udp":
    target_host = input("UDP ip?")
    target_port = input("port?")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    client.sendto("AAABBBCCC",(target_host,target_port))# receive some dataw 
    data, addr = client.recvfrom(4096) 
print(data)
