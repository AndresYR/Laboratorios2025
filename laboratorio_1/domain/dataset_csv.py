import pandas as pd

from .dataset import Dataset


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:

            def leer_csv(fuente):
                sep = [",", ";", "\t", "|", "/"]
                for s in sep:
                    df = pd.read_csv(fuente, sep=s)
                    if df.shape[1] > 1:
                        break
                return df

            self.datos = leer_csv(self.fuente)
            if self.validado:
                print("Datos validados")
                self.limpiar_datos()

        except Exception as e:
            print(f"Error cargando archivo CSV: {e}")
