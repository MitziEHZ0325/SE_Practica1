# -*- coding: utf-8 -*-
"""
Doramitzi Esmeralda Herrera Zepeda
20310343
"""
def conflicto(fila, k):
    for i in range(k-1):
        if (fila[i] == fila[k-1]) or \
           (fila[i] - fila[k-1] == i - (k-1)) or \
           (fila[i] - fila[k-1] == (k-1) - i):
            return True
    return False

def cuatro_reinas(fila, columna_inicial):
    k = 1
    fila[0] = columna_inicial
    while k > 0:
        fila[k-1] = fila[k-1] + 1
        while (fila[k-1] <= 4) and conflicto(fila, k):
            fila[k-1] = fila[k-1] + 1
        if fila[k-1] <= 4:
            if k == 4:
                return True
            else:
                k = k + 1
                fila[k-1] = 0
        else:
            k = k - 1
    return False

fila = [0, 0, 0, 0]
columna_inicial = 0
solucion = cuatro_reinas(fila, columna_inicial)
if solucion:
    print("Hay solución:")
    for i in range(4):
        print((i+1, fila[i]))
else:
    print("No hay solución.")

