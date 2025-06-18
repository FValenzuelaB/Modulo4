

class Personaje:
   
    
    def __init__(self,nombre="orco"):
        self.nombre=nombre
        self.nivel=1
        self.experiencie=0

    #va a almacenar el nivel y experiancias actuales del personaje
    @property
    def estado(self):
        return f"El personaje {self.nombre} está en nivel {self.nivel} y tiene {self.experiencie} XP"    

    #adminsitrar subidas y bajadas de nivel al ganar o perder xp
    @estado.setter
    def estado(self,xp):
        tmp_xp=self.experiencie+xp

        #subir de nivel
        while tmp_xp>99:
            self.nivel+=1 
            tmp_xp-=100

        #bajar de nivel
        while tmp_xp<0:
            if self.nivel==1:
                tmp_xp=0
                self.experiencie=0
            else:
                self.nivel-=1
                tmp_xp+=100

        self.experiencie=tmp_xp

    #sobrecargar "<" para que pueda comparar los niveles de personajes
    def __lt__(self,enemy):
        return self.nivel<enemy.nivel
    
    #sobrecargar ">" para que pueda comparar los niveles de personajes
    def __gt__(self,enemy):
        return self.nivel>enemy.nivel
    
    #sobrecargar "=" para comparar niveles de personajes
    def __eq__(self,enemy):
        return self.nivel==enemy.nivel
    
    #Establecer probabilidad de ganar combate
    def probabilidad(self,enemy):
        """
        ○ Si el jugador es menor al orco, tiene un 33% de probabilidades de ganar.
        ○ Si el jugador es mayor al orco, tiene un 66% de probabilidades de ganar.
        ○ Si el jugador es igual al orco, tiene un 50% de probabilidades de ganar.
        """
        if self.nivel<enemy.nivel:
            return 33
        elif self.nivel==enemy.nivel:
            return 50
        elif self.nivel>enemy.nivel:
            return 66

    #usando la probabilidad de ganar, realizar combate
    @staticmethod
    def mostrar_dialogo(prob):
        return int(input(f"""
                         ¡Oh no!, ¡Ha aparecido un Orco!
                        Con tu nivel actual, tienes {prob} % de probabilidades de ganarle al Orco.
                        Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
                        Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
                        ¿Qué deseas hacer?
                        1. Atacar
                        2. Huir
                        :"""))

    def __str__(self):
        return f"{self.nombre}"
