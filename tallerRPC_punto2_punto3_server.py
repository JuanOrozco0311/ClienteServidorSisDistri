#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 2 y PUNTO 3
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
class login_lista:
    __saved_user = 'falcao'
    __saved_password = 'rayo2023'

    def login(self, information):
        user = information[0]
        password = information[1]
        if user == self.__saved_user and password == self.__saved_password:
            return "Correcto"
        else:
            return "Usuario o contraseña incorrectos"
    
    def invList(self, fileReceive):
        with open('read.txt','wb') as file:
            file.write(fileReceive.data)
            
        with open('read.txt', 'r') as file:
            container = file.readlines()
            inverted_content = container[::-1]
            
        with open('read.txt', 'w') as file:
            for x in inverted_content:
                file.write(x)
        
        with open('read.txt', 'rb') as file:
            return Binary(file.read())
    
    def mostFrequent(self, fileReceive):
        with open('read.txt','wb') as file:
            file.write(fileReceive.data)
        with open('read.txt', 'r') as file:
            container = file.readlines()
            return max(set(container), key = container.count)
        
server2 = SimpleXMLRPCServer(("localhost", 8002))
server2.register_instance((login_lista()))
print("soy un servidor implementado en el puerto 8002")
server2.serve_forever()