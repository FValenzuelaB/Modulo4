import os
from producto import Producto
from tienda import Farmacia, Supermercado, Restaurante

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
limpiar()

#====CREAR TIENDA====
def crear_tienda():
    tipo_tienda=int(input("""Que tipo de tienda desea abrir?
                    1. Farmacia
                    2. Supermercado
                    3. Restaurante
                    (escriba 1, 2 o 3): """))
    nombre_tienda=str(input("Cual es el nombre de tu tienda: "))
    delivery=int(input("Cual es el costo de delivery?: "))


    if tipo_tienda not in [1,2,3]:
        print("Te dijeron que elijeras 1, 2 o 3 ay dioh mio")
        return crear_tienda()
    elif tipo_tienda ==1:
        return Farmacia(nombre_tienda,delivery)
    elif tipo_tienda ==2:
        return Supermercado(nombre_tienda,delivery)
    else:
        return Restaurante(nombre_tienda,delivery)
    
def menu(tienda):
    limpiar()
    print(tienda)
    while True:
        opcion=(input("""
                         ===MENÚ PRINCIPAL===
                         1. Ingresar producto a la tienda.
                         2. Listar productos existentes
                         3. Realizar venta
                         4. Salir
                         Elija su opción: ... """))
        if opcion=="1":
            tienda.ingresar_producto()
            limpiar()
        elif opcion=="2":
            print(tienda.listar_productos())
        elif opcion=="3":
            tienda.realizar_venta()
        elif opcion=="4":
            limpiar()
            print("Se cierra la tienda señores")
            break
        else:
            print("Porfavor ingresa una opción valida")

if __name__=="__main__":
    tienda=crear_tienda()
    menu(tienda)

