# Importar módulos
import time
import tkinter as tk

# Crear ventana
window = tk.Tk()
window.title("Temporizador de cuenta regresiva")
window.geometry("300x150")

# Crear etiqueta para mostrar el tiempo restante
label = tk.Label(window, text="00:00:00", font=("Arial", 32))
label.pack()

# Crear función para iniciar el temporizador
def start_timer():
    global hours, minutes, seconds # Guardar las variables de tiempo como globales
    hours = int(entry_hours.get()) # Obtener las horas del usuario
    minutes = int(entry_minutes.get()) # Obtener los minutos del usuario
    seconds = int(entry_seconds.get()) # Obtener los segundos del usuario
    countdown() # Llamar a la función de cuenta regresiva

# Crear función para actualizar el temporizador
def countdown():
    global hours, minutes, seconds # Usar las variables de tiempo globales
    if hours > 0 or minutes > 0 or seconds > 0: # Si el tiempo no se ha acabado
        if seconds == 0: # Si los segundos son cero
            seconds = 59 # Restablecer los segundos a 59
            minutes -= 1 # Restar un minuto
            if minutes == -1: # Si los minutos son -1
                minutes = 59 # Restablecer los minutos a 59
                hours -= 1 # Restar una hora
        else: # Si los segundos no son cero
            seconds -= 1 # Restar un segundo
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}" # Formatear el tiempo como una cadena
        label.config(text=time_str) # Actualizar el texto de la etiqueta con el tiempo
        window.after(1000, countdown) # Llamar a la función de cuenta regresiva después de un segundo
    else: # Si el tiempo se ha acabado
        label.config(text="¡Tiempo acabado!") # Mostrar un mensaje en la etiqueta

# Crear entradas para que el usuario ingrese el tiempo deseado
entry_hours = tk.Entry(window)
entry_hours.pack(side=tk.LEFT)
entry_minutes = tk.Entry(window)
entry_minutes.pack(side=tk.LEFT)
entry_seconds = tk.Entry(window)
entry_seconds.pack(side=tk.LEFT)

# Crear botón para iniciar el temporizador
start_button = tk.Button(window, text="Iniciar", command=start_timer)
start_button.pack(side=tk.LEFT)

# Iniciar el bucle principal de la ventana
window.mainloop()
