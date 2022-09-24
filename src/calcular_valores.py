import numpy as np
import argparse 

def calcular_suma(lista_numeros, verbose=1):
    """Calcula la suma de una lista de numeros
    
    Arg:
        lista_numeros(lista): lista de numeros con valores enteros
        
    Return:
        int """
        
    resultado_suma = np.sum(lista_numeros)
    
    if verbose == 1:
        print('calcular_suma')
        print('suma: ', resultado_suma)
    else:
        pass 
    
    return resultado_suma

def calcular_valores_centrales(lista_numeros, verbose=1):
    """Calcula el valor de la media y la desviacion estandar de una lista de numeros
    
    Arg:
        lista_numeros(lista): lista de numeros con valores enteros
        
    Returns:
        tuple: (media, desviacion estandar)"""
        
    resultado_media   = np.mean(lista_numeros)
    resultado_dev_std = np.std(lista_numeros)
    
    if verbose == 1:
        print('calcular_valores_centrales')
        print('media: ', resultado_media)
        print('desviación estandar: ', resultado_dev_std)
    else:
        pass
    
    return resultado_media, resultado_dev_std

def calcular_extremos(lista_numeros, verbose=1):
    """Calcula el valor minimo y maximo de una lista de numeros
    
    Arg:
        lista_numeros (lista): lista de numeros con valores enteros
        
    Returns:
        tuple: (minimo, maximo)
    
    """

    resultado_min = np.min(lista_numeros)
    resultado_max = np.max(lista_numeros)
    
    if verbose == 1:
        print('calcular_extremos')
        print('minímo: ', resultado_min)
        print('máximo: ', resultado_max)
    else:
        pass
    
    return resultado_min, resultado_max
 
def calcular_valores(lista_numeros, verbose):
    suma             = calcular_suma(lista_numeros, verbose)
    media, dev_std   = calcular_valores_centrales(lista_numeros, verbose)
    min_val, max_val = calcular_extremos(lista_numeros, verbose)
    return suma, media, dev_std, min_val, max_val

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', type=int, default=1, help='para decidir si imprime informe')
    args = parser.parse_args()
    verbose = args.verbose 


    lista_numeros = [1,5, 8, 3, 45, 93]
    suma, media, dev_std, min_val, max_val = calcular_valores(lista_numeros, 1)
    
    print('DONE!!!')
    
if __name__  == '__main__':
    main()