#App para que clientes se puedan hacer los pedidos solos
# Pizza de 3 ingredientes y escojer tipo de masa
# Ingredientes pueden ser VEGETALES o PROTEICOS y la masa TRADICIONAL o DELGADA
# VEGETALES: tomate,aceitunas y champiñones
# PROTEICOS: pollo, vacuno, carne vegetal
# Los ingredientes varian segun disponibilidad (?)
# La pizza debe llevar 2 vegetales y 1 proteico 
# Todas tienen precio de 10mil y tamaño familiar
import os

class Pizza:
    precio = 10000
    tamaño = "familiar"
    vegetales = ["tomate", "aceitunas", "champiñones"]
    proteinas = ["pollo", "vacuno", "carne vegetal"]
    masas = ["tradicional", "delgada"]

    def __init__(self, masa: str, ingr1: str, ingr2: str, ingr3: str):
        self.masa = masa
        self.ingr1 = ingr1  # proteico
        self.ingr2 = ingr2  # vegetal
        self.ingr3 = ingr3  # vegetal
        self.valida = self.validar_pizza() #True or False, para saber si es pizza valida o no

    def __repr__(self):
        return f"Pizza(masa={self.masa}, proteico={self.ingr1}, vegetales={[self.ingr2, self.ingr3]})"

    @staticmethod
    def validar(ingrediente: str, lista: list[str]) -> bool:
        return ingrediente.lower() in (i.lower() for i in lista)

    def validar_pizza(self) -> bool:
        return (
            self.validar(self.masa, self.masas)
            and self.validar(self.ingr1, self.proteinas)
            and self.validar(self.ingr2, self.vegetales)
            and self.validar(self.ingr3, self.vegetales)
            and self.ingr2.lower() != self.ingr3.lower()
        )


        


    @staticmethod
    def pedido():
        print("=== Pedido de Pizza ===")
        masa = input("¿Desea masa tradicional o delgada?: ").strip().lower()
        ingr_prot = input("Ingrediente proteico (pollo, vacuno o carne vegetal): ").strip().lower()
        ingr_veg1 = input("Primer vegetal (tomate, aceitunas, champiñones): ").strip().lower()
        ingr_veg2 = input("Segundo vegetal (diferente del primero): ").strip().lower()

        pizza = Pizza(masa, ingr_prot, ingr_veg1, ingr_veg2)
        return pizza
    
        

