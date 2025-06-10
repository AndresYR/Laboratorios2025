import pandas as pd

from .dataset import Dataset


class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            if self.validado:
                print("Datos validados")
                self.limpiar_datos()

        except Exception as e:
            print(f"Error cargando archivo Excel: {e}")
