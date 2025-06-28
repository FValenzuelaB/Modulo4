class DimensionError(Exception):
    def __init__(self,mensaje,dimension,maximo):
        self.mensaje=mensaje
        self.dimension=dimension
        self.maximo=maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super ().__str__
        else:
            return f"{self.mensaje},{self.dimension},{self.maximo}"