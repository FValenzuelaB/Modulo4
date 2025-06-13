
# Tipos de te: Te negro, te verde e infusiones
# Tiempos de preparación: 3, 5 y 6 minutos
# Consumo recomendado: 
# Tamaños: 300 y 500 gr
# precios: $3000 y $5000

class Te:

    #Atributo de clase
    duración=365

    sabores={
        1:{
            "nombre":"te negro",
            "tiempo":"3 minutos", 
            "recomendacion":"desayuno"
            },
        2:{
            "nombre":"te verde",
            "tiempo":"5 minutos", 
            "recomendacion": "almuerzo"
            },
        3:{
            "nombre":"infusion",
            "tiempo":"6 minutos", 
            "recomendacion": "once"
            }
    }

    precios={
        300:3000,
        500:5000
    }

    #debe retornar tiempo de preparación
    @staticmethod
    def receta(sabor):
        preparar=Te.sabores[sabor]
        return preparar["nombre"], preparar["tiempo"], preparar["recomendacion"]

    @staticmethod
    def obtener_precio(tamaño):
        precio=Te.precios[tamaño]
        return precio
