#!/usr/bin/env python
import socket
serverPort = 80
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('', serverPort))
serverSock.listen(1)
