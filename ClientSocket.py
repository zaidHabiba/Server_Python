import socket
import sys



class Client:
    def __init__(self,Address,Port):
        self.Address = Address
        self.Port = Port
        self.DebuggingMode=True
        self.server_address = (self.Address, self.Port)
    
    def restart(self):
        try:
            self.sock.close()
            self.debugg("Restart Done")
        except:
            self.debugg("Client not start")
        self.debugg("Client Auto start")
        self.start()
        

    def setPort(self,Port):
        self.Port=Port

    def setAddress(self,Address):
        self.Address=Address

    def setDebuggingMode(self,flag):
        self.DebuggingMode=flag   

    def debugg(self,msg):
        if self.DebuggingMode:
            print (msg)    
    
    def start(self):
        self.debugg("Server Connect to Address:"+self.Address+" and Port:"+str(self.Port))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.Address, self.Port)
        #self.sock.bind(self.server_address)
        try:
            self.sock.connect(self.server_address)
            self.debugg("Server Connect")
        except:
            self.debugg("Server Connect failed")

    def send(self,msg):
        try:
            msgBytes=bytes(msg, encoding='utf-8')
            self.sock.sendall(msgBytes)
            self.debugg("Msg send")
        except:
            self.debugg("Msg not send")

    def receive(self,size):
        msg = self.sock.recv(size)
        self.debugg("Msg receive: "+str(msg))
        return msg

    def close(self):
        self.sock.close()
        