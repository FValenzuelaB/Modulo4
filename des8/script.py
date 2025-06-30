from usuario import Usuario
from datetime import datetime
import json
import pytz

tz_CL=pytz.timezone('America/Santiago')
datetime_CL=datetime.now(tz_CL)
instancias=[]

ruta="usuarios.txt"
with open(ruta) as u:
    linea=u.readline()
    while linea:
        try:
            usuario=json.loads(linea)
            instancias.append(
                Usuario(
                    usuario.get("nombre"),
                    usuario.get("apellido"),
                    usuario.get("email"),
                    usuario.get("genero")
                    ))
        
        except Exception as e:
            with open (f"error.log","a",encoding="utf-8") as log:
                log.write(f"Date: {datetime_CL.strftime("%m/%d/%Y, %H:%M:%S")} El error:{e}\n")

        finally:
            linea=u.readline()

print(instancias)