import ClientSocket
from Server import Command 


PortNumber = 2629
Address='localhost'


client =ClientSocket.Client(Address,PortNumber)
client.start()
client.setDebuggingMode(True)


#Login Command Format= "Login , UserName , Password " @ server append @ " CC Address , CC Port"
comand=Command.Command(Command.Commands["Login"])
comand.addToken("Zaid")
comand.addToken("00zaid00")
client.send(comand.getCommand())

while(True):
    data = client.receive(1024)
    data=data.decode("utf-8")
    print(data)
