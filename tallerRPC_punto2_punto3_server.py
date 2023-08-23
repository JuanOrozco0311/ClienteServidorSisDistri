#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 2 y PUNTO 3
from xmlrpc.server import SimpleXMLRPCServer
class login_lista:
    __saved_user = 'falcao'
    __saved_password = 'rayo2023'

    def login(self, information):
        user = information[0]
        password = information[1]
        if user == self.__saved_user and password == self.__saved_password:
            return "BIEN"
        else:
            return "Usuario o contraseña incorrectos"
        
        
server2 = SimpleXMLRPCServer(("localhost", 8002))
server2.register_instance((login_lista()))
print("soy un servidor implementado en el puerto 8002")
server2.serve_forever()