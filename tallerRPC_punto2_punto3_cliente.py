#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 2 y PUNTO 3
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8002')

user = str(input('Sistema de autentificaion:\n\nIngrese su usuario: '))
password = str(input('Ingrese su contraseña: '))
print(s.login((user, password)))
