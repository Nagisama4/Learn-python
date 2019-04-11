# -*- coding:utf-8 -*-
"""
Group chat server
env: Python3.7
exc: for socket and fork
All man must die
"""

from socket import *
import os, sys
from time import ctime

# Server address
ADDR = ('0.0.0.0', 8080)
# Save Users
user = {}

# Build network connection
def udp_server():
    # build socket
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    return s

def do_login(s, name, addr):
    if (name in user) or ("Admin" in user):
        s.sendto("User name exist".encode(), addr)
        return
    s.sendto(b'OjbK', addr)

    # Broadcast to other
    msg = "\nWelcome %s enter group chat"%name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # Add in user dictionary
    user[name] = addr

def do_chat(s, name, text):
    msg = "%s : %s"%(name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])

def do_quit(s, name):
    msg = "\n%s left the group chat"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    # delete user from dictionary
    del user[name]
    

def request(s):
    while True:
        data, addr = s.recvfrom(1024)
        msgList = data.decode().split(' ')
        # identify request type
        if   msgList[0] == 'L':
            do_login(s, msgList[1], addr)
        elif msgList[0] == 'C':
            # remake the msg
            text = ' '.join(msgList[2:])
            do_chat(s, msgList[1], text)
        elif msgList[0] == 'Q':
            do_quit(s, msgList[1])

def main():
    s = udp_server()
    pid = os.fork()
    if pid < 0:
        print("Error")
    elif pid == 0:
        while True:
            msg = input('Admin: ')
            msg = "C Admin info " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        request(s)

main()