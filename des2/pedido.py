from te import Te
import os

os.system("cls" if os.name == "nt" else "clear")
opcion_sabor=int(input("""
               ===MENU DE TE===
             1.Te Negro
             2.Te Verde
             3.Infusión
             
             elección (1, 2 o 3): """))

opcion_tamaño=int(input("""
               ===ELEGIR TAMAÑO===
                300 gramos
                500 gramos

                Tamaño elegido (300 o 500): """))

nombre,tiempo,recomendacion=Te.receta(opcion_sabor)
precio=Te.obtener_precio(opcion_tamaño)

os.system("cls" if os.name == "nt" else "clear")
print (f"""
        Tipo de té: {nombre}
        Tiempo de preparación: {tiempo}
        Se recomienda domarlo a la hora de: {recomendacion}
        Tamaño o formato: {opcion_tamaño} gramos
        precio: ${precio} CLP
        Duración: {Te.duración} días
       """)