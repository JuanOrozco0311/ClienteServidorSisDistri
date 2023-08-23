#Por Juan Alejandro Orozco y Juan Camilo Palleja
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8001')
option = str(input("*************Menú Matemático******************************\na. Sumar\nb. Restar\nc. Multiplicar\nd. Dividir\ne. Potencia\nf. Fibonacci\nEscoja su opción:"))

while(option):
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))
    if option == 'a':
        print("la suma es: " + str(s.suma(a,b)))
        break
    elif option == 'b':
        print("la resta es: " + str(s.resta(a,b)))
        break
    elif option == 'c':
        print("la multiplicacion es: " + str(s.multi(a,b)))
        break
    elif option == 'd':
        print("la division es: " + str(s.divi(a,b)))
        break
    elif option == 'd':
        print("la division es: " + str(s.divi(a,b)))
        break
    elif option == 'd':
        print("la division es: " + str(s.divi(a,b)))
        break
    else:
        print("Finalizado")