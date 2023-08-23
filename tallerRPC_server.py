#Por Juan Alejandro Orozco y Juan Camilo Palleja

#PUNTO 1
from xmlrpc.server import SimpleXMLRPCServer
class funciones_rpc:
    def suma(self, p, q):
        return p+q
    def resta(self, p, q):
        return p-q

    def multi(self, p, q):
        return p*q
    
    def divi(self, p, q):
        return p/q
    
    def invList(self, file):
        fileOpen = open(file, 'r')
        return fileOpen.read()
        
server1 = SimpleXMLRPCServer(("localhost", 8001))
server1.register_instance(funciones_rpc())
print("soy un servidor implementado con clases")
server1.serve_forever()

#PUNTO 2 y PUNTO 3