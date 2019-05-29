import random
from Server import ServerError
#CommmandList
Commands={"Verify":"VR","Get":"G","Login":"LG","Post":"P","SingleCommandMode":"SCM","MultiCommandMode":"MCM","Error":"ER"}
#CC == connection Comming , C == Client , SID == Server ID , ID == Client "User" ID

#Client Command
#Verify Command Format= "Verify , C Address , C Port "
#Login Command Format= "Login , UserName , Password " @ server append @ " CC Address , CC Port"
#Post Command Format= "Post , ID , Value_Name , Value " @ server append @ " CC Address , CC Port"
#Get Command Format= "Get , ID , Value_Name , Value " @ server append @ " CC Address , CC Port"

#Server Command
#Verify Command Format= "Verify , Server ID (SID)"
#Post Command Format= "Post , SID , Value_Name , Value " 
#Error Command Format= "Error , SID , ErrorMsg , ErrorCode " 


class Command :
    def __init__(self,name=None,key=86,autoED=True):
        self.CommandList = []
        self.CommandName=name
        self.key=key
        self.autoED=autoED
    
    def addToken(self,token):
        self.CommandList.append(str(token))

    def setCommandName(self,name):
        self.CommandName=name
    
    def getCommand(self):
        command = self.CommandName
        for token in self.CommandList:
            command=command+';;;'+token

        if self.autoED:
            command=self.encryption(command)
        return command
    
    def toCommand(self,stringcommand):
        if self.autoED:
            stringcommand=self.decryption(stringcommand)
        listOfCommand = stringcommand.split(';;;')
        self.CommandName=listOfCommand[0]
        listOfCommand.remove(listOfCommand[0])
        self.CommandList=listOfCommand.copy()
    
    def getName(self):
        return self.CommandName
    
    def getTokenList(self):
        return self.CommandList

    def encryption(self,StrCommand):
        charLsit=list(StrCommand)
        newstr=""
        for c in charLsit:
            c=chr(ord(c) ^ self.key) 
            newstr+=c
        return newstr
    
    def decryption(self,decCommand):
        charLsit=list(decCommand)
        newstr=""
        for c in charLsit:
            c=chr(ord(c) ^ self.key) 
            newstr+=c
        return newstr



class Executor:
    
    def __init__(self):
        self.users=[]
        self.NumberOfUsers=0

    def Verify(self,command):
        return True

    def checkDataBase(self,name,password):
        return True

    def Login(self,command):
        #Login Command Format= "Login , UserName , Password " @ server append @ " CC Address , CC Port"
        name=command.getTokenList()[0]
        password =command.getTokenList()[1]
        Address =command.getTokenList()[2]
        Port =int(command.getTokenList()[3])
        if self.checkDataBase(name,password):
            import Server
            if self.NumberOfUsers<Server.MaxUserNumber:
                user=User(name,self.NumberOfUsers)
                user.Port=Port
                user.Address=Address
                self.users.append(user)
                self.NumberOfUsers+=1
                #Verify Command Format= "Verify , Server ID (SID)" 
                command=Command(Commands["Verify"])
                command.addToken(Server.SID)
                command.addToken("ID")
                Server.send(command.getCommand(),user.Address,user.Port)
            else:
                #Error Command Format= "Error , SID , ErrorMsg , ErrorCode " 
                command=Command(Commands["Error"])
                command.addToken(Server.SID)
                command.addToken("Server Have Max User")
                command.addToken(ServerError.Command_Error)
                Server.send(command.getCommand(),Address,Port)
    
    def Post(self,command):
        #Post Command Format= "Post , ID , Value_Name , Value " @ server append @ " CC Address , CC Port"
        ID=int(command.getTokenList()[0])
        Value_Name=command.getTokenList()[1]
        Value=command.getTokenList()[2]
        Address=command.getTokenList()[3]
        Port=int(command.getTokenList()[4])
        if self.checkUser(ID,Address,Port):
            print("[V]Command\\Executer\\PostCommand>>"+Value_Name+":"+Value)
        else:
            #Error Command Format= "Error , SID , ErrorMsg , ErrorCode" 
            command=Command(Commands["Error"])
            import Server
            command.addToken(Server.SID)
            command.addToken("Error Command Source")
            command.addToken(ServerError.Source_Error)
            Server.send(command.getCommand(),Address,Port)

    def checkUser(self,ID,Address,Port):
        try:
            user = self.users[ID]
            if user.getAddress()==Address and user.getPort()==Port:
                return True
            return False
        except:
            return False
    
    def Exe(self,command):
        if command.getName()==Commands["Verify"]:
            return self.Verify(command)
        if command.getName()==Commands["Login"]:
            return self.Login(command)       
        if command.getName()==Commands["Post"]:
            return self.Post(command)  





class User :
    def __init__(self,UserName,ID):
        self.UserName=UserName
        self.ID=ID
        self.Port=None
        self.Address=None
    
    def checkID(self,ID):
        if self.ID==ID:
            return True
        else :
            return False
    
    def getID(self):
        return self.ID
    
    def getUserName(self):
        return self.UserName
    
    def getPort(self):
        return self.Port
    
    def getAddress(self):
        return self.getAddress
    


