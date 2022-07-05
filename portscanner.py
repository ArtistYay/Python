import socket  # We are importing the socket library. A socket or a Socket API are used to send messages across a network.

target = "127.0.0.1"

def portscan(port): # Define what portscan will do
	try: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is for protocols based on IP addresses using IPV4. SOCK_STREAM means to just run on TCP.
		sock.connect((target, port)) # Telling the sock to connect to a certain port you input.
		return True # If the port is open it will say true or false
	except:
		return False

print(portscan(90)) 