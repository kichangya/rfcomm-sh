from bluetooth import *
from telnetlib import Telnet

server_address = "cc:3d:82:e8:b3:da"

port = 1

s = BluetoothSocket(RFCOMM)
s.connect((server_address, port))

t = Telnet()
t.sock = s

t.interact()
