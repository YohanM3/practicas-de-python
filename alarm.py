import datetime
import time
import os

# Obtener una entrada válida del usuario para la hora de la alarma
invalido = True
while (invalido):
    print("Establezca una hora válida para la alarma (Ej. 06:30)")
    entrada_usuario = input(">> ")
    # Convertir la entrada del usuario en una lista de enteros
    hora_alarma = [int(n) for n in entrada_usuario.split(":")]
    # Validar que la hora sea entre 0 y 23 y el minuto entre 0 y 59
    if hora_alarma[0] >= 24 or hora_alarma[0] < 0:
        invalido = True
    elif hora_alarma[1] >= 60 or hora_alarma[1] < 0:
        invalido = True
    else:
        invalido = False

# Obtener la hora actual y convertirla en segundos
ahora = datetime.datetime.now()
segundos_actuales = ahora.hour * 3600 + ahora.minute * 60 + ahora.second

# Convertir la hora de la alarma en segundos
segundos_alarma = hora_alarma[0] * 3600 + hora_alarma[1] * 60

# Calcular el tiempo restante hasta la alarma en segundos
tiempo_restante = segundos_alarma - segundos_actuales

# Si el tiempo restante es negativo, significa que la alarma es para el día siguiente
if tiempo_restante < 0:
    tiempo_restante += 24 * 3600

# Mostrar el tiempo restante en formato hh:mm:ss
tiempo_restante_formato = time.strftime(
    "%H:%M:%S", time.gmtime(tiempo_restante))
print(f"La alarma sonará en {tiempo_restante_formato}")

# Esperar hasta que el tiempo restante sea cero
time.sleep(tiempo_restante)

# Reproducir un sonido cuando suene la alarma (cambiar el nombre del archivo según sea necesario)
os.system("start alarm.mp3")
