#!/usr/bin/python

import socket
import SimpleHTTPServer
import SocketServer

#setting up some sockets
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setting shit up on port 80 - for webserver
PORT = 80
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print("Web Server Started on PORT: ", PORT)

#SWervin!
httpd.serve_forever()
