import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tablero(num_filas,num_columnas):
    """
    Esta función genera una lista con listas anidadas  según el número de
    filas, con el objetivo de simular un tablero.
    Argumentos:
    <num_filas> número de filas que se requiera
    <num_columnas> número de columnas que se requiera.
    return tablero
    """
    tablero=[]
    for i in range(num_filas):
        fila=[]
        tablero.append(fila)
        for j in range(num_columnas):
            fila.append("•")
    return tablero

def mostrar_tablero(tablero):
    """
    Esta función imprime el una lista de manera más ordenada, simulando un tablero.
    Argumentos:
    <tablero> una lista que contiene listas y simula un tablero.
    """
    for num in range(len(tablero[0])):
        print(num, end='  ')
    for i in tablero:
        print("")
        for casilla in i:
            print(casilla, end="  ")
    print("")

def introducir_fichas(tablero,columna,color):
    """
    La función inserta la variable color en la columna que desea el jugador. Recibe tres argumentos, y retorna un
    tablero si la inserción es extosa o None si no lo fue.
    Argumentos: 
    <tablero> una lista que contiene listas y simula un tablero.
    <columna> un dato del tipo int que indica donde el jugador desea poner su variable.
    <color> la variable que será insertada, puede ser X o Y.
    return tablero o None
    """
    if columna>=len(tablero[0]):
        print("¡Error! La columna esta fuera del rango del tablero.")
        return
    elif tablero[0][columna] != "•":
        print(f"¡Error! La columna {columna} esta llena.")
        return
    else:
        for i in range(len(tablero)-1,-1,-1):
            if tablero[i][columna]=="•":
                tablero[i][columna]=color
                return tablero

def revisar_filas(tablero,color):
    """
    Esta función revisa si algún caracter que simula un color se repite cuatro veces seguidas. Si es así, retorna
    un True, y si no, retorna un False.
    Recibe como argumento un tablero donde se encuentran los caracteres a revisar, y el color que sera evaluado.
    Argumentos:
    <tablero> El conjunto de caracteres donde va a iterar y revisar si hay 4 caracteres consecutivos.
    <color> El caracter que va a revisar para retornar True si se encuentran 4 caraceteres seguidos.
    return True || False
    """
    contador=0 
    for i in tablero:
        contador=0
        for j in i:
            if contador==4:
                return True
            else:
                if j==color:
                    contador+=1
                else:
                    contador=0
    return False

def revisar_columnas(tablero,color):
    """
    Esta función verifica si se forma un patrón de cuatro caracteres iguales seguidos por columna para retornar
    un True o False
    si no se cumple.
    Argumentos:
    <tablero> El conjunto de caracteres donde va a iterar y revisar si hay 4 caracteres consecutivos.
    <color> El caracter que va a revisar para retornar True si se encuentran 4 caraceteres seguidos.
    return True || False
    """
    contador=0
    for i in range(len(tablero[0])):
        contador=0
        for j in tablero:
            if contador==4:
                return True
            else:
                if j[i]==color:
                    contador+=1
                else:
                    contador=0
    return False

def revisar_diagonal_derecha(tablero, color):
    """
    Esta función revisa si existe una secuencia de 4 caracteres consecutivas en las diagonales derechas
    del tablero, retornando un True si se cumple, o False si no.
    Argumentos:
    <tablero> El conjunto de caracteres donde va a iterar y revisar si hay 4 caracteres consecutivos.
    <color> El caracter que va a revisar para retornar True si se encuentran 4 caraceteres seguidos.
    return True || False
    """
    for i in range(len(tablero)-3):
        for j in range(len(tablero[0])-3):
            contador=0
            for escalera in range(4):
                if tablero[i+escalera][j+escalera]==color:
                    contador+=1
                else:
                    break
            if contador==4:
                return True
    return False

def revisar_diagonal_izquierda(tablero, color):
    """
    Esta función revisa si existe una secuencia de 4 caracteres consecutivas en las diagonales izquierdas
    del tablero, retornando un True si se cumple, o False si no.
    Argumentos:
    <tablero> El conjunto de caracteres donde va a iterar y revisar si hay 4 caracteres consecutivos.
    <color> El caracter que va a revisar para retornar True si se encuentran 4 caraceteres seguidos.
    return True || False
    """
    for i in range(len(tablero)-3):
        for j in range(3, len(tablero[0])):
            contador=0
            for escalera in range(4):
                if tablero[i+escalera][j-escalera]==color:
                    contador+=1
                else:
                    break
            if contador==4:
                return True
    return False


def revisar_ganador(tablero,color):
    """
    Esta función revisa si hay algún retorno de True si se cumple una condición. Esta función llama a otras
    funciones que revisan por fila, columna, diagonal izquierda y derecha.
    <tablero> El conjunto de caracteres dondese revisara sisecumplala condición por cada funcion.
    <color> El caracter que va a revisar para retornar True si se encuentran 4 caraceteres seguidos.
    return True || False
    """
    if revisar_filas(tablero,color)==True:
        return True
    elif revisar_columnas(tablero,color)==True:
        return True
    elif revisar_diagonal_derecha(tablero,color)==True:
        return True
    elif  revisar_diagonal_izquierda(tablero,color)==True:
        return True
    else:
        return False

#Implentación del juego
        
def juego_cuatro_en_raya():
    """
    Esta función simula el juego cuatro en raya, donde el objetivo es juntar 4 posiciones seguidas de una
    ficha color en fila, columna o diagonalmente para ganar. La función esta compuesta de otras funciones
    que internamente hacen posible que el juego funcione.
    Esta función no necesita argumentos para trabajar, y retorna al jugador ganador cuando
    se cumple un cuatro en raya, o un empate si los espacios han sido llenado completamente.
    """
    print("¡Cuatro en raya!")
    columna=int(input("¿Cuántas columnas tendrá el tablero? "))
    fila=int(input("¿Cuántas filas tendrá el tablero? "))
    limite=fila*columna
    tabla=crear_tablero(fila,columna)
    turno=input("Elige X o Y como tu ficha para jugar. ")
    if turno not in ["X", "Y"]:
        print("Ficha inválida. Se asignará X por defecto.")
        turno = "X"
    contador_de_intentos=0
    while contador_de_intentos != limite:
        mostrar_tablero(tabla)
        print(f"Es el turno de {turno}. ")
        col=int(input("¿En que columna deseas poner la ficha: "))
        resultado=introducir_fichas(tabla,col,turno)
        if resultado is None:
            continue
        else:
            tabla=resultado
            limpiar_pantalla()
            contador_de_intentos+=1
            condicion=revisar_ganador(tabla,turno)
            if condicion==True:
                print(f"¡El juego ha terminado! ¡El ganador fue el participante del turno {turno}.!")
                mostrar_tablero(tabla)
                break
            if contador_de_intentos==limite:
                print("El número de intentos ha llegado a su límte. ¡Ha  sido un empate.!")
                mostrar_tablero(tabla)
            else:
                if turno == "X":
                    turno = "Y"
                else:
                    turno = "X"
    
























