#encoding utf-8-*-

# ----------------------------
# BATALLA NAVAL EN PYTHON.
# ----------------------------


# Importamos la libreria randon para algunas funciones.
import random 
import os


# Tuplas.

# Tupla que representan una coordenada.
"""
 Un Coordenada es:
 (x, y)
 x y : Int
 0 <= x < ANCHO
 0 <= y < ALTO
"""
# Tupla que representa un estado.
"""
 Un Estado es:
 (turnoPersona, disparosRestantes, persona, oponente, ganador)
 turnoPersona: Booleano
 disparosRestantes: Int
 persona, oponente: Tablero
 ganador: Int
 0 <= disparosRestantes <= 73
 ganador: mientras que el juego no haya terminado, ganador tendra valor -1, cuando termine quien sea el ganador valdra G_PERSONA o G_OPONENTE
"""

# CONSTANTES.
# Representan los indices del valor correspondiente en un Estado.
I_TURNO = 0
I_DISPAROS = 1
I_JUGADOR = 2
I_OPONENTE = 3
I_GANADOR = 4
# Representan el ganador del juego.
G_JUGADOR = 1
G_OPONENTE = 2
G_EMPATE = 3
# Representan la direccion de un barco mediante Int.
HORIZONTAL = 0
VERTICAL = 1
# Representan la cantidad de filas y columnas que tendra el tablero.
ANCHO = 10
ALTO = 10
# Representan la cantidad de disparos.
CANT_DISPAROS = 73
# Representan las bases del juego.
ESPACIO_VACIO = ' '
BARCO = '#'
TOCADO = 'X'
AGUA = '·'
# Representa el alfabeto para los nombres de la filas del tablero.
ALFABETO = "abcdefghijklmnopqrstuvwqyz"
# Variable globales como nombre de archivos para tablero.
TABJUGADOR = "tab_jugador.txt"
TABOPONENTE = "tab_oponente.txt"

# Funciones del juego.

# limpiar_pantalla: None->None
# Limpia la pantalla para que sea mas claro el juego.
def limpiar_pantalla():
	os.system("clear")

# espera: None->None
# imprime una espera para que el jugador mire bien su juego y cuando esta decidido a atacar o ver lo que hizo su oponente pueda hacerlo facilmente.
def espera():
	input("...")

# crea_tablero_vacio: None->Tablero
# Crea un tablero 10X10 para la batalla naval.
# Ejemplo:
# EntradaI/O: None  -  Salida: [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#                               [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#                               [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#                               [" "," "," "," "," "," "," "," "," "," "]]
def crear_tablero_vacio():
    nuevoTablero = [[ESPACIO_VACIO for _ in range(ANCHO)] for _ in range(ALTO)]
    return nuevoTablero

# Tablero: Tablero
# mostrar_tablero_jugador: Tablero->None
# Dado el Tablero del jugador como parametro, lo muestra por pantalla.
# Ejemplos:
# Entrada:[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],  -   SalidaI/O:  0 1 2 3 4 5 6 7 8 9
#          [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],                a
#          [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],                b
#          [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],                c
#          [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]                d
#                                                                                                              e
#                                                                                                              f
#                                                                                                              g
#                                                                                                              h
#                                                                                                              i
#                                                                                                              j
def mostrar_tablero_jugador(tablero):
    indices = " "
    for x in range(ANCHO):
        indices += " " + str(x)
    print(indices)
    for y in range(ALTO):
        linea = ALFABETO[y]
        for x in range(ANCHO):
            linea += " " + str(tablero[y][x])
        print(linea)

# archivo: archivo
# cargar_tablero: archivo->Tablero
# Dado un archivo donde se encontrar los barcos que colocaste, los pone en el tablero.
def cargar_tablero(archivo):
        tablero = crear_tablero_vacio()
        fout = open(archivo, "r")
        linea = fout.readline()
        y = 0
        while linea != "":
            tok = linea.rstrip("\n").split(",")
            x = 0
            for i in tok:
                if i == "1":
                    tablero[y][x] = BARCO
                else:
                    tablero[y][x] = ESPACIO_VACIO
                x += 1
            y += 1
            linea = fout.readline()
        fout.close()
        return tablero

