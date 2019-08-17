from flask import Flask
import socket,threading

app = Flask(__name__)

class Main:
	def __init__(self):
		[threading.Thread(target = i).start() for i in [self.Interop, self.UI]]

	def Interop(self):
		print('1')
#                Interop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                Interop.connect(("localhost",4000))
#                Interop.send(b'Take us to your leader...')
		pass

	def UI(self):
		print('2')
		@app.route("/test")
		def test(): return '0'

Main()
