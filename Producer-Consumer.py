import os
import threading
import time
import random
import msvcrt
os.system('cls')

#EXECUTE IN POWERSHELL!!!!!!!!!!!!!!

def gotoxy(x,y):
    print("%c[%d;%df" % (0x1B, y, x), end='')

def kbhit():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        return key
    return None

def buffer_lista():
    numeracion = 1
    salto_linea = 0
    for i in buffer:
        if i == 0:
            gotoxy(54,8+salto_linea),print(f"{numeracion}.-Dato:              ")
        else:
            gotoxy(54,8+salto_linea),print(f"{numeracion}.-Dato: {i}    ")
        salto_linea = salto_linea + 1
        numeracion = numeracion + 1

def limpiar(valor):
    gotoxy(15+valor,13),print("                       ")
    gotoxy(15+valor,14),print("                       ")
    gotoxy(15+valor,15),print("                       ")
    gotoxy(15+valor,16),print("                       ")
    gotoxy(15+valor,17),print("                       ")
    gotoxy(15+valor,18),print("                       ")
    gotoxy(15+valor,19),print("                       ")
    gotoxy(15+valor,20),print("                       ")
    gotoxy(15+valor,21),print("                       ")
    gotoxy(15+valor,22),print("                       ")
    gotoxy(15+valor,23),print("                       ")

def dibujo_despierto(valor):
    gotoxy(15+valor,13),print("░░░░░░░░███████░░░░░░░░")
    gotoxy(15+valor,14),print("░░░░░░░█░░░░░░░█░░░░░░░")
    gotoxy(15+valor,15),print("░░░░░░█░░█░░░█░░█░░░░░░")
    gotoxy(15+valor,16),print("░░░░░░█░░░░░░░░░█░░░░░░")
    gotoxy(15+valor,17),print("░░░░░░░██░░█░░██░░░░░░░")
    gotoxy(15+valor,18),print("░░░░░░░░░█████░░░░░░░░░")
    gotoxy(15+valor,19),print("░░░█████████████████░░░")
    gotoxy(15+valor,20),print("░░███████████████████░░")
    gotoxy(15+valor,21),print("░█████░█████████░█████░")
    gotoxy(15+valor,22),print("░█████░█████████░█████░")
    gotoxy(15+valor,23),print("░████░░█████████░░████░")

def dibujo_dormido(valor):
    gotoxy(15+valor,13),print("░░░░░░░░░░░░███░███░███")
    gotoxy(15+valor,14),print("░░░░░░░░░░░░░░█░░░█░░░█")
    gotoxy(15+valor,15),print("░░░░░░░░░░░░░█░░░█░░░█░")
    gotoxy(15+valor,16),print("░░░░░░░░░░░░█░░░█░░░█░░")
    gotoxy(15+valor,17),print("░░░░░░░░░░░░███░███░███")
    gotoxy(15+valor,18),print("░░████████░░░░░░░░░░░░░")
    gotoxy(15+valor,19),print("░█░░░░░░░░██░░░░░░░░░░░")
    gotoxy(15+valor,20),print("░█░███░███░█░░░░░░░░░░░")
    gotoxy(15+valor,21),print("░█░░░░░░░░░█░░░░░░░░░░░")
    gotoxy(15+valor,22),print("░█░░░░░█░░░█░░░░░░░░░░░")
    gotoxy(15+valor,23),print("░░█████████░░░░░░░░░░░░")

def dibujo_consumiendo(valor):
    gotoxy(15+valor,13),print("░░░░░░░░░░░░░░░░░░░░░░░")
    gotoxy(15+valor,14),print("░░░███████░░░░░░░░░░░░░")
    gotoxy(15+valor,15),print("░░█░░░░░░░█░░░░░░░░░░░░")
    gotoxy(15+valor,16),print("░█░░█░░░░█░█░░░░░░░░░░░")
    gotoxy(15+valor,17),print("░█░░░░███░░█░░██████░░░")
    gotoxy(15+valor,18),print("░█░░░█░░░█░█░█░░░░░░█░░")
    gotoxy(15+valor,19),print("░░█░░░███░█░░░██████░░░")
    gotoxy(15+valor,20),print("░░░█░░░░░█░░░░░▒▒▒▒░░░░")
    gotoxy(15+valor,21),print("░░░░█████░░░░░░████░░░░")
    gotoxy(15+valor,22),print("░░████████░░░░░████░░░░")
    gotoxy(15+valor,23),print("░██████████░░░░████░░░░")

def dibujo_trabajando(valor):
    gotoxy(15+valor,13),print("░░░░░░███████████░░░░░░")
    gotoxy(15+valor,14),print("░░░░░█░░░░░░░░░░░█░░░░░")
    gotoxy(15+valor,15),print("░░░░█░███████████░█░░░░")
    gotoxy(15+valor,16),print("░░░░░█░░░░░░░░░░░█░░░░░")
    gotoxy(15+valor,17),print("██░░░░███████████░░░░██")
    gotoxy(15+valor,18),print("█████░░░░░░░░░░░░░█████")
    gotoxy(15+valor,19),print("░█████████░░░█████████░")
    gotoxy(15+valor,20),print("░░░░░█████░░░█████░░░░░")
    gotoxy(15+valor,21),print("░░░░░█████░░░█████░░░░░")
    gotoxy(15+valor,22),print("░░░░░█████░░░█████░░░░░")
    gotoxy(15+valor,23),print("░░░░░█████░░░█████░░░░░")

