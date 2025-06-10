import domain

from pathlib import Path
from data.data_saver import DataSaver


def standar_name(s):
    return s.lower().strip().replace(" ", "_")


def data_to_bbdd(ruta):

    nombre_tabla = standar_name(ruta.name).replace(".", "_")

    # Cargar y limpiar data
    if ruta.suffix == ".csv":
        data = domain.DatasetCSV(ruta)
    elif ruta.suffix == ".xlsx":
        data = domain.DatasetExcel(ruta)
    else:
        raise TypeError("Por favor ingresa un archivo CSV o Excel")
    data.cargar_datos()

    # Mostrar reporte
    data.mostrar_reporte()

    # Guardar en BBDD
    db = DataSaver()
    db.guardar_dataframe(data.datos, nombre_tabla)


if __name__ == "__main__":
    # Detectar archivos compatibles en carpeta /files
    directorio = Path("./files")
    archivos_csv = list(directorio.glob("*.csv"))
    archivos_excel = list(directorio.glob("*.xlsx"))
    archivos = archivos_csv + archivos_excel

    # Iterar archivos encontrados
    for archivo in archivos:
        data_to_bbdd(archivo)
        print(f"Datos de archivo {archivo.name} guardados exitosamente\n")
        print("--------------------------------------------\n")
    print("EJECUCION FINALIZADA")
