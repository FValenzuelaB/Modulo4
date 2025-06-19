from abc import ABC, abstractmethod


#farmacias, supermercado y restaurante
class Tienda(ABC):
    def __init__(self,nombre,delivery):
        self.nombre=nombre
        self.delivery=delivery
        self.productos=[]
    #debe poder vender, ingresar y listar productos
    #cada tienda tiene nombre, lista de productos y costo de delivery
    #para crear la tienda en si, solo se requiere nombre y costo de delivery
    pass

    @abstractmethod
    def vender():
        pass

    @abstractmethod
    def comprar():
        pass



    

class Tienda_Restaurante(Tienda):
    pass

class Tienda_Supermercado(Tienda):
    pass

class Tienda_Farmacia(Tienda):
    pass