#Por Juan Alejandro Orozco y Juan Camilo Palleja
#PUNTO 2 y PUNTO 3
import xmlrpc.client
import os

s = xmlrpc.client.ServerProxy('http://localhost:8002')
    
def login():
    user = str(input('Sistema de Autenticación:\n\nIngrese su usuario: '))
    password = str(input('Ingrese su contraseña: '))
    return s.login((user, password))

def listCreator():
    print("Aplicativo para manipular una lista de 15 numeros enteros\n")
    print("Ingrese los numeros enteros que desea agregar a la lista.\n")
    length = 15
    l = []
    l2 = []
    for x in range(length):
        item = input('Ingrese el valor: ')
        try:
            l2.append(int(item))
            l.append(item+'\n')
        except:
            print('El valor ingresado no es un numero entero, se agregara un 0 a la lista')
            l2.append(0)
            l.append('0\n')
    file = open('items.txt', 'w')
    for item in l:
        file.write(item)
    file.close()
    print(f'\nLa lista original es:\n{l2}')

def invertList():
    with open('items.txt', 'rb') as file:
        file_content = file.read()
    inverted_list_file = s.invList(file_content)
    with open('items.txt', 'wb') as file:
        file.write(inverted_list_file.data)
    file_open = open('items.txt', 'r')
    invert_result = file_open.readlines()
    file_open.close()
    inverted_list = []
    for value in invert_result:
        inverted_list.append(int(value.split('\n')[0]))
    print(f'\nLa lista invertida es:\n{inverted_list}\n')

def mostFrequent():
    with open('items.txt', 'rb') as file:
        file_content = file.read()
    print('El elemento de la lista que mas se repite es:',s.mostFrequent(file_content))
    
def main():
    option = 1
    os.system('cls')
    print("Bienvenido al Login\n")
    result = login()
    if result == 'Correcto':
        while option != 0:
            os.system('cls')
            print("Menu\n")
            print("Eliga una opcion:\n")
            print("1. Invertir lista\n")
            print("2. Valor más repetido\n")
            print("0. Salir del programa\n")
            option = int(input("Ingrese la opción: "))
            if option == 1:
                os.system('cls')
                listCreator()
                invertList()
                os.system('pause')
            elif option == 2:
                os.system('cls')
                listCreator()
                print('\n')
                mostFrequent()
                os.system('pause')
    else:
        print(result)

main()