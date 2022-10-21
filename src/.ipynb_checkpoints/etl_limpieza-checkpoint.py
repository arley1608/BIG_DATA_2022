# PSEUDO-CÓDIGO

# main()
#   datos = get_data(nombre del archivo : str) --> pd.dataframe
#   datos = remover_duplicados_y_nulos(datos : pd.dataframe)  --> pd.dataframe
#   datos = convertir_str_a_num(datos, col = 'EDAD') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA1') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA2') --> pd.dataframe
#   save_data()

from funciones_limpieza import get_data, agregar_tabla, remover_duplicados_y_nulos, convertir_str_a_num, corregir_fechas, corregir_localidad, save_data

def main():
    
    filename = 'llamadas123_agosto_2022.csv'
    print ('¿Cuantos meses se van a agregar?')
    meses = input()
    meses = int(meses)
    filename = 'llamadas123_agosto_2022.csv'
    datos = get_data(filename)    
    while meses > 0:
        meses -= 1
        print('Introduzca el mes_año:')
        mes = input()
        filename_2 = 'llamadas123_' + mes + '.csv'
        print('Agregando: ', filename_2)
        datos = agregar_tabla(datos, filename_2)
    datos   = get_data(filename)
    datos   = agregar_tabla(datos, filename_2)
    datos = remover_duplicados_y_nulos(datos)
    datos = convertir_str_a_num(datos)
    datos = corregir_fechas(datos)
    datos = corregir_localidad(datos)
    save_data(datos, filename)
    
if __name__ == '__main__':
    main()
