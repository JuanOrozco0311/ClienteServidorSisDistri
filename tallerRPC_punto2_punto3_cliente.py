#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 2 y PUNTO 3
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8002')

user = str(input('Sistema de autentificaion:\n\nIngrese su usuario: '))
password = str(input('Ingrese su contraseña: '))
login = s.login((user, password))
if login == 'Correcto':
    print('\n',login, '\n')
    print("Aplicativo para manipular una lista de 15 numeros enteros\n")
    print("Ingrese los numeros enteros que desea agregar a la lista.\n")
    length = 15
    l = []
    for x in range(length):
        item = input('Ingrese el valor: ')
        l.append(item+'\n')
        file = open('items.txt', 'w')
    for item in l:
        file.write(item)
    file.close()
    print('\nLa lista invertida es: \n',s.invList('items.txt'))
    print('El elemento de la lista que mas se repite es: ',s.mostFrequent('items.txt'))
else:
    print(login)

