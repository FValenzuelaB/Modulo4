import os
from pizza import Pizza

#limpiar pantalla al iniciar
os.system("cls" if os.name == "nt" else "clear")

# a. Mostrar atributos de clase sin crear instancia
print("Ingredientes proteicos disponibles:", Pizza.proteinas)
print("Ingredientes vegetales disponibles:", Pizza.vegetales)
print("Tipos de masa disponibles:", Pizza.masas)

# b. Validar si “salsa de tomate” está en la lista
print("¿'salsa de tomate' está en la lista?", Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear instancia y solicitar ingredientes
pizza1 = Pizza.pedido()

# d. Mostrar datos del pedido
print(f"""\n=== Resumen del pedido ===)
    Ingrediente proteico: {pizza1.ingr1})
    Ingredientes vegetales: {pizza1.ingr2}, {pizza1.ingr3})
    Tipo de masa:, {pizza1.masa})
    ¿Es una pizza válida?:{pizza1.valida}""")

# e. Mostrar validez desde la clase sin instancia (esto dará error, como se solicita)
try:
    print(Pizza.validar_pizza())  # Esto debería lanzar un error dado que no hay un objeto instanciado como pizza
except:
    print("error,objeto no instanciado ")