# Tablero: Tablero
# mostrar_tablero_oponente: Tablero->None
# Dado el Tablero del jugador enemigo, lo muestra por pantalla y ademas se veran tus barcos posicionados.
# Ejemplos:
# Entrada:[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],  -   SalidaI/O:  0 1 2 3 4 5 6 7 8 9
#          [" "," "," "," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "," "," "],                a
#          ["#"," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],                b
#          [" "," "," "," "," "," ","#"," "," "," "],[" "," "," "," "," "," "," "," "," "," "],                c
#          [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]                d #
#                                                                                                              e #
#                                                                                                              f
#                                                                                                              g                #
#                                                                                                              h
#                                                                                                              i
#                                                                                                              j
def mostrar_tablero_oponente(tablero):
    indices = " "
    for x in range(ANCHO):
        indices += " " + str(x)
    print(indices)
    for y in range(ALTO):
        linea = ALFABETO[y]
        for x in range(ANCHO):
            if tablero[y][x] == BARCO:
                linea += "  "
            else:
                linea += " " + str(tablero[y][x])
        print(linea)

# crear_estado_incial: None->Estado
# Se crea un estado para arrancar la batalla naval.
def crear_estado_inicial():
    turnoPersona = True
    disparosTotales = CANT_DISPAROS
    tableroJugador = cargar_tablero(TABJUGADOR)
    tableroOponente = cargar_tablero(TABOPONENTE)
    ganador = -1
    return (turnoPersona, disparosTotales, tableroJugador, tableroOponente, ganador)

# estado: Estado
# Dado los tableros del estado actual del juego los imprime por pantalla los dos tableros uno abajo del otro con sus respectivos mensajes.
# Ejemplo:
# Entrada: [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "], , [["#"," "," "," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "," "," "],
#           [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],    [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#           [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],    [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#           [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],    [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#           [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]    [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," ","#"]]
# SalidaI/O:

# TABLERO BARCO JUGADOR / DISPAROS OPONENTE:

#  0 1 2 3 4 5 6 7 8 9
#a #
#b #
#c
#d
#e
#f
#g
#h
#i
#j                    #


# TABLERO DISPAROS JUGADOR:

#  0 1 2 3 4 5 6 7 8 9
# a
# b
# c
# d
# e
# f
# g
# h
# i
# j
def mostrar_juego(estado):
    print("\nTABLERO BARCO JUGADOR / DISPAROS OPONENTE:\n")
    mostrar_tablero_jugador(estado[I_JUGADOR])
    print("\n\nTABLERO DISPAROS JUGADOR:\n")
    mostrar_tablero_oponente(estado[I_OPONENTE])

# string: String
# crear_coordenada: String->Cordenada
# Dado un string simulando una entrada para que el jugador ataque al barco enemigo, devuelve una coordenada valida para poder graficar en el tablero.
# Ejemplos:
# Entrada: "a1"  -  Salida: (0,1)
# Entrada: "j9"  -  salida: (9,9)
# Entrada: "e6"  -  Salida: (4,6)
def crear_coordenada(string):
    posicionX = ALFABETO.index(string[0])
    posicionY = int(string[1])
    return (posicionX, posicionY)
# Testing.
def test_crear_cordenada():
        assert crear_coordenada("a1") == (0,1)
        assert crear_coordenada("j9") == (9,9)
        assert crear_coordenada("e6") == (4,6)
        
# ingresar_coordenada: None->Coordenada
# Crea una coordenada correctamente.
# Ejemplos:
# EntradaI/O: "a1"  -  Salida: (1,1)
# EntradaI/O: "p1" "b3"  -  Salida: (2,3)
def ingresar_coordenada():
    resp = ""
    while not len(resp) == 2:
        resp = input("Ingrese coordenada (ej: a0) : ")
        if not len(resp) == 2 :
            resp = ""
            continue
        elif not resp[0] in ALFABETO:
            resp = ""
        elif ALFABETO.index(resp[0]) >= ALTO:
            resp = ""
        elif not resp[1].isdigit():
                resp = ""
    return crear_coordenada(resp)

