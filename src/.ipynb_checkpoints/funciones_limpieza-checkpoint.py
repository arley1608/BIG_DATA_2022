import pandas as pd
import numpy as np
import os  
from pathlib import Path
import argparse
import logging 

bucket = "gs://arodriguez_llamadas_123/"

def get_data(filename):
    """Carga datos desde la carpeta raw
    
    Arg:
        filename: nombre del archivo guardado en la carpeta raw
        
    Return:
        datos --> pd.dataframe """
    
    logger = logging.getLogger('get_data')
    
    data_dir = 'raw'
    file_path = os.path.join(bucket, "data", data_dir, filename)

    #logger.info(f'Reading file: {file_path}')
    
    print('Leyendo los datos')
    logger.info(f'Leyendo datos: {file_path}')
    datos = pd.read_csv(file_path, encoding='latin-1', sep=';')
    
    logger.info(f'La tabla contiene {datos.shape[0]} filas y {datos.shape[1]} columnas')
    return datos

def agregar_tabla(datos, filename_2):
    
    print('agregar_tabla')

    bucket = "gs://arodriguez_llamadas_123/"
    file_path = os.path.join(bucket , 'data', 'raw', filename_2)
    file_path
    nueva_tabla = pd.read_csv(file_path, encoding='latin-1', sep=';')
    datos = datos.append(nueva_tabla)
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
    #print(datos)
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
    #print(datos)
    #print(datos.dtypes)
    return datos

def corregir_fechas(datos):
    """Corrige el tipo de dato de las fechas del dataframe a tipo pd.datetime
    
    Arg:
        datos --> pd.dataframe
        
    Return:
        datos --> pd.dataframe """
        
    print('corregir_fechas')
    datos['FECHA_INICIO_DESPLAZAMIENTO_MOVIL'] = pd.to_datetime(datos['FECHA_INICIO_DESPLAZAMIENTO_MOVIL'],errors='coerce')
    datos['RECEPCION'] = pd.to_datetime(datos['RECEPCION'], errors='coerce')
    #print(datos)
    print(datos.dtypes)
    return datos

def corregir_localidad(datos):
    
    print('corregir_localidad')
    datos.loc[datos['CODIGO_LOCALIDAD'] == 1.0, 'LOCALIDAD'] = 'Usaquen'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 2.0, 'LOCALIDAD'] = 'Chapinero'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 3.0, 'LOCALIDAD'] = 'Santa Fe'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 4.0, 'LOCALIDAD'] = 'San Cristobal'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 5.0, 'LOCALIDAD'] = 'Usme'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 6.0, 'LOCALIDAD'] = 'Tunjuelito'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 7.0, 'LOCALIDAD'] = 'Bosa'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 8.0, 'LOCALIDAD'] = 'Keneddy'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 9.0, 'LOCALIDAD'] = 'Fontibon'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 10.0, 'LOCALIDAD'] = 'Engativa'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 11.0, 'LOCALIDAD'] = 'Suba'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 12.0, 'LOCALIDAD'] = 'Barrios Unidos'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 13.0, 'LOCALIDAD'] = 'Teusaquillo'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 14.0, 'LOCALIDAD'] = 'Los Martires'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 15.0, 'LOCALIDAD'] = 'Antonio Nariño'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 16.0, 'LOCALIDAD'] = 'Puente Aranda'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 17.0, 'LOCALIDAD'] = 'Candelaria'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 18.0, 'LOCALIDAD'] = 'Rafael Uribe Uribe'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 19.0, 'LOCALIDAD'] = 'Ciudad Bolivar'
    datos.loc[datos['CODIGO_LOCALIDAD'] == 20.0, 'LOCALIDAD'] = 'Sumapaz'
    return datos

def save_data(datos, filename):
    """Guarda los datos limpios en un nuevo archivo en la carpeta processed
    
    Arg:
        datos --> pd.dataframe
        filename: nombre del archivo
        
    Return:
        datos --> csv"""
    print('DATOS GUARDADOS')
    
    out_name = 'resumen_llamadas_123.csv'
    out_path = os.path.join(bucket, 'data', 'processed', out_name)
    datos.to_csv(out_path, index = False)
    