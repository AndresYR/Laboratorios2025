import pandas as pd

from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None
        self.__validado = False

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, value):
        if not self.validado:
            self.validar_datos(value)
            self.__datos = value
        else:
            self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @property
    def validado(self):
        return self.__validado

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Los datos ingresados deben ser un DataFrame")

        if df is None:
            raise ValueError("Datos no cargados.")

        if df.empty:
            raise ValueError("El DataFrame está vacío")

        self.__validado = True

    def limpiar_datos(self):
        if self.datos is not None:
            print("\n--- Inicio de Limpieza de Datos ---")
            df = self.datos.copy()

            duplicados = df.duplicated().sum()
            if duplicados > 0:
                print("Filas duplicadas detectadas")
                df = df.drop_duplicates()
                print(f"Se han eliminado {duplicados} filas duplicadas")
            # Encabezados a minuscula y reemplaca espacios por _
            df.columns = df.columns.str.lower().str.replace(" ", "_")
            # Elimina espacios vacios y convierte a minuscula en columnas tipo object
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].astype(str).str.strip().str.lower()

            self.datos = df
            print("--- Fin de Limpieza de Datos ---")
        else:
            print("No hay datos para limpiar")

    def mostrar_reporte(self):
        if self.datos is not None:
            print("\n--- Reporte del DataFrame ---")
            print(f"Filas: {self.datos.shape[0]}    Columnas: {self.datos.shape[1]}\n")
            for index, value in self.datos.isnull().sum().items():
                print(
                    f"El campo <{index}> es de tipo <{self.datos[index].dtypes}> y contiene <{value}> datos faltantes. ({value*100/self.datos.shape[0]:.2f}%)\n"
                )
            print("\n- Estadisticas -")
            print(self.datos.describe())
            print("\n- DataFrame -")
            print(self.datos.head())
