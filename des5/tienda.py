from abc import ABC, abstractmethod
from producto import Producto


#farmacias, supermercado y restaurante
class Tienda(ABC):
    def __init__(self,nombre,delivery):
        self.__nombre=nombre
        self.__delivery=delivery
        self._productos=[]


    #===GETTER==
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def delivery(self):
        return self.__delivery
    
    @abstractmethod
    def ingresar_producto(self):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self):
        pass

    # Método para buscar producto
    def buscar_producto(self, nombre_producto):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                return producto
        return None


class Restaurante(Tienda):
    def ingresar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        producto = Producto(nombre, precio, 0)

        if producto in self._productos:
            print("Producto ya existe. No se modifica nada.")
        else:
            self._productos.append(producto)

class Tienda_Supermercado(Tienda):
    pass

class Tienda_Farmacia(Tienda):
    pass