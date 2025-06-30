from datetime import datetime
import os as o
import pytz

tz_NY=pytz.timezone('America/Santiago')
datetime_NY=datetime.now(tz_NY)

try:
    edad=int(input("Cual es tu edad?: "))
except Exception as e:
    with open (f"error.log","a",encoding="utf-8") as log:
        log.write(f"Date: {datetime_NY.strftime("%m/%d/%Y, %H:%M:%S")} El error:{e}\n")


