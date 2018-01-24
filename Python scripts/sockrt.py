import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name="data.pr4e.org"
port=80
sock.connect((host_name,port))
rqst="GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
sock.send(rqst)
while True :
    data=sock.recv(512)
    if len(data)<1:
        break
    print(data.decode())
sock.close()