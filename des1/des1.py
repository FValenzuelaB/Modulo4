import os
import math

#Crear clase velocidad escape, que manejará radio y la constante "g" en verioes privadas.
class Velocidad_escape:
    def __init__(self,radio:int,cte_g:float):
        self.__radio=radio
        self.__cte_g=cte_g

    
    @property
    def radio(self):
        return self.__radio
    
    @property
    def cte_g(self):
        return self.__cte_g
    
    def __repr__(self):
        return repr([self.radio,self.cte_g])
    

#Rentabilidad = Precio*Usuarios - Gastos totales, se creará clase para versión normal y luego sublcase para versión con usuarios premium
class Rentabilidad:
    def __init__(self,precio:int,usuarios:int,gastos:int):
        self.__precio=precio
        self.__usuarios:usuarios
        self.__gastos=gastos
    
    @property
    def precio(self):
        return self.__precio

    @property
    def usuarios(self):
        return self.__usuarios
    
    @property
    def gastos(self):
        return self.__gastos
    
    def __repr__(self):
        return repr([self.precio,self.usuarios,self.gastos])


#Esta es la version con usuarios premium, que se hibrida de la original solo agregando un atributo, user_p para el nuemro de usuarios premium
class Rentabilidad_premium(Rentabilidad):
    #constructor de rentabilidad premium
    def __init__(self,precio:int,usuarios:int,gastos:int,user_p:int):
        #constructor de rentabilidad
        super().__init__(precio,usuarios,gastos)
        self.__user_p=user_p

    @property
    def user_p(self):
        return self.__user_p
    
    def __repr__(self):
        return repr([self.precio,self.usuarios,self.gastos,self.user_p])


class Razon(Rentabilidad):
    def __init__(self,precio:int,usuarios:int,gastos:int,ut_ant):
        super().__init__(precio,usuarios,gastos)
        self.__ut_ant=ut_ant

    @property
    def ut_ant(self):
        return self.__ut_ant
    
    def __repr__(self):
        return repr([self.precio,self.usuarios,self.gastos,self.ut_ant])

#Se creará el menu para escojer desafio a evaluar
class Menu:
    #limpiar consola
    #display menu

    @staticmethod
    def limpiar_consola():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def mostrar_menu():
        print("""
        === menu desafio 1 ===
                    
        1. Velocidad de escape
        2. Rentabilidad 1 (solo usuarios normales)
        3. Rentabilidad 2 (con usuarios premium)
        4. Rentabilidad 3 (Razón de utilidades ahora vs año pasado)
        5. Salir
        """)

#clase que albergará funciones que pedirán selectivamente los datos necesarios para armar los objetos según opción ingresada
class Getget:

    #Pedir datos para calcular velocidad de escape
    @staticmethod
    def vel_escape():
        radio = int(input("Intoduzca el radio del planeta en kilometros :"))
        g = float(input("Introduzca la fuerza de gravedad en metros/segundos al cuadrado :"))
        return Velocidad_escape(radio,g)

    #Pedir datos para rentabilidad solo con usuarios normales
    @staticmethod
    def Rent1():
        precio=int(input("Ingrese el precio de suscripción: "))
        usuarios=int(input("Ingrese la cantidad de usuarios: "))
        gastos=int(input("Ingrese los gastos totales: "))
        return Rentabilidad(precio,usuarios,gastos)

    #Pedir datos para rentabilidad con usuarios normales y premium
    @staticmethod
    def Rent2():
        precio=int(input("Ingrese el precio de suscripción: "))
        usuarios=int(input("Ingrese la cantidad de usuarios: "))
        premium=int(input("Ingrese numero de usuarios premium"))
        gastos=int(input("Ingrese los gastos totales: "))
        return Rentabilidad(precio,usuarios,gastos,premium)

    @staticmethod
    def Rent3():
        precio=int(input("Ingrese el precio de suscripción: "))
        usuarios=int(input("Ingrese la cantidad de usuarios: "))
        gastos=int(input("Ingrese los gastos totales: "))
        ut_ant=int(input("Ingrese las utilidades anteriores:"))
        return Razon(precio,usuarios,gastos,ut_ant)


class App():
    def run(self):
        while True:
            Menu.limpiar_consola()
            Menu.mostrar_menu()\
            
            opcion = input("Elige una opcion : ")

            #Velocidad de escape
            if opcion == "1":
                v= Getget.vel_escape()
                vel=math.sqrt(2*v[0]*v[1])/1000
                print(f"La velocidad es {vel:.1f} metros por segundos!")
                
            # Rentabilidad 1
            elif opcion == "2":
                r = Getget.Rentabilidad()
                rent1=r[0]*r[1]-r[2]
                print(f"Las utilidades son de {rent1} pesos!")


            elif opcion == "3":
                r = Getget.Rentabilidad_premium()
                rent2=(r[0]*r[1]+r[0]*1,5*r[3])-r[2]
                print(f"Las utilidades son de {rent2} pesos!")

            
            elif opcion == "4":
                r = Getget.Razon()
                razon=(r[0]*r[1]-r[2])/r[3]
                print(f"La razón de utilidad actual versus anterior es de {razon}")

            elif opcion == "5":
                Menu.limpiar_consola()
                print("Hasta luego!")
                break
owo=App()                   
owo.run()





            