# coord: Coordenada
# tableroOponente: Tablero
# verificar_coordenada_ataque: Coordenada->Tablero->Boolean
# Dado una cordenada y el tablero del enemigo, verifica si la coordenada del ataque del jugador al enemigo es correcta.
# Ejemplos:
# Entrada: a1  -  Salida: True
# Entrada: 99  -  Salida: False
def verificar_coordenada_ataque(coord, tableroOponente):
    x = coord[0]
    y = coord[1]
    return not (tableroOponente[x][y] == AGUA or tableroOponente[x][y] == TOCADO)

# tablero: Tablero
# coord: Coordenada
# direccion : Coordenada
# verificar_barco_vivo: Tablero->Coordenada->Cordenada->Boolean
# Verifica si el barco donde el jugador le pego un misil al enemigo se hundio o solo lo toco.
# El ultimo argumento debe ser la tupla (0, 0)
def verificar_barcos_vivo(tablero, coord, direccion):
    nueva_coord = (coord[0] + direccion[0], coord[1] + direccion[1])
    if nueva_coord[0] < 0 or nueva_coord[0] >= ANCHO:
        return False
    if nueva_coord[1] < 0 or nueva_coord[1] >= ALTO:
        return False
    valor = tablero[nueva_coord[0]][nueva_coord[1]]
    if valor == ESPACIO_VACIO:
        return False
    if valor == BARCO:
        return True
    if direccion == (0, 0):
        return verificar_barcos_vivo(tablero, nueva_coord, (1, 0)) or verificar_barcos_vivo(tablero, nueva_coord, (-1, 0)) or verificar_barcos_vivo(tablero, nueva_coord, (0, 1))or verificar_barcos_vivo(tablero, nueva_coord, (0, -1))
    else:
        return verificar_barcos_vivo(tablero, nueva_coord, direccion)

# estado: Estado
# tablero: Tablero
# modificar_tablero_jugador: Estado->Tablero->Estado
# Modifica el tablero del jugador para que se vea el juego de donde van cayendo sus misiles.
def modificar_tablero_jugador(estado, tablero):
    return estado[0:2] + (tablero,) + estado[3:]

# estado: Estado
# modificar_turno: Estado->Estado
# Devuelve un estado con el turno opuesto al dado
def modificar_turno(estado):
    nuevoTurno = not estado[I_TURNO]
    return (nuevoTurno,) + estado[1:]
# estado: Estado
# ataque_jugador: Estado->Estado
# Dado un estado del jugador, se ingresa una coordenada hasta que es valida y verifica si no se uso, si esta
# se uso, pierde el turno si no se fija en el tablero enemigo y lo guarda en el estado actual.
# lo que sucedio, y guarda el tablero en un nuevo estado.
def ataque_jugador(estado):
    tablero_jugador = estado[I_JUGADOR]
    tablero_enemigo = estado[I_OPONENTE]
    coord = ingresar_coordenada()
    x = coord[0]
    y = coord[1]
    if(tablero_enemigo[x][y] == AGUA or tablero_enemigo[x][y] == TOCADO):
        print("Posicion ya seleccionada\nPerdiste el turno")
        estado = modificar_turno(estado)
        return estado
    if tablero_enemigo[x][y] == BARCO:
        tablero_enemigo[x][y] = TOCADO
        print("TOCADO")
        if not verificar_barcos_vivo(tablero_enemigo, coord, (0, 0)):
            print("HUNDIDO")
    else:
        tablero_enemigo[x][y] = AGUA
        print("AGUA")
    estado = modificar_tablero_oponente(estado, tablero_enemigo)
    estado = modificar_turno(estado)
    return estado

# coordenada_aleatoria: None->Coordenada
# Devuelve una cordenada para el jugador enemigo, con esta atacara al tablero del jugador.
# Ejemplos:
# EntradaI/O: None  -  Salida: (0,0)
# EntradaI/O: None  -  Salida: (9,2)
# EntradaI/O: None  -  Salida: (9,9)
def coordenada_aleatoria():
    return (random.randint(0, ALTO - 1), random.randint(0, ANCHO - 1))

