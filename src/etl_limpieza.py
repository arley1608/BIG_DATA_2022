# PSEUDO-CÓDIGO

# main()
#   datos = get_data(nombre del archivo : str) --> pd.dataframe
#   datos = remover_duplicados_y_nulos(datos : pd.dataframe)  --> pd.dataframe
#   datos = convertir_str_a_num(datos, col = 'EDAD') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA1') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA2') --> pd.dataframe
#   save_data()

from funciones_limpieza import get_data, remover_duplicados_y_nulos, convertir_str_a_num, corregir_fechas, save_data

def main():
    
    filename = 'llamadas123_julio_2022.csv'
    datos   = get_data(filename)
    datos = remover_duplicados_y_nulos(datos)
    datos = convertir_str_a_num(datos)
    datos = corregir_fechas(datos)
    save_data(datos, filename)
    
if __name__ == '__main__':
    main()
