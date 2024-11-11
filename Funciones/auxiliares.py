from validaciones import *
from inputs import *
from calculos import *
from textwrap import dedent
import os

def inicializar_matriz(cantidad_fil:int, cantidad_col:int)->list:
    """
    Recibe una cantidad de filas y columnas y retorna una
    matriz de ceros.
    
    Args: 
        cantidad_fil (int): La cantidad de filas de la matriz.
        cantidad_col (int): La cantidad de columnas de la matriz.
        
    Returns:
        matriz (list): La matriz inicializada.
    """
    
    matriz = []
    
    for i in range(cantidad_fil):  #recorro la cantidad de filas
        fila = [0] * cantidad_col  #creo una fila con la cantidad de columnas
        matriz += [fila]           #agrego la fila a la matriz
    return matriz


def encontrar_turno_con_mas_votos(matriz_votos:list)->int:
    """
    Recibe una matriz de votos.
    Retorna el turno con mayor cantidad de votos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        turno_con_mas_votos (int): El turno con mayor cantidad de votos.
    """
    
    votos_mañana = sumar_votos_por_turno(matriz_votos, 1)           #sumo los votos de cada turno
    votos_tarde = sumar_votos_por_turno(matriz_votos, 2)
    votos_noche = sumar_votos_por_turno(matriz_votos, 3)
    turno_con_mas_votos = None
    
    if votos_mañana > votos_tarde and votos_mañana > votos_noche:   #busco el turno con mas votos
        turno_con_mas_votos = 1
    elif votos_tarde > votos_mañana and votos_tarde > votos_noche:
        turno_con_mas_votos = 2
    elif votos_noche > votos_mañana and votos_noche > votos_tarde:
        turno_con_mas_votos = 3
    else:
        return 0
    return turno_con_mas_votos


def verificar_empate_turnos(matriz_votos:list)->bool:
    """
    Recibe una matriz de votos.
    Retorna True si hay empate entre dos turnos.
    
    Args:
        matriz_votos (list): La matriz de votos.
        
    Returns:
        bandera_empate (bool): True si hay empate entre dos turnos.
    """
    
    bandera_empate = False
    turno_con_mas_votos = encontrar_turno_con_mas_votos(matriz_votos)   #busco el turno con mas votos
    if turno_con_mas_votos == 0:                                     #si no hay turno con mas votos, hay empate
        bandera_empate = True
        return bandera_empate


def mostrar_empate_turnos(matriz_votos:list)->None:
    """
    Recibe una matriz de votos e imprime los turnos empatados.
    
    Args:
        matriz_votos (list): La matriz de votos.
    Returns:
        None
    """
    
    if verificar_empate_turnos(matriz_votos) == True:                  #si hay empate
        votos_mañana = sumar_votos_por_turno(matriz_votos, 1)   #sumo los votos de cada turno
        votos_tarde = sumar_votos_por_turno(matriz_votos, 2)
        votos_noche = sumar_votos_por_turno(matriz_votos, 3)
                                                                #imprimo los turnos empatados
        print(dedent(f"""                                       
        {'-'* 40}
        Hay un empate en el turno con más votos.
        Votos por turno:
        Turno mañana: {votos_mañana}
        Turno tarde: {votos_tarde}
        Turno noche: {votos_noche} 
        {'-'* 40}
        """))
        
        return None


def cargar_ballotage(primer_candidato:str, segundo_candidato:str,
                     votos_primer_candidato:int, votos_segundo_candidato:int)->list:
    """
    Recibe las dos listas que participan en el ballotage y sus respectivos votos 
    y retorna una matriz con estos datos.
    
    Args:
        primer_candidato (str): Numero de lista del primer candidato.
        segundo_candidato (str): Numero de lista del segundo candidato.
        votos_primer_candidato (int): La cantidad de votos del primer candidato.
        votos_segundo_candidato (int): La cantidad de votos del segundo candidato.
        
    Returns:
        matriz_ballotage (list): La matriz con los datos del ballotage.
    """
    
    matriz_ballotage = [[primer_candidato, votos_primer_candidato],     #declaro la matriz
                        [segundo_candidato, votos_segundo_candidato]]
    
    return matriz_ballotage


def mostrar_ganador(lista:int, votos:int, porcentaje_de_votos:float)->None:
    """
    Recibe la lista ganadora, la cantidad de votos y el porcentaje de votos.
    Imprime los datos del ganador.
    
    Args:
        lista (int): La lista ganadora.
        votos (int): La cantidad de votos.
        porcentaje_de_votos (float): El porcentaje de votos.
        
    Returns:
        None
    """
    #imprimo los datos del ganador
    print(dedent(f"""      
    El ganador es la lista {lista} 
    con {votos} votos 
    y un porcentaje de {porcentaje_de_votos:.2f}%
    """))
    return None
    
    
def mostrar_empate_ballotage(matriz_ballotage:list)->None:
    """
    Recibe una matriz de ballotage e imprime que hubo empate.
    
    Args:
        matriz_ballotage (list): La matriz de ballotage.
        
    Returns:
        None
    """
    
    votos_primer_candidato = matriz_ballotage[0][1]
    votos_segundo_candidato = matriz_ballotage[1][1]
    if  votos_primer_candidato == votos_segundo_candidato: 
        #si hay empate
        votos_empate = matriz_ballotage[0][1]
        print(dedent(f"""                                       
        {'-'* 40}
        Hay un empate en la segunda vuelta con {votos_empate}.
        {'-'* 40}
        """))
        
        return None
    
    
def limpiar_consola()->None:
    """
    Limpia la consola una vez que se sale del sistema.
    
    Args:
        None
        
    Returns:
        None
    """
    
    print("Saliendo...")
    os.system('cls')
    return None


def salir_del_sistema()->None:
    """
    Pregunta al usuario si desea salir del sistema, en caso afirmativo limpia la consola,
    caso contrario no hace nada.
    
    Args:
        None
        
    Returns:
        None
    """
    salida = input("Esta seguro que desea salir del sistema? (s / n): ")        #pregunto al usuario si desea salir
    
    while validar_si_no(salida) == False: #valido la respuesta
        salida = input("Esta seguro que desea salir del sistema? (s / n): ") 
    if salida == "s": #si la respuesta es afirmativa, limpio la consola
        limpiar_consola()
        print("✦ GRACIAS POR USAR NUESTRO SISTEMA ✦")
        print(f"{'-'* 50} ")
        print(" ")
    else: #si la respuesta es negativa, no hago nada
        return None
    
    
def mostrar_menu()->None:
    """
    Muestra en pantalla el menu de opciones.
    
    Args:
        None
        
    Returns:
        None
    """
    #imprimo el menu
    print(dedent(
    """
    1. Cargar votos
    2. Mostrar resultados
    3. Ordenar votos por turno
    4. Mostrar las listas menos votadas
    5. Mostrar el turno con más votos
    6. Verificar si hay Ballotage
    7. Realizar segunda vuelta
    8. Salir

    """))
    return None
          


