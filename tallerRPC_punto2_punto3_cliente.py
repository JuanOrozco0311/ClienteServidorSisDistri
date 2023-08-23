#Por Juan Alejandro Orozco y Juan Camilo Palleja
import xmlrpc.client
a =int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el segundo numero: '))
length = 15
l = []
for x in range(length):
    item = input('Ingrese el valor: ')
    l.append(item+'\n')
file = open('items.txt', 'w')
for item in l:
    file.write(item)
file.close()
s = xmlrpc.client.ServerProxy('http://localhost:8001')
print("la suma es: " + str(s.suma(a,b)))
print("la resta es: " + str(s.resta(a,b)))
print("la multiplicacion es: " + str(s.multi(a,b)))
print("la division es: " + str(s.divi(a,b)))
#PUNTO 2 
print("la division es: " + str(s.invList('items.txt')))
#PUNTO 3