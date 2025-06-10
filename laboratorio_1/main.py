import domain

from os import path
from data.data_saver import DataSaver


def data_to_bbdd(ruta, nombre_tabla):
    file_extension = path.splitext(ruta)[1]

    # Cargar y limpiar data
    if file_extension == ".csv":
        data = domain.DatasetCSV(ruta)
    elif file_extension == ".xlsx":
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
    ruta = path.join(path.dirname(__file__), "files/economia.csv")
    # ruta = path.join(path.dirname(__file__), "files/Datos Empresa.xlsx")
    data_to_bbdd(ruta, "probando")
