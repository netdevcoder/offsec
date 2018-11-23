import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

if s.connect_ex("web server", 80):
   print("failed to connect")
else:   
   s.sendall("GET / HTTP/1.1\r\n")
   s.sendall("host: web server\r\n")
   print s.recv(4096)
   s.close()
   



