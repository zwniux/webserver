#!/usr/bin/env python
# coding=utf-8
import socket
import os.path

def findFile(directory):
  newDir = directory
  if newDir == '/':
    newDir = '/index.html'
  fullDir = docRoot + newDir
  return fullDir

def readFile( direct ):
  if os.path.exists(direct):
	f = open(direct, 'r')
	content = f.read()
	return (content, 200)
  else:
	return ('', 404)


respMsg = {
	200:
	'''
	HTTP/1.1 200 OK
	Connection: close
	Server: NiuServer/0.0 (Ubuntu)

	''',
	404:
	'''
	HTTP/1.1 404 Not Found
	Connection: close

	'''
	}

docRoot = '/home/zwniux/project/network/webserver'
serverPort = 80
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('', serverPort))
serverSock.listen(1)
print "开启服务器....."
while 1:
  connectSock, addr = serverSock.accept()
  message = connectSock.recv(10240)
  lines = message.split('\n')
  reqLine = lines[0].split(' ')
  directory = reqLine[1]
  fullDir = findFile(directory)
  content, num = readFile(fullDir)
  message = respMsg[num] + content + '\n'
  print message
  connectSock.send(message)
  connectSock.close()
serverSock.close()


