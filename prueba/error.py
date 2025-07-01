
class Error(Exception):
    """Clase base para errores personalizados."""
    pass

class LargoExcedidoError(Error):
    def __init__(self, mensaje="El largo es superior al permitido"):
        super().__init__(mensaje)

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje="El subtipo especificado no corresponde a un subtipo de Video, Social ni Display"):
        super().__init__(mensaje)
