'''
Lista con los datos de los sistemas de seguridad que tiene instalados en locaciones de la ciudad

Lista con los datos personales de los clientes
[{'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
{'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
{'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 3,'sensores': 5},
{'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
{'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
{'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1,'sensores': 8}]

Guardias asignados depende de la zona donde se encuentre la locación. zona 1 - 3 guardias, zonas 2 y 3 - 2 guardias

Función:
Recibe: una lista con el código del cliente y una tupla con el código binario 
indicando sensores activos e inactivos. Ejemplo [020008, (1,0,0,1,0)]
Retorna: una lista que contenga los clientes que tienen sensores activos. La lista de salida debe contener
diccionarios con los siguientes datos, código del cliente, dirección del cliente, cantidad guardias asignados,
cantidad de sensores activos, estado sensores en revisar.

Entradas                    Salidas
codigo  tupla               Return
020008  (1,0,1,0,0,0,0)     [{'codigo_cliente': '020008', 'direccion': 'cr 84 70 27 Bod 4', 'cantidad_guardias': '2 
                             guardias', 'sensores_activos': 2, 'estado_sensores': 'revisar'}]
020115  (0,0,0,0,0)         [{}]
020114  (0,0,1,0,0)         [{'codigo_cliente': '020114', 'direccion': 'cr 30 25 80', 'cantidad_guardias': '2 guardias',
                             'sensores_activos': 1, 'estado_sensores': 'correcto'}]

'''

datos_clientes = [
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
    {'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
    {'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 3,'sensores': 5},
    {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1,'sensores': 8}
]
    
def monitoreo(codigo:str,sensores:tuple)->list:
    if sensores.count(1) == 0:
        return [{}]
    for c in datos_clientes:
        if c['codigo'] == codigo:
            direccion = c['dir']
            if len(sensores) == c['sensores']:
                estado = 'correcto'
            else:
                estado = 'revisar'
            if c['zona'] == 1:
                guardias = "3 guardias"
            else:
                guardias = "2 guardias"
    return [{'codigo_cliente': codigo, 'direccion': direccion, 'cantidad_guardias': guardias,
                'sensores_activos': sensores.count(1), 'estado_sensores': estado}]

print(monitoreo('020008',(1,0,1,0,0,0,0)))
print(monitoreo('020115',(0,0,0,0,0)))
print(monitoreo('030011',(0,0,0,0,0)))
print(monitoreo('010010',(0,0,0,0,0)))