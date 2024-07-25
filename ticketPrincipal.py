'''
Una empresa dedicada a la gestión de peajes en rutas requiere un programa para gestionar los movimientos de cobro
en cada una de sus ventanillas. Por cada ticket cobrado se tienen los siguientes datos: número de ticket (un entero),
nombre de puesto de peaje (una cadena de caracteres), un número entre 1 y 10 para indicar la ventanilla o carril que
hizo el cobro en ese puesto, una cadena para la patente del automóvil al que se le hizo el cobro, y finalmente un
número entero para indicar el monto que se cobró.
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos [Máximo 4 puntos
por este requerimiento, incluyendo también convenciones de estilo y otros aspectos del programa general]:
• En uno de ellos, definir la clase Ticket que represente al registro a usar en el programa, y las funciones básicas
para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de
datos, aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones
para desarrollar las siguientes tareas...

[1]. Generar un arreglo de n registros de tipo Ticket que contenga los datos de los cobros realizados (cargue el valor de
n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
generando los datos en forma aleatoria. El arreglo debe permanecer en todo momento ordenado por el número
de ticket durante la carga. Cada vez que se seleccione esta opción, el arreglo debe ser generado nuevamente
desde cero. Será considerada la eficiencia de la estrategia de carga y los algoritmos que aplique. [Máximo 4 puntos
entre los ítems 1 y 2 juntos].

[2]. Mostrar todos los datos del arreglo generado en el punto 1, a razón de un registro por renglón. Al final del listado,
muestre una línea adicional con el monto total recaudado por todos los tickets que se mostraron. [Máximo 4
puntos entre los ítems 1 y 2 juntos].

[3]. En base al arreglo generado en el punto 1 determinar si existe un ticket cuyo número sea num (cargar num por
teclado). Si existe, informe solo el nombre del puesto de peaje y el número de ventanilla o carril de ese registro. Si
no existe, informe con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que cumpla el
criterio de busqueda pedido. [Máximo 4 puntos].

[4]. En base al arreglo generado en el punto 1, determinar cuántos tickets se cobraron en cada una de las 10 posibles
ventanillas o carriles posibles. Mostrar solo los contadores diferentes de cero. [Máximo 4 puntos].

[5]. En base al arreglo generado en el punto 1 determinar cuántas veces se le cobró peaje al automóvil cuya patente es
pat (cargue la cadena pat por teclado). Note que esa patente podría estar varias veces en el vector, y ahora sí se
pide contar todas sus apariciones. Si no existe ningún ticket emitido para esa patente, informe con un mensaje.
[Máximo 4 puntos].

[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
tickets emitidos por ventanillas con número menor a 6. [Máximo 4 puntos].

[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando la cantidad de registros
mostrados. [Máximo 4 puntos].
'''


import os
import pickle
from random import *
from classTicket import *


def mayorQue(li, msj = 'Ingrese un numero: '):
    n = int(input(msj))
    while n < li:
        print()
        print(f'ERROR, el numero debe ser mayor a {li}, vuelva a intentarlo...')
        print()
        n = int(input(msj))
    return n


def entre(li, ls, msj = 'Ingrese un numero: '):
    n = int(input(msj))
    while n < li or n > ls:
        print()
        print(f'ERROR, el numero debe estar entre {li}, y {ls}, vuelva a intentarlo...')
        print()
        n = int(input(msj))
    return n


def menu():
    print('BIENVENIDO AL MENU DE OPCIONES...')
    print('1. Generar arreglo de tickets')
    print('2. Mostrar arreglo de tickets')
    print('3. Buscar tocket segun nombre')
    print('4. Contar tickets')
    print('5. Contar apariciones')
    print('6. Generar Binario')
    print('7. Leer Binario')
    print('8. Salir del programa.')
    print()
    op = entre(1, 8, 'Elija su opcion: ')
    print()
    return op


def addInOrder(tickets, x):
    izq, der = 0, len(tickets) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x.num < tickets[c].num:
            der = c - 1
        else:
            izq = c + 1
    tickets.insert(izq, x)


def generarArreglo(tickets, n):
    for i in range(n):
        num = randint(100, 400)
        puesto = chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90))
        ventanilla = randint(1, 10)
        patente = chr(randint(65, 90)) + str(randint(0, 9)) + str(randint(0, 9)) + chr(randint(65, 90))
        monto = randint(1000, 10000)
        tx = Ticket(num, puesto, ventanilla, patente, monto)
        addInOrder(tickets, tx)
    return tickets


def mostrarArreglo(tickets):
    monto = 0
    for ticket in tickets:
        print(ticket)
        monto += ticket.monto
    print('El monto recaudado entre todos los tickets mostrados es de: ', monto)


def existe(tickets, num):
    n = len(tickets)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if tickets[c].num == num:
            r = (f'Puesto del peaje: {tickets[c].nombre}, Numero de ventanilla: {tickets[c].ventanilla}.')
            return r
        elif num < tickets[c].num:
            der = c - 1
        elif num > tickets[c].num:
            izq = c + 1
    if izq < der:
        r = (f'Puesto del peaje: {tickets[izq].nombre}, Numero de ventanilla: {tickets[izq].ventanilla}.')
        return r
    return 'Que lastima, ese ticket no existe....'


def contar(tickets):
    conteo = [0] * 10
    for ticket in tickets:
        conteo[ticket.ventanilla] += 1
    return conteo


def mostrar4(conteo):
    for i in range(len(conteo)):
        if conteo[i] != 0:
            print(f'Para la ventanilla: {i} hubo {conteo[i]} tickets.')


def contarApariciones(tickets, pat):
    cuantas = 0
    for ticket in tickets:
        if ticket.patente == pat:
            cuantas += 1
    if cuantas == 0:
        return 'No existe ningun ticket emitido para esa patente.'
    else:
        return cuantas


def generarBinario(ruta, tickets):
    archivo = open(ruta, 'wb')
    for ticket in tickets:
        if ticket.ventanilla < 6:
            pickle.dump(ticket, archivo)
    archivo.close()


def leerBinario(ruta):
    if not os.path.exists(ruta):
        print('Ruta inaccesible...')
        return
    tamanio = os.path.getsize(ruta)
    cantidad = 0
    archivo = open(ruta, 'rb')
    while archivo.tell() < tamanio:
        tic = pickle.load(archivo)
        print(tic)
        cantidad += 1
    print('Se mostraron', cantidad, 'registros.')
    archivo.close()


def test():
    op = -1
    tickets = []
    ruta = 'tickets.dat'
    while op != 0:
        op = menu()

        if op == 8:
            print('Fue un gusto conocerte, adios!!!')
            print()
            break

        if op == 1:
            tickets = []
            n = mayorQue(0, 'Ingrese la cantidad de tickets que desea cargar: ')
            generarArreglo(tickets, n)
            print('Carga exitosa!!!')
            print()

        if op == 2:
            mostrarArreglo(tickets)
            print()

        if op == 3:
            num = entre(100, 400, 'Ingrese el numero de ticket que esta buscando: ')
            print()
            print(existe(tickets, num))
            print()

        if op == 4:
            conteo = contar(tickets)
            mostrar4(conteo)
            print()

        if op == 5:
            pat = input('Ingrese la patente EXACTA del vehiculo el cual quiere saber cuantos tickets se le cobraron: ')
            print(contarApariciones(tickets, pat))
            print()

        if op == 6:
            generarBinario(ruta, tickets)
            print('Archivo binario generado correctamente...')
            print()

        if op == 7:
            leerBinario(ruta)
            print()


if __name__ == '__main__':
    test()
