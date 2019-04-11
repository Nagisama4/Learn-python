# -*- coding:utf-8 -*-
"""
Group chat client
env: Python3.7
exc: for socket and fork

"""

from socket import *
import os, sys

# Server address
ADDR = ('127.0.0.1', 8080)

# Build network connection
def udp_client():
    # Build socket
    return socket(AF_INET, SOCK_DGRAM)

def login(s):
    while True:
        name = input("Please input name: ")
        msg = "L " + name  # L indicate request type
        s.sendto(msg.encode(), ADDR)
        # Wait for response
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OjbK':
            print("You've enter the group chat")
            break
        else:
            print(data.decode())
    return name

def send_msg(s, name):
    while True:
        try:
            text = input("Msg>>")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("Exit from group chat")
        msg = "\nC %s %s"%(name, text)
        s.sendto(msg.encode(), ADDR)    

def recv_msg(s):
    while True:
        data, addr = s.recvfrom(4096)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\nMsg>>',end='')  

def chat(s, name):
    # Create process
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(s, name)
    else:
        recv_msg(s)

def main():
    s = udp_client()
    name = login(s)
    chat(s, name)

main()