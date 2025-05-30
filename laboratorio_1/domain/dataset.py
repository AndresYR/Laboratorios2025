from abc import ABC


class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, value):
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente
