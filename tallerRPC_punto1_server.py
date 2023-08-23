#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 1
from xmlrpc.server import SimpleXMLRPCServer
class menu_matematico:
    def suma(self, p, q):

        return p+q
    def resta(self, p, q):
        return p-q

    def multi(self, p, q):
        return p*q
    
    def divi(self, p, q):
        if(q == 0):
            return "No se puede dividir por 0"
        return p/q
    
    def potencia(self, p, q):
        return p**q
    
    def fibo(self, p):
        if p == 0:
            return 0
        elif p == 1:
            return 1
        else:
            return self.fibo(p-1) + self.fibo(p-2)
        
server1 = SimpleXMLRPCServer(("localhost", 8001))
server1.register_instance(menu_matematico())
print("soy un servidor implementado en el puerto 8001")
server1.serve_forever()
