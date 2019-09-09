from flask import Flask
import socket,threading,websocket,random

class Main:
	def __init__(self):
		[threading.Thread(target = i).start() for i in [self.Interop, self.UI]]

	def Interop(self):
		print('Connecting to a server on localhost...')
		Interop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		while(True):
			try:
				Interop.connect(("localhost",4000))
				break
			except:pass
		Interop.send(b'Take us to your leader...')
		print("Was able to connect to a server on localhost, port 4000.")

	def UI(self):
		print('2')
		app = Flask(__name__)
		@app.route("/test")
		def test(): return open("./Pages/Main.html",'r').read()
		@app.route("/Motivation.mp3")
		def Motivation(): return open("./Pages/Motivation.mp3",'rb').read()
		app.run()

	def Reflect(self):
		def on_message(ws, message): print(message)
		def on_error(ws, error): print(error)
		def on_close(ws): print("[CLOSING TIME]")
		def on_open(ws):
			def run(*args):
				while(True):
					time.sleep(5)
					ws.send(str(random.randint(0,1000000)))
				ws.close()
			threading.Thread(run,())
		print("???")
		websocket.enableTrace(True)
		ws = websocket.WebSocketApp("127.0.0.1:6800",
				on_message = on_message,
				on_error = on_error,
				on_close = on_close)
		ws.on_open = on_open
		ws.run_forever()


Main()

if __name__ == "__main__": pass
