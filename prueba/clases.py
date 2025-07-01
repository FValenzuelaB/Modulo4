from abc import ABC,abstractmethod
from error import LargoExcedidoError,SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self,ancho,alto,url_archivo,url_click,subtipo):
        self.__ancho=ancho if ancho>0 else 1
        self.__alto=alto if alto>0 else 1
        self.__url_archivo=url_archivo
        self.__url_click=url_click
        self.__subtipo=subtipo

    def __repr__(self):
        return
    
    @property
    def ancho(self):
        return self.__ancho   
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho=ancho

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self,alto):
        self.__alto=alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self,url_archivo):
        self.__url_archivo=url_archivo

    @property
    def url_click(self):
        return self.__url_click
    @url_click.setter
    def url_click(self,url_click):
        self.__url_click=url_click

    @staticmethod
    def mostrar_formatos():
        return {Video.FORMATO} - {Social.FORMATO} 
    
    @property
    def subtipo(self):
        return self.__subtipo
    @subtipo.setter
    def subtipo(self,subtipo):       
        if (isinstance(self,Video) and self.subtipo in Video.SUB_TIPOS 
            or isinstance(self,Display) and self.subtipo in Display.SUB_TIPOS
            or isinstance(self,Social) and self.subtipo in Social.SUB_TIPOS):
            self.__subtipo=subtipo 
        else:
            raise SubTipoInvalidoError

    
    
    @abstractmethod
    def comprimir_anuncio():
        pass
    
    @abstractmethod
    def redimensionar_anuncio():
        pass


class Campana:
    def __init__(self,nombre:str,fecha_inicio,fecha_termino):
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_termino=fecha_termino
        self.__anuncios=[self.componer_anuncio()]

    def componer_anuncio(self):
        opcion = int(input("que tipo de anuncio quieres  1 -  para video - 2 para display - 3 para social"))
        if opcion == 1:
            duracion = int(input("cual es la duracion del video? (minimo 5): "))
            new_anuncio = Video(duracion)
        elif opcion == 2:
            new_anuncio = Display()
        elif opcion == 3:
            new_anuncio = Social()
        return new_anuncio

    def agregar_anuncios(self):
        while True:
            try:
                opcion = int(input("que tipo de anuncio quieres  1 -  para video - 2 para display - 3 para social"))
                if opcion == 1:
                    duracion = int(input("cual es la duracion del video  minimo 5"))
                    new_anuncio = Video(duracion)
                elif opcion == 2:
                    new_anuncio = Display()
                elif opcion == 3:
                    new_anuncio = Social()
                else:
                    break
                self.__anuncios.append(new_anuncio)
            except Exception as e:
                pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        if len(nombre)<250:
            self.__nombre=nombre
        else:
            raise LargoExcedidoError
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self,fecha_termino):
        self.__fecha_termino=fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __repr__(self):
        return f"{self.__nombre} Anuncios:{self.__anuncios}"


class Video(Anuncio):
    FORMATO="Video"
    SUB_TIPOS=("instream","outstream")
    def __init__(self,duracion):
        self.ancho=1
        self.alto=1
        self.__duracion=duracion if duracion>0 else 5

    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self,duracion):
        self.__duracion=duracion

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN\n")
    
    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN\n")

    def __repr__(self):
        return f"{Video.FORMATO} - {self.duracion}"

class Display(Anuncio):
    FORMATO="Display"
    SUB_TIPOS=("tradicional","native")

    def __init__(self,ancho,alto,url_archivo,url_click,subtipo):
        super().__init__(ancho, alto, url_archivo, url_click, subtipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN\n")
    
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN\n")
    
    def __repr__(self):
        return f"{Display.FORMATO}"


class Social(Anuncio):
    FORMATO="Social"
    SUB_TIPOS=("facebook","linkedin")

    def __init__(self,ancho,alto,url_archivo,url_click,subtipo):
        super().__init__(ancho, alto, url_archivo, url_click, subtipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN\n")
    
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN\n")

    def __repr__(self):
        return f"{Social.FORMATO}"


