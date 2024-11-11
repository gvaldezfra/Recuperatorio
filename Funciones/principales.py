from auxiliares import *
from validaciones import *
from inputs import *
from calculos import *
from textwrap import dedent
import random

def cargar_votos()->list:
    """
    Carga los datos de los votos en una matriz.
    Retorna una matriz de votos.
    
    Args:
        None
        
    Returns:
        matriz_votos (list): La matriz de votos.
    """
    matriz_votos = inicializar_matriz(pedir_cantidad_listas(),4)       #inicializo la matriz con la cantidad de listas que pedi           
    
    for lista in range(len(matriz_votos)):                             #recorro la cantidad de listas
        matriz_votos[lista][0] = pedir_lista()                         #pido nombre de lista y lo guardo en la matriz
        for turno in range(1, len(matriz_votos[lista])):               #recorro la cantidad de turnos
            matriz_votos[lista][turno] = pedir_votos_por_turno(turno)  #guardo los votos de cada turno
    
    return matriz_votos

def mostrar_resultados(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e imprime los datos de cada lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        None
    """
      
    for lista in range(len(matriz_votos)):                      #recorro las listas
        porcentaje_lista = calcular_porcentaje_votos_por_lista(matriz_votos, lista) #calcilo el porcentaje de cada lista    
        print(f'LISTA NRO: {matriz_votos[lista][0]}')           #imprimo nro de lista
        for turno in range(1, len(matriz_votos[lista])):        #recorro los turnos
            print(f"VOTOS TURNO {mostrar_turno(turno).upper()}: {matriz_votos[lista][turno]} votos") #imprimo los votos por turno
        print(f"PORCENTAJE DE VOTOS: {porcentaje_lista:.2f}%")  #imprimo el porcentaje de votos de la lista
        print(f"{'-'* 40} ") 
    return None

def ordenar_votos_por_turno(matriz_votos:list)->list:
    """
    Ordena de mayor a menor la matriz de votos por el turno elegido.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        matriz_votos (list): La matriz de votos ordenada.
    """
    
    print("¿Qué turno desea ordenar? \n")                       #Pregunto que turno ordenar 
    turno = pedir_turno()                                       #guardo el turno en una variable   
    for i in range(len(matriz_votos)):                          #recorro la cantidad de listas  
        for j in range(i+1, len(matriz_votos)):                 #recorro la cantidad de turnos
            if matriz_votos[i][turno] < matriz_votos[j][turno]: #comparo los turnos,si el elemento siguiente es mayor, los intercambio
                aux = matriz_votos[i]                           #primero guardo el primer elemento en una variable aux
                matriz_votos[i] = matriz_votos[j]               #luego guardo el segundo en el primero
                matriz_votos[j] = aux                           #luego guardo el primero en el segundo
    return matriz_votos

def mostrar_listas_menos_votadas(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e 
    imprime las listas con menos del 5% de los votos.
    
    """
    print("Listas con menor porcentaje de votos (<5%): \n")
    listas_encontradas = False                      # Creo una bandera de listas encontradas
    for lista in range(len(matriz_votos)):          #Recorro listas
        porcentaje_votos_lista = calcular_porcentaje_votos_por_lista(matriz_votos, lista)  #Calculo el porcentaje de lista
        if porcentaje_votos_lista < 5:       #Si el porcentaje es menor a 5, la bandera se vuelve verdadera
            listas_encontradas = True        #Luego imprimo las listas con menos del 5%
            print(dedent(f"""
            NRO LISTA: {matriz_votos[lista][0]}
            PORCENTAJE DE VOTOS: {porcentaje_votos_lista:.2f}%
            {'-'* 40}
                  """))
    if listas_encontradas == False:  #Si no se encuentran listas con menos del 5%,la bandera sigue en False e imprimo que no se encontraron.
        print("No se encontraron listas con menos del 5% de los votos.")
    return None

def mostrar_turno_con_mas_votos(matriz_votos:list)->None:
    """
    Imprime el turno con mas votos, en caso de empate,
    imprime los resultados de los turnos empatados.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        None
    """
    empate = verificar_empate_turnos(matriz_votos) #Verifico empate, guardo el bool en una variable
    if empate == True:  #Si empate es verdadero, muestro los turnos empatados
        mostrar_empate_turnos(matriz_votos)
        return None
    else:
        turno_con_mas_votos = encontrar_turno_con_mas_votos(matriz_votos)  #Busco el nro de turno, lo guardo en una variable
        nombre_turno_mas_votos = mostrar_turno(turno_con_mas_votos)        #Lo mismo con el nombre
        votos_turno_con_mas_votos = sumar_votos_por_turno(matriz_votos, turno_con_mas_votos) #Sumo los votos del turno, los guardo
        #imprimo el turno con más votos
        print(dedent(f"""
        El turno con más votos es el turno {nombre_turno_mas_votos}, 
        con {votos_turno_con_mas_votos} votos."""))
        return None

def verificar_ballotage(matriz_votos:list)->bool:
    """
    Recibe una matriz de votos y verifica si se debe
    realizar una segunda vuelta.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        ballotage (bool): True si hay ballotage, False en caso contrario
    """
    
    ballotage = False    #Por defecto no hay ballotage
    for lista in range(len(matriz_votos)):    #Recorro listas
        if calcular_porcentaje_votos_por_lista(matriz_votos, lista) < 50: 
            ballotage = True #Si el porcentaje de votos es menor a 50, la bandera se vuelve verdadera
        else:
            ballotage = False #Caso contrario sigue en False
    if  ballotage == True: 
        print("Hay ballotage.") #La bandera es verdadera, informo que hay ballotage
        return ballotage
    elif ballotage == False: #La bandera es falsa, informo que no hay ballotage
        print("No hay ballotage.")
        return ballotage

def realizar_segunda_vuelta(matriz_votos:list, ballotage:bool)->None:
    """
    Realiza la segunda vuelta electoral con los dos candidatos más votados.
    
    Si hay ballotage, se ordenan los resultados y se realizan los cálculos
    para determinar el ganador de la segunda vuelta.
    
    Si no hay ballotage, se muestra un mensaje y se finaliza.
    
    Parámetros:
        matriz_votos (list): Matriz de votos con los resultados de la primera vuelta.
        ballotage (bool): Indica si hay ballotage o no.
    
    Retorna:
        None
    """
    if ballotage == True: #Recibo la bandera de ballotage, si es verdadera realizo la segunda vuelta
        
        print("Realizando segunda vuelta...")
        ordenar_resultados(matriz_votos)                    #Ordeno los resultados de la matriz de votos

        primer_candidato = matriz_votos[0][0]               #Declaro las variables de candidatos (nro de sus listas)
        segundo_candidato = matriz_votos[1][0]
        
        total_votos_segunda_vuelta = pedir_votos_segunda_vuelta() #Pido la cantidad de votos de la segunda vuelta
        
        votos_primer_candidato = random.randint(0, total_votos_segunda_vuelta) #Genero los votos aleatorios
        votos_segundo_candidato = total_votos_segunda_vuelta - votos_primer_candidato
       
       #Guardo los datos del ballotage en una matriz  
        matriz_ballotage = cargar_ballotage(primer_candidato, segundo_candidato, 
                                            votos_primer_candidato, votos_segundo_candidato) 
        
        #Calculo el porcentaje de votos de cada candidato
        porcentaje_primer_candidato = calcular_porcentaje_votos_por_lista(matriz_ballotage, 0)
        porcentaje_segundo_candidato = calcular_porcentaje_votos_por_lista(matriz_ballotage, 1)
        
        
        #Busco al ganador del ballotage y lo muestro
        if porcentaje_primer_candidato > porcentaje_segundo_candidato:
            mostrar_ganador(primer_candidato, votos_primer_candidato, porcentaje_primer_candidato)    
        elif porcentaje_segundo_candidato > porcentaje_primer_candidato:
            mostrar_ganador(segundo_candidato, votos_segundo_candidato, porcentaje_segundo_candidato)
        else:
            mostrar_empate_ballotage(matriz_ballotage)
        return None


