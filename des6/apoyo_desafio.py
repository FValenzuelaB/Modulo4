from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho<1 or ancho>self.MAX:
            raise DimensionError(f"El ancho {ancho} es invalido",self.MAX)
        else:
            self.__ancho=ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto<1 or alto>self.MAX:
            raise DimensionError(f"El alto {alto} es invalido",self.MAX)
        else:
            self.__alto=alto