import numpy as np

cuadricula = np.zeros((4,4), np.uint8)

#print(cuadricula)


def setReina(columna, fila):
    
    Reina = 0

    for x in cuadricula[:,columna]:
        
        if(x == 1):
            
            Reina = 1
            
    for y in cuadricula[fila,:]:
        
        if(y == 1):
            
            Reina = 1
            
                
    if(Reina == 1):
        
        return False
    
    else:
        
        cuadricula[fila,columna] = 1
        return True

def cuatro_reinas():
    
    col = 0
    fil = -1
    
    while(col >= 0):
        
        fil = fil + 1
        #se busca un movimiento legal en la columna "col" #Metodo setReina retorna False si no se pudo agregar la reina 
        
        while(fil < 4 and  setReina(col,fil) == False ):
            
            #se intenta en el siguiente reglon
            fil = fil + 1
            
        if(fil < 4):
            
            if(col == 3):
                
                return True
            
            else:#siguiente columna
            
                col = col + 1
                fil = 0
                
        else:#regresar a columna anterior
        
            col = col - 1
            
    return False        

            
solucion = cuatro_reinas()

if(solucion == True):
    
    print("La cuadricula resultante es:\n", cuadricula)
    
else:
    
    print("no existe solucion")