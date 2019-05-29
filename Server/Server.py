import sys,socket,threading
from Command import Executor,Command

class Recevier(threading.Thread):

    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection=connection

    def run(self):
        while(True):
            try:
                print("heeloo")
                data = self.connection.recv(1024)
                data=data.decode("utf-8")
                command=Command()
                print(data)
                command.toCommand(data)
                executor.Exe(command)
            except:
                None








SID=26489413
PortNumber=2629
IPAddress='localhost'
MaxUserNumber=10
Connections=[]
ReciverConnections=[]
executor=Executor()
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (IPAddress, PortNumber)
sock.bind(server_address)

print("\nServer Status:")
print("--------------------------")
print("IP Address:"+IPAddress)
print("Port Number:"+str(PortNumber))
print("--------------------------\n")

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    print('Connection Comming..')
    if 1 < MaxUserNumber:
        print('hi')
        Connections.append(connection)
        rec=Recevier(connection)
        rec.start()
        ReciverConnections.append(rec)




def send(StrCommand,IPAddress,PortNumber):
    for connection in Connections:
        add=connection.getsockname()[0]
        port=int(connection.getsockname()[1])

    if IPAddress==add and PortNumber==port:
        connection.sendall(StrCommand)





