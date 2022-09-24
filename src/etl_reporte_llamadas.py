# presudo código
# main()
#   datos   = get_data(filename)
#   reporte = generate_report(datos)
#   save_data(reporte)

import pandas as pd
import os  
from pathlib import Path

root_dir = Path('.').resolve()

def get_data(filename):
    data_dir = 'raw'
    file_path = os.path.join(root_dir, 'data', data_dir, filename)
    
    datos = pd.read_csv(file_path, sep=';', encoding='latin-1')
    print('get_data')
    print('La tabla contiene: ', datos.shape[0], 'filas', datos.shape[1], 'columnas')
    return datos

def generate_report(datos):
    
    dict_reporte = dict()

    for col in datos.columns:
        valores_unicos = datos[col].unique()
        n_valores = len(valores_unicos)
        dict_reporte[col] = n_valores
    
    reporte = pd.DataFrame.from_dict(dict_reporte, orient = 'index')
    reporte.rename({0: 'Count'}, inplace=True, axis = 1)
 
    print('generate_report')
    print(reporte.head())
    return reporte

def save_data(reporte, filename):
    
    out_name = 'reporte_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path)
    

def main():
    
    filename = 'llamadas123_julio_2022.csv'
    datos   = get_data(filename)
    reporte = generate_report(datos)
    save_data(reporte, filename)
    
if __name__ == '__main__':
    main()
