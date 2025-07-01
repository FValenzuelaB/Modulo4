



class Error(Exception):
    pass

class LargoExcedidoError(Error):
    print("El largo es superior al permitido")

class SubTipoInvalidoError(Error):
    print("El subtipo especificado no corresponde a un subtipo de Video, Social ni Display")
