from flask import Flask
import socket,threading,websockets

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
		app.run()

	async def Reflect(self):
		pass

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 6800)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

Main()
