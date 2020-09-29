from datetime import datetime
import logging
from socket import socket, AF_INET, SOCK_DGRAM

#Setting app log
logging.basicConfig(filename='./Log/Meridian.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

# IP address configuration
print("Enter the IP address")
IPHost = input()

# Port configuration
print("Enter the Port")
Port = input()
print(" - Url set: ", IPHost + ":" + Port)

#socket settings
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((IPHost, int(Port)))

#  Listen to messages posted by meridian
while True:
    
    #Infoamcaion message received
    msg, addr = sock.recvfrom(800192)  
    
    # Decode Message Bytes
    MsgDecode = msg.decode('utf-8')
    
    # Current date
    now = datetime.now()
    
    # Print to console
    print("  - Got message from %s - %s - Message Received: %s" % (addr, now, MsgDecode))
    # Print to Log
    logging.info('- Got message from %s - %s - Message Received: %s' % (addr, now, MsgDecode))