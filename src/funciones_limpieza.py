import pandas as pd
import numpy as np
import os  
from pathlib import Path
import argparse

root_dir = Path('.').resolve()

def get_data(filename):
    """Carga datos desde la carpeta raw
    
    Arg:
        filename: nombre del archivo guardado en la carpeta raw
        
    Return:
        datos --> pd.dataframe """
        
    data_dir = 'raw'
    file_path = os.path.join(root_dir, 'data', data_dir, filename)
    
    datos = pd.read_csv(file_path, sep=';', encoding='latin-1')
    print('get_data')
    print('La tabla contiene: ', datos.shape[0], 'filas', datos.shape[1], 'columnas')
    print(datos)
    return datos

def remover_duplicados_y_nulos(datos):
    """Remueve datos duplicados y datos nulos de la columna UNIDAD
        
    Arg:
        datos --> pd.dataframe
        
    Return:
        datos --> pd.dataframe """
        
    print('remover_duplicados_y_nulos')
    datos = datos.drop_duplicates()
    datos.reset_index(inplace = True, drop = True)
    
    datos['UNIDAD'] = datos['UNIDAD'].fillna('SIN_DATO')
    datos['UNIDAD'].value_counts(dropna = False, normalize = True)
    print(datos)
    return datos
    
def convertir_str_a_num(datos):
    """Convierte los datos tipo str de la columna EDAD a datos numericos tipo float
    
    Arg:
        datos --> pd.dataframe
        
    Return:
        datos --> pd.dataframe """
        
    print('convertir_str_a_num')
    datos['EDAD'] = datos['EDAD'].replace({'SIN_DATO' : np.nan})
    datos['EDAD'] = datos['EDAD'].astype('float')
    print(datos)
    print(datos.dtypes)
    return datos

def corregir_fechas(datos):
    """Corrige el tipo de dato de las fechas del dataframe a tipo pd.datetime
    
    Arg:
        datos --> pd.dataframe
        
    Return:
        datos --> pd.dataframe """
        
    print('corregir_fechas')
    datos['FECHA_INICIO_DESPLAZAMIENTO_MOVIL'] = pd.to_datetime(datos['FECHA_INICIO_DESPLAZAMIENTO_MOVIL'], errors='coerce')
    datos['RECEPCION'] = pd.to_datetime(datos['RECEPCION'], errors='coerce')
    print(datos)
    print(datos.dtypes)
    return datos

def save_data(datos, filename):
    """Guarda los datos limpios en un nuevo archivo en la carpeta processed
    
    Arg:
        datos --> pd.dataframe
        filename: nombre del archivo
        
    Return:
        datos --> csv"""
    print('DATOS GUARDADOS')
    
    out_name = 'reporte_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    datos.to_csv(out_path)
    