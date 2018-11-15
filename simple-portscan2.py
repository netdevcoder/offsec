#!/usr/bin/python3
import socket
import ipaddress
import sys
import threading
import time

def portscan(min,max,ip):
  for port in range (min,max):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    if s.connect_ex((ip, port)):
       continue
    else:
       print ( ip, " Port", port, "is Open")
    s.shutdown(2)
    s.close()
#if sys.argv[1] == "":
#   print ("usage ./simple-portscan.py <subnet>")
IP = sys.argv[1]


list_ip=[]
for ips in ipaddress.IPv4Network(IP):
    list_ip.append(ips)

count = len(list_ip)
count_1 = int(count//4)
count_2 = int(count//2)
count_3 = count_1 + count_2
def range_ip(min, max):
    for id in range (min,max):
       ip = str(list_ip[id])
       t1 = threading.Thread(target=portscan, args=(1, 2500,ip ) )
       t2 = threading.Thread(target=portscan, args=(2501, 5000,ip ) )
       t3 = threading.Thread(target=portscan, args=(5001, 7500,ip ) )
       t4 = threading.Thread(target=portscan, args=(7501, 10000,ip ) )

       t1.start()
       t2.start()
       t3.start()
       t4.start()

       t1.join()
       t2.join()
       t3.join()
       t4.join()

       time.sleep(0.25)

ip1 = threading.Thread(target=range_ip, args=(0, count_1 ) )
ip2 = threading.Thread(target=range_ip, args=(count_1+1, count_2-1 ) )
ip3 = threading.Thread(target=range_ip, args=(count_2, count_3-1 ) )
ip4 = threading.Thread(target=range_ip, args=(count_3, count ) )

ip1.start()
ip2.start()
ip3.start()
ip4.start()
