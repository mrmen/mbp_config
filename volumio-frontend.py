#!/usr/bin/env python3
from mpd import	MPDClient
import sys

# connect to server
client = MPDClient()
server="192.168.1.221"
client.connect(server,6600)

# parse arguments

if len(sys.argv)>2 or len(sys.argv)==1:
    sys.exit(0)
elif len(sys.argv)==2:
    command = sys.argv[1]
    
    
# switch between case
if command=="play":
    client.play()
if command=="pause":
    client.pause()
if command=="stop":
    client.stop()
if command=="next":
    client.next()
if command=="previous":
    client.previous()
if command=="clear":
    client.pause()
    client.clear()
if command[0]=="v":
    option=command[1:]
    client.pause()
    client.clear()
    client.load(option)
    client.play()
if command=="list":
    L = client.listplaylists()
    output = ""
    for _ in L:
        output+=_["playlist"] + " $ "
    print(output)