def dibujo_finalizado(valor):
    gotoxy(15+valor,13),print("░░░░░░░░░░░░░░░░░░░░░░░")
    gotoxy(15+valor,14),print("░░░░░░░░░░░░░░░░░░░░░░░")
    gotoxy(15+valor,15),print("░░████░░██░░░██░░████░░")
    gotoxy(15+valor,16),print("░░█████░░██░██░░░█░░░░░")
    gotoxy(15+valor,17),print("░░██░██░░░███░░░░█░░░░░")
    gotoxy(15+valor,18),print("░░█████░░░░█░░░░░███░░░")
    gotoxy(15+valor,19),print("░░████░░░░░█░░░░░█░░░░░")
    gotoxy(15+valor,20),print("░░█████░░░░█░░░░░█░░░░░")
    gotoxy(15+valor,21),print("░░██░██░░░░█░░░░░█░░░░░")
    gotoxy(15+valor,22),print("░░████░░░░░█░░░░░████░░")
    gotoxy(15+valor,23),print("░░░░░░░░░░░░░░░░░░░░░░░")

def productor():
    global buffer, productos
    posicion_lista_productor = 0
    while not salida.is_set():
        items_productor = random.randint(4,7)
        tiempo_dormir = random.randint(1,5)
        gotoxy(15,9),print("Despierto")
        dibujo_despierto(0)
        vacio.acquire()
        mutex.acquire()
        gotoxy(15,9),print("                        ")
        limpiar(0)
        gotoxy(15,9),print("Trabajando")
        dibujo_trabajando(0)
        while items_productor > 0 and not salida.is_set():
            buffer_lista()
            random_producto = random.randint(0,5)
            if posicion_lista_productor == 20:
                posicion_lista_productor = 0
            elif buffer[posicion_lista_productor] != 0:
                break
            else:   
                buffer[posicion_lista_productor] = productos[random_producto]
                posicion_lista_productor = posicion_lista_productor + 1
                items_productor = items_productor - 1
                time.sleep(1)
        lleno.release()
        mutex.release()
        while tiempo_dormir > 0 and not salida.is_set():
            gotoxy(15,9),print("                        ")
            limpiar(0)
            gotoxy(15,9),print("Dormido")
            dibujo_dormido(0)
            time.sleep(1)
            tiempo_dormir = tiempo_dormir - 1
        gotoxy(15,9),print("              ")
        limpiar(0)
    gotoxy(15,9),print("Finalizado")
    dibujo_finalizado(0)

def consumidor():
    global buffer
    posicion_lista_consumidor = 0
    while not salida.is_set():
        items_consumidor = random.randint(4,7)
        tiempo_dormir = random.randint(1,5)
        gotoxy(95,9),print("Despierto")
        dibujo_despierto(80)
        lleno.acquire()
        mutex.acquire()
        gotoxy(95,9),print("                    ")
        limpiar(80)
        gotoxy(95,9),print("Consumiendo")
        dibujo_consumiendo(80)
        while items_consumidor > 0 and not salida.is_set():
            buffer_lista()
            if posicion_lista_consumidor == 20:
                posicion_lista_consumidor = 0
            elif buffer[posicion_lista_consumidor] == 0:
                break
            else:
                gotoxy(92,10),print(f"{buffer[posicion_lista_consumidor]} consumido")  
                buffer[posicion_lista_consumidor] = 0
                posicion_lista_consumidor = posicion_lista_consumidor + 1
                items_consumidor = items_consumidor - 1
                time.sleep(1),gotoxy(85,10),print("                            ")
        mutex.release()
        vacio.release()
        while tiempo_dormir > 0 and not salida.is_set():
            gotoxy(95,9),print("                    ")
            limpiar(80)
            gotoxy(95,9),print("Dormido")
            dibujo_dormido(80)
            time.sleep(1)
            tiempo_dormir = tiempo_dormir - 1
        gotoxy(95,9),print("               ")
        limpiar(80)
        buffer_lista()
    gotoxy(95,9),print("Finalizado")
    dibujo_finalizado(80)
    
mutex = threading.Semaphore(1)
lleno = threading.Semaphore(0)
vacio = threading.Semaphore(1)
salida = threading.Event()
buffer = [0] * 20
productos = ["Pescado","KFC","Albondigas","Pizza","Cacahuates","Hamburguesa"]

gotoxy(40,1),print("##########################################")
gotoxy(45,3),print("PRODUCTO - CONSUMIDOR SIMULACION")
gotoxy(40,2),print("#"),gotoxy(40,3),print("#"),gotoxy(40,4),print("#")
gotoxy(81,2),print("#"),gotoxy(81,3),print("#"),gotoxy(81,4),print("#")
gotoxy(40,5),print("##########################################")
gotoxy(15,7),print("PRODUCTOR")
gotoxy(15,8),print("ESTADO:")
gotoxy(95,7),print("CONSUMIDOR")
gotoxy(95,8),print("ESTADO:")
gotoxy(54,7),print("Lista de Datos")

hilo_productor = threading.Thread(target= productor)
hilo_consumidor = threading.Thread(target= consumidor)

hilo_productor.start()
hilo_consumidor.start()

while True:
    buffer_lista()
    key = kbhit()
    if key == b'\x1b':
        salida.set()
        hilo_consumidor.join()
        hilo_productor.join()
        break
    time.sleep(1)
