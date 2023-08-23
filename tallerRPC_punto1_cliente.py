#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 1
import xmlrpc.client
import os

s = xmlrpc.client.ServerProxy('http://localhost:8001')
option = ''

while(option != 'g'):
    os.system("cls")
    option = str(input("*************Menú Matemático******************************\na. Sumar\nb. Restar\nc. Multiplicar\nd. Dividir\ne. Potencia\nf. Fibonacci\ng. Salir\nEscoja su opción:"))
    if option == 'a':
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        print("La suma es: " + str(s.suma(a,b)))
        os.system("pause")
    elif option == 'b':
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        print("La resta es: " + str(s.resta(a,b)))
        os.system("pause")
    elif option == 'c':
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        print("La multiplicacion es: " + str(s.multi(a,b)))
        os.system("pause")
    elif option == 'd':
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        print("La division es: " + str(s.divi(a,b)))
        os.system("pause")
    elif option == 'e':
        a = int(input('Ingrese la base: '))
        b = int(input('Ingrese el exponente: '))
        print("La potencia es: " + str(s.potencia(a,b)))
        os.system("pause")
    elif option == 'f':
        a = int(input('Que termino desea conocer: '))
        print("EL valor de la sucesion de fibbonacci en ese termino es: " + str(s.fibo(a)))
        os.system("pause")

    