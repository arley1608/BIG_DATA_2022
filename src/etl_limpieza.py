# main()
#   datos = leer_datos(nombre del archivo : str) --> pd.dataframe
#   datos = remover_duplicados_y_nulos(datos : pd.dataframe)  --> pd.dataframe
#   datos = convertir_str_a_num(datos, col = 'EDAD') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA1') --> pd.dataframe
#   datos = corregir_fechas(datos, col = 'FECHA2') --> pd.dataframe
#   save_data()

def main():
    
    filename = 'llamadas123_julio_2022.csv'
    datos   = get_data(filename)
    reporte = generate_report(datos)
    save_data(reporte, filename)
    
if __name__ == '__main__':
    main()
