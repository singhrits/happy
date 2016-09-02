import os
import socket
s=socket.socket()
host=socket.gethostname()
port=54222
s.bind((host,port))
s.listen(10)
c,adrr=s.accept()
print"connection is created with",addr
data=c.recv(100)
print"file requested by user"
file=open(data,'r')
chunk=file.read(65536)
print chunk
s.sendall(chunk)
s.close
