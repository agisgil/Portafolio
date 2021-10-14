def calcular_seguro(nombre: str, apellido: str, val_asegurado: int, descuento: int, )->str:
    '''
    Calcular seguro
    Parámetros:
    nombre(str), nombre del tomador del seguro
    apellido(str), apellido del tomador del seguro
    val_asegurado(int), valor asegurado
    descuento(int), valor descuento promocional del mes
    Retorno:
    String: de la forma "El valor del seguro de {nombre} {apellido}
    es: {valor_total}, el descuento realizado fue:
    {valor_descuento}", dónde, el valor_total debe ser calculado
    de acuerdo con el valor asegurado y restarle la promoción del mes, y 
    valor_descuento, es el descuento aplicado por promoción.
    '''

    valor_descuento = (val_asegurado * 15 / 100) * descuento / 100
    valor_total =  (val_asegurado * 15 / 100) - valor_descuento
    return f'El valor del seguro de {nombre} {apellido} es: {valor_total}, el descuento realizado fue: {valor_descuento}'

print(calcular_seguro('Pedro', 'Diaz', 10000000,5))

def even_bigger(x):
    return (2 * x) ** x

print(even_bigger(12))