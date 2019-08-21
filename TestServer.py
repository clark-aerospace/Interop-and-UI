import socket

SO = socket.socket()
SO.bind(('',4000))
SO.listen(3)
while(True):
	print(SO.accept())
