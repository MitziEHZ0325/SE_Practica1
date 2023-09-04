#Doramitzi Esmeralda Herrera Zepeda
#20310343

def prim(w, n, s):
    v = [0] * (n + 1)
    v[s] = 1
    E = set()
    suma_pesos = 0
    for i in range(n - 1):
        
        m = float('inf')
        agregar_vértice = None
        
        for j in range(1, n + 1):
            if v[j] == 1:
                for k in range(1, n + 1):
                    if v[k] == 0 and w[j][k] < m:
                        agregar_vértice = k
                        e = (j, k)
                        m = w[j][k]
        
        v[agregar_vértice] = 1
        E.add(e)
        suma_pesos += m
    
    return E, suma_pesos

w = [[float('inf')] * 7 for _ in range(7)]

w[1][2] = 4
w[2][1] = 4
w[1][3] = 2
w[3][1] = 2
w[1][5] = 3
w[5][1] = 3
w[2][4] = 5
w[4][2] = 5
w[3][4] = 1
w[4][3] = 1
w[3][5] = 6
w[5][3] = 6
w[3][6] = 3
w[6][3] = 3
w[4][6] = 6
w[6][4] = 6
w[5][6] = 2
w[6][5] = 2

s = int(input("Seleccione el vértice inicial: "))

aem, suma_pesos = prim(w, 6, s)

print("Aristas del árbol de expansión mínima:")
for e in aem:
    print(e)