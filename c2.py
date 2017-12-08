#!/usr/bin/python
#Charles V. Frank Jr.
#This script creates a C&C server which
#(1) sends a command to the bot
#(2) displays the information received from the bot
#if bot does not respond in 10 seconds, the socket will timeout
#This is a real simple C&C 

import getopt
import sys
import socket

#A command lne option must be supplied
#I am only putting this in for testing purposes
#In a real scenario, I might not even check

try:
    #Get the option from the command line
    opts, args = getopt.getopt(sys.argv[1:], 'c:')
except getopt.GetoptError as err:
    print(err);
    print("c2.py -c <command>\n")
    sys.exit()

#get the bot command
bot_command = opts[0][1]

#socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket timeout incase bot does not respond
s.settimeout(2)

#port number
port = 1337

#loopback address
bot_ip = "127.0.0.1"

#connect to the bot
s.connect((bot_ip, port))

#send the bot command
s.sendall(bot_command.encode())

#print the messages sent from the bot
#catch the socket timeout
#loop until the bot is done sending the results
bot_message = "true"

while bot_message :  
    try:
        bot_message = s.recv(1024).decode()
    except socket.timeout:
        s.close
        sys.exit()

    print (bot_message)
        
#close the connection
s.close






 