# estado: Estado
# ataque_oponente: Estado->Estado
# Dado un estado del enemigo, se ingresa una coordenada aleatoriamente y verifica si no se uso, si esta
# se uso, pierde el turno si no se fija en el tablero jugador e imprime por pantalla
# lo que sucedio, y guarda el tablero en un nuevo estado.
def ataque_oponente(estado):
    tableroJugador = estado[I_JUGADOR]
    tableroOponente = estado[I_OPONENTE]
    coord = coordenada_aleatoria()
    x = coord[0]
    y = coord[1]
    while not verificar_coordenada_ataque(coord, tableroJugador):
        coord = coordenada_aleatoria()
    print("POSICION ATAQUE OPONENTE : ", ALFABETO[x], y)
    if tableroJugador[x][y] == BARCO:
        tableroJugador[x][y] = TOCADO
        print("TOCADO")
        if not verificar_barcos_vivo(tableroJugador, coord, (0, 0)):
            print("HUNDIDO")
    else:
        tableroJugador[x][y] = AGUA
        print("AGUA")
    estado = modificar_tablero_jugador(estado, tableroJugador)
    estado = modificar_turno(estado)
    return estado

# estado: Estado
# tablero: Tablero
# modificar_tablero_jugador: Estado->Tablero->Estado
# Modifica el tablero del oponente para que vea el jugador donde le estan cayendo misiles en sus barcos.
def modificar_tablero_oponente(estado, tablero):
    return estado[0:3] + (tablero,) + estado[4:]

# estado: Estado
# disminuir_disparos:Estado->Estado
# Disminuye la cantidad de disparos que realizan los jugadores.
def disminuir_disparos(estado):
    return (estado[0],) + (estado[1] - 1,) + estado[2:]

# estado: Estado
# verificar_fin_juego: Estado->Estado
# Verifica quien es el ganador o si hay empate y lo modifica en el estado con un 1 si gano el jugador
# con un 2 si gano el enemigo o 3 si hay empate.
def verificar_fin_juego(estado):
    g_jugador = True
    for y in range(ALTO):
        if not g_jugador:
                break
        for x in range(ANCHO):
            if estado[I_OPONENTE][x][y] == BARCO:
                g_jugador = False
                break
    g_oponente = True
    for y in range(ALTO):
        if not g_oponente:
                break
        for x in range(ANCHO):
            if estado[I_JUGADOR][x][y] == BARCO:
                g_oponente = False
                break
    if g_jugador and g_oponente:
        estado = modificar_ganador(estado, G_EMPATE)
    elif g_jugador:
        estado = modificar_ganador(estado, G_JUGADOR)
    elif g_oponente:
        estado = modificar_ganador(estado, G_OPONENTE)
    elif estado[I_DISPAROS] == 0:
        estado = modificar_ganador(estado, G_EMPATE)
    return estado

# estado: Estado
# ganador: Int 
# modificar_ganador: Estado->Int->Estado
# Modifica el estado del ganador, donde comienza con un -1, y cambia segun sea el ganador:
# 1 si gana el jugador
# 2 si gana el enemigo
def modificar_ganador(estado, ganador):
    return estado[0:4] + (ganador,)


# Jugar la batalla naval.
def jugar():
    limpiar_pantalla()
    estado = crear_estado_inicial();
    mostrar_juego(estado)
    while estado[I_GANADOR] == -1:
        if(estado[I_TURNO]):
            print("\nTURNO JUGADOR")
            estado = ataque_jugador(estado)
            espera()
            limpiar_pantalla()
        else:
            print("\nTURNO OPONENTE")
            estado = ataque_oponente(estado)
            estado = disminuir_disparos(estado)
            estado = verificar_fin_juego(estado)
            espera()
            limpiar_pantalla()
        mostrar_juego(estado)
    print("FINAL DEL JUEGO.....")
    if(estado[I_GANADOR] == G_JUGADOR):
        print("GANASTE!!!!!!! ヘ( ^o^)ノ＼(^_^ )")
    elif estado[I_GANADOR] == G_OPONENTE:
        print("PERDISTE (╯°□°）╯︵ ┻━┻")
    else:
        print("EMPATE (ಠ_ಠ)")

# Ejecucion de la batalla naval.
jugar()
