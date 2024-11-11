from inputs import *
from auxiliares import *


def sumar_votos_por_lista(matriz_votos:list, lista:int)->int:
    """
    Recibe una matriz de votos y un número de lista.
    Retorna la suma de los votos de la lista especificada.
    
    Args:
        matriz_votos (list): La matriz de votos.
        lista (int): El número de la lista.
        
    Returns:
        votos_por_lista (int): La suma de los votos de la lista.
    """
    
    votos_por_lista = 0
    for turno in range(1, len(matriz_votos[lista])):  #recorro la cantidad de turnos
        votos_por_lista += matriz_votos[lista][turno] #sumo los votos de cada turno
    return votos_por_lista
    
    
def sumar_total_votos(matriz_votos:list)->int:
    """
    Recibe una matriz de votos y retorna la suma total de los votos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        total_votos (int): La suma total de los votos.
    """
    
    total_votos = 0
    
    for lista in range (len(matriz_votos)):                             #recorro la cantidad de listas
            total_votos += sumar_votos_por_lista(matriz_votos, lista)   #sumo los votos de cada lista
    return total_votos    


def calcular_porcentaje_votos_por_lista(matriz_votos:list, lista:int)->int:
    """
    Recibe una matriz de votos y un número de lista.
    Calcula el porcentaje de votos de la lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        lista (int): El número de la lista.
        
    Returns:
        porcentaje_votos_lista (int): El porcentaje de votos de la lista.
    """

    votos_por_lista = 0                                             #inicializo las variables
    total_votos = 0
    porcentaje_votos_lista = 0
    
    votos_por_lista = sumar_votos_por_lista(matriz_votos, lista)    #sumo los votos de la lista
    total_votos = sumar_total_votos(matriz_votos)                   #sumo los votos totales
    
    porcentaje_votos_lista = votos_por_lista / total_votos * 100    #calculo el porcentaje
    
    return porcentaje_votos_lista


def sumar_votos_por_turno(matriz_votos:list, turno:int)->int:
    """
    Recibe una matriz de votos y un número de turno.
    Retorna la suma de los votos del turno especificado.
    
    Args:
        matriz_votos (list): La matriz de votos.
        turno (int): El número de turno.
        
    Returns:
        votos_por_turno (int): La suma de los votos del turno.
    """
    
    votos_por_turno = 0
    for lista in matriz_votos:              #recorro la cantidad de listas  
        votos_por_turno += lista[turno]     #sumo los votos de cada turno
    return votos_por_turno

def ordenar_resultados(matriz_votos:list)->list:
    """
    Recibe una matriz de votos y retorna la matriz ordenada
    de mayor a menor, según la cantidad de votos por lista.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        matriz_votos (list): La matriz de votos ordenada.
    """
    
    for lista in range(len(matriz_votos)):                      #recorro la cantidad de listas
        for turno in range(lista + 1, len(matriz_votos)):       #recorro la cantidad de turnos
            if sumar_votos_por_lista(matriz_votos, lista) < sumar_votos_por_lista(matriz_votos, turno): #comparo las cantidades de votos
                aux = matriz_votos[lista]                       #intercambio las listas
                matriz_votos[lista] = matriz_votos[turno]       
                matriz_votos[turno] = aux                       
    return matriz_votos
