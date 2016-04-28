!/usr/bin/env python
import socket
import os

#------------------------------------------
#Packet Information - Quick Sniffing stuff
#------------------------------------------

#creating a INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#clearing the screen cause messy screen suck :)
cls = os.popen('clear')
clear = cls.read()
print(clear)

print("__________________________________________________________________________________")
print('Sniffing Packets....') 
while True:
  data = s.recvfrom(65565)
  print(data) 
  print("__________________________________________________________________________________")
  
  
  

  
  
