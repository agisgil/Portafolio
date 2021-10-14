def estado_nivel(datos_tanque: dict)->str:
    dicSalida = dict(codigoTanque = datos_tanque['codigo'], nivel = "revisar sensores")
    if not datos_tanque['sensor1']:
        if not datos_tanque['sensor2'] and not datos_tanque['sensor3']:
            dicSalida['nivel'] = "vacio"
    else:
        if datos_tanque['sensor2']:
            if datos_tanque['sensor3']:
                dicSalida['nivel'] = "nivel alto"
            else:
                dicSalida['nivel'] = "nivel medio"
        else:
            if not datos_tanque['sensor3']:
                dicSalida['nivel'] = "nivel bajo"
        
    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"

'''print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = True)))'''

print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = False)))



'''
def estado_nivel1(datos_tanque: dict)->dict:
    dicSalida = dict(codigoTanque = datos_tanque['codigo'], nivel = "revisar sensores")
    if not datos_tanque['sensor1'] and not datos_tanque['sensor2'] and not datos_tanque['sensor3']:
            dicSalida['nivel'] = "vacio"
    else:
        if datos_tanque['sensor1'] and datos_tanque['sensor2'] and datos_tanque['sensor3']:
                dicSalida['nivel'] = "nivel alto"
        else:
            if datos_tanque['sensor1'] and datos_tanque['sensor2'] and not datos_tanque['sensor3']:
                dicSalida['nivel'] = "nivel medio"
            else:
                if datos_tanque['sensor1'] and not datos_tanque['sensor2'] and not datos_tanque['sensor3']:
                    dicSalida['nivel'] = "nivel bajo"
        
    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"
'''
