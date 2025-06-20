
#producto tiene nombre, precio, cantidad
class Producto:
    def __init__(self,nombre,precio,stock=0):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__nombre=nombre
        self.__precio=precio
        self.__stock=stock

     # === Getters ===
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    # === Setters (solo stock) ===
    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = max(0, nuevo_stock)

    #se sobrecarga equivalente para poder usarlao en clases
    def __eq__(self,otro):
        return self.nombre==otro.nombre
    
    #se sobrecarga suma para poder sumar clases
    def __iadd__(self, otro):
        if self == otro:
            self.stock += otro.stock
            nuevo=Producto(self.nombre,self.precio,self.stock)
            return nuevo
        raise ValueError("No se pueden sumar productos diferentes")
    
    #se sobrecarga resta para poder restar clases
    def __sub__(self, cantidad):
        if isinstance(cantidad, int):
            nuevo_stock = max(0, self.stock - cantidad)
            nuevo = Producto(self.nombre, self.precio, nuevo_stock)
            return nuevo
        raise TypeError("La cantidad debe ser un entero")

    #para los print, vuelve la clase printeable xd
    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio = ${self.precio}\nstock={self.stock}"
    