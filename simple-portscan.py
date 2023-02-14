#!/usr/bin/python3
import socket
import ipaddress
import sys
import threading
import time

def portscan(min,max):
  for port in range (min,max):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    if s.connect_ex((ip, port)):
       continue
    else:
       print ( ip, " Port", port, "is Open")
    s.shutdown(2)
    s.close()


IP = sys.argv[1]

for ip in ipaddress.IPv4Network(IP):
  ip = str(ip)
  #portscan()
  t1 = threading.Thread(target=portscan, args=(1, 2500 ) )
  t2 = threading.Thread(target=portscan, args=(2501, 5000 ) )
  t3 = threading.Thread(target=portscan, args=(5001, 7500 ) )
  t4 = threading.Thread(target=portscan, args=(7501, 10000 ) )

  t1.start()
  t2.start()
  t3.start()
  t4.start()

  t1.join()
  t2.join()
  t3.join()
  t4.join()

  time.sleep(0.25)
print ("BYE")
#end of program
