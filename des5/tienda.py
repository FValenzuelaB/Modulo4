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

    def listar_productos(self):
        lista="Productos restaurante:\n "
        for producto in self.productos:
            lista+= f"Producto: {producto.nombre}, Precio: ${producto.precio}\n"
        return lista
    
    def realizar_venta(self):
        nombre = input("Producto vendido: ")
        producto = self.buscar_producto(nombre)
        if producto:
            print(f"{producto.nombre} vendido") #En restaurante no baja el stock dado que siempre es 0
        else:
            print("Producto no encontrado.")

class Supermercado(Tienda):
    def ingresar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        nuevo_producto = Producto(nombre, precio, stock)

        for i, prod in enumerate(self._productos):
            if prod==nuevo_producto:
                new=nuevo_producto+prod
                self._productos[i]=new
                print(f"Producto {new.nombre} fue actualizado, su nuevo stock es: {new.stock}")          
            else:
                self._productos.append(nuevo_producto)


    def listar_productos(self):
        lista="Productos restaurante:\n "
        for producto in self.productos:
            if producto.stock<10:
                lista+= f"Producto: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock} Pocos prodcutos disponibles \n"
            else:
                lista+=f"Producto: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}"
        return lista
    
    def realizar_venta(self):
        vendido=str(input("Producto vendido: "))
        cantidad=int(input("Cantidad vendida: "))
        producto=Tienda.buscar_producto(vendido)
        if producto in self._productos and producto.stock>cantidad:
            print("Producto vendido!!")
            producto.stock-=cantidad
        elif producto not in self.productos:
            print("Producto no encontrado") 
        elif producto.stock<cantidad:
            c=min(cantidad,producto.stock)
            producto.stock-=c
            print(f"Cantidad en stock es insuficiente, solo se venden{c} ") 
    
class Farmacia(Tienda):
    def ingresar_producto(self):
        nombre=str(input("Nombre producto:"))
        precio=float(input("Precio: "))
        stock=int(input("Precio: "))
        new_product=Producto(nombre,precio,stock)
        for i, prod in enumerate(self._productos):
            if prod==new_product:
                new=new_product+prod
                self._productos[i]=new
                print(f"Producto {new.nombre} fue actualizado, su nuevo stock es: {new.stock}")          
            else:
                self._productos.append(new_product)
    
    def listar_productos(self):
        lista="Lista de productos farmacia:\n"
        for producto in self._productos:
            if producto.precio>15000:
                lista+=f"Producto: {producto.nombre}, Precio: ${producto.precio}, Envío gratis al solicitar este producto"
            else:
                lista+=f"Producto: {producto.nombre}, Precio: ${producto.precio}"
        return lista
    
    def realizar_venta(self):
        vendido=str(input("Producto vendido: "))
        cantidad=int(input("Cantidad vendida: "))
        producto=Tienda.buscar_producto(vendido)
        if producto in self._productos and producto.stock>cantidad and cantidad<4:
            print("Producto vendido!!")
            producto.stock-=cantidad
        elif producto not in self.productos:
            print("Producto no encontrado") 
        elif producto.stock<cantidad:
            c=min(cantidad,producto.stock)
            producto.stock-=c
            print(f"Cantidad en stock es insuficiente, solo se venden{c} ") 

