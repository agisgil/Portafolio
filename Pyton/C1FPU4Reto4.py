orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
 [2,("5464",9,30000),("9744",9,150000)],
 [3,("5464",9,30000),("88112",11,45000)],
 [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]

orden1 = [[1,("5464",1,30000),("8274",2,42000),("9744",3,150000)],
        [2,("7733",3,80000),("88112",10,45000),("5464",2,30000),("9744",9,150000)],
        [3,("88112",25,45000)],
        [4,("5464",9,30000),("9744",20,150000)],
        [5,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]

''' Respuestas
[[1, 2226000], [2, 1620000], (3, 795000), [4, 1350000]]
[(1, 594000), [2, 2100000], [3, 1125000], [4, 3270000], [5, 1350000]]
'''

def facturarTotal(orden:list)->list:
    from functools import reduce
    ''' 
    num_pedido = [ped[0] for ped in orden]
    vlr_art = map(lambda ord: map(lambda n: n[1]*n[2], ord[1:]), orden)
    vlr_pedido = list(map(lambda listaVlr: reduce(lambda vlr1, vlr2: vlr1 + vlr2, listaVlr), vlr_art))
    pedidos = list(zip(num_pedido, vlr_pedido))
    pedidos = list(map(lambda n: (n[0],n[1] + 30000) if n[1] < 1000000 else list(n), pedidos))
    return pedidos
    '''
    return list(map(lambda n: (n[0],n[1] + 30000) if n[1] < 1000000 else list(n),
                    list(zip([ped[0] for ped in orden], list(map(lambda listaVlr: reduce(lambda vlr1, vlr2: vlr1 + vlr2, listaVlr),
                                                                 map(lambda ord: map(lambda n: n[1]*n[2], ord[1:]), orden)))))))

print(facturarTotal(orden))
print(facturarTotal(orden1))

'''
---Version en una Sola Línea (poco nemotecnica pero genial)
pedidos = list(map(lambda n: (n[0],n[1] + 30000) if n[1] < 1000000 else list(n),
                   list(zip([ped[0] for ped in orden], list(map(lambda listaVlr: reduce(lambda vlr1, vlr2: vlr1 + vlr2, listaVlr),
                                                                map(lambda ord: map(lambda n: n[1]*n[2], ord[1:]), orden)))))))

---Versión con funciones avanzadas solicitadas solo no use el filter
num_pedido = [ped[0] for ped in orden]
vlr_art = list(list(map(lambda n: n[1]*n[2], ord[1:])) for ord in orden)
vlr_pedido = list(map(lambda listaVlr: reduce(lambda vlr1, vlr2: vlr1 + vlr2, listaVlr), vlr_art))
pedidos = list(zip(num_pedido, vlr_pedido))
pedidos = list(map(lambda n: (n[0],n[1] + 30000) if n[1] < 1000000 else list(n), pedidos))
print(pedidos)

---Version con algunas funciones avanzadas
for ord in orden:
    #print(ord[1:])
    total_art = list(map(lambda n: (n[1]*n[2]), ord[1:]))
    total_pedido = reduce(lambda total_pedido, n: total_pedido + (n[1]*n[2]), ord[1:], 0) 
    # total_pedido + 30000 if total_pedido < 1000000 for 
    #a if a < b else b
    if total_pedido < 1000000:
        total_pedido = total_pedido + 30000
        print(total_pedido)
        print((ord[0],total_pedido))
        pedidos.append((ord[0],total_pedido))
    else:
        print(total_pedido)
        print([ord[0],total_pedido])
        pedidos.append([ord[0],total_pedido])
print(pedidos)

--- Version sin uso de funciones avanzadas
pedidos = []
for pedido in orden:
    tot = 0
    for art in pedido[1:]:
        tot = tot + (art[1]*art[2])
    pedidos.append([pedido[0], tot] if tot >= 1000000 else (pedido[0], tot + 30000))
print(pedidos)

---Prueba de creacion de código
print(orden[0:])
print(orden[0][1:])
print(orden[0][1][1:])

articulos = orden[0][1:]
total_articulos = list(map(lambda n: n[1]*n[2], articulos))
total_pedidos = reduce(lambda a, b: a + b, total_articulos, 0)

list(map(lambda n: n[1]*n[2], articulos))
map(lambda total_pedido, n: total_pedido + (n[1]*n[2]) , orden)
reduce(lambda total_pedido, n: total_pedido + (n[1]*n[2]), orden[1:], 0)
'''
