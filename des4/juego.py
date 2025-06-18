from personaje import Personaje
import random

print("Bienvenido a gran fantasía")
nombre=str(input("Ingrese el nombre de su personaje: ")).strip()

#Crear personaje y orco y mostrar personaje
personaje=Personaje(nombre)
orco=Personaje()
print(personaje.estado)


#Crear probabilidad inicial basado en niveles y mostrar dialogo inicial que da opcion de pelear o huir, recibiendo la opcion
prob=personaje.probabilidad(orco)
opcion=Personaje.mostrar_dialogo(prob)

#Combate en base a suerte, donde se obtendra un random y este se compara con la probabilidad de ganar
while opcion==1:
    resultado= "g" if random.uniform(0,100)<prob else "p"
    if resultado =="g":
        print ("""¡Le has ganado al orco, felicidades!
                  ¡Recibirás 50 puntos de experiencia!
               """)
        personaje.estado=50
        orco.estado=-30
    else:
        print("""¡Oh no! ¡El orco te ha ganado!
                 ¡Has perdido 30 puntos de experiencia!
              """)
        personaje.estado=-30
        orco.estado=50
    print(personaje.estado)
    print(orco.estado)
    prob=personaje.probabilidad(orco)
    opcion=Personaje.mostrar_dialogo(prob)


print("¡Has huido! El orco ha quedado atrás.")