'''
Se cuenta con un archivo csv, con la información de los voluntarios que se inscribieron para el evento que tiene la siguiente estructura por linea:
        1234,Juan,921,5.4 -> id_voluntario, nombre, codigo_playa, peso_recolectado.
La url del archivo csv es la siguiente:
    https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv
Requerimiento:
    Se necesita leer el archivo csv, y obtener la siguiente información:
        Opción 1: cuántos voluntarios se registraron en cada playa.
        Opción 2: total de residuos recolectados en cada playa.
        Opción 3: el máximo valor recolectado en una playa.
        Opción 4: total recolectado en el evento.
        Opción 5: total de voluntarios enlistados.

Escriba una función que reciba como parámetros la url del archivo y el código de la opción. 
A partir de estos datos, construya un datframe y obtenga la información según la opción escogida
Entradas
    Nombre          Tipo    Descripción
    ruta_archivo    Str     https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv
    codigo          Int     Entero del 1 al 5, define las opciones
Salidas
    Tipo    Descripción
    Dict    • Opción 1: {codigo_playa:cantidad_voluntarios, …}      int  : int
            • Opción 2: {codigo_playa:total_recolectado, …}         int  : float
            • Opción 3: Diccionario con un solo par llave valor:
                        {'Máximo recolectado en una playa': xxxx}   float
            • Opción 4. Diccionario con un solo par llave valor:
                        {'Total recolectado': xxxx}                 float
            • Opción 5: Diccionario con un solo par llave valor:
                        {'Total voluntarios': xxxx}                 int

def funcion1(ruta_archivo:str, opcion:int)->dict:
    pass
Casos públicos:
    Entradas                        Salida
    funcion1(ruta archivo csv, 1)   {138: 12, 432: 12, 921: 11}
    funcion1(ruta archivo csv, 2)   {138: 93.173858975, 432: 74.74362202500001, 921: 90.83004181000001}
    funcion1(ruta archivo csv, 3)   {'Máximo recolectado en una playa': 11.63081858}
'''
import pandas as pd
global datos

def voluntarios_playa():
    total = datos.groupby(['codigo_playa'])['id_voluntario'].count()
    return total.to_dict()

def residuos_playa():
    total = datos.groupby(['codigo_playa'])['peso_recolectado'].sum()
    return total.to_dict()

def max_residuos_playa():
    return {'Máximo recolectado en una playa': datos['peso_recolectado'].max()}

def total_residuos():
    return {'Total recolectado': datos['peso_recolectado'].sum()}
    
def total_voluntarios():
    return {'Total voluntarios': datos['id_voluntario'].count()}
    
def default():
    return "Opción Incorrecta"
 
def funcion1(ruta_archivo:str, opcion:int)->dict:
    global datos
    case = {
        1 : voluntarios_playa,
        2 : residuos_playa,
        3 : max_residuos_playa,
        4 : total_residuos,
        5 : total_voluntarios
    }
    
    datos = pd.read_csv(ruta_archivo,names=['id_voluntario','nombre','codigo_playa','peso_recolectado'])
    return case.get(opcion, default)()

print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',1))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',2))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',3))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',4))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',5))