# Importar módulos
import pygame
import tkinter as tk
from tkinter import filedialog

# Inicializar pygame
pygame.init()
pygame.mixer.init()

# Crear ventana
window = tk.Tk()
window.title("Reproductor de música")
window.geometry("300x150")

# Crear etiqueta para mostrar el nombre del archivo
label = tk.Label(window, text="Ningún archivo seleccionado")
label.pack()

# Crear función para abrir un archivo de música
def open_file():
    global filename # Guardar el nombre del archivo como una variable global
    filename = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos MP3", "*.mp3"), ("Todos los archivos", "*.*"))) # Pedir al usuario que seleccione un archivo
    if filename: # Si el usuario seleccionó un archivo
        label.config(text=filename) # Cambiar el texto de la etiqueta al nombre del archivo

# Crear función para reproducir el archivo de música
def play_file():
    if filename: # Si hay un archivo seleccionado
        pygame.mixer.music.load(filename) # Cargar el archivo en el mixer de pygame
        pygame.mixer.music.play() # Reproducir el archivo

# Crear función para pausar el archivo de música
def pause_file():
    if filename: # Si hay un archivo seleccionado
        pygame.mixer.music.pause() # Pausar el archivo

# Crear función para reanudar el archivo de música
def resume_file():
    if filename: # Si hay un archivo seleccionado
        pygame.mixer.music.unpause() # Reanudar el archivo

# Crear botones para las funciones
open_button = tk.Button(window, text="Abrir", command=open_file)
open_button.pack(side=tk.LEFT)

play_button = tk.Button(window, text="Reproducir", command=play_file)
play_button.pack(side=tk.LEFT)

pause_button = tk.Button(window, text="Pausar", command=pause_file)
pause_button.pack(side=tk.LEFT)

resume_button = tk.Button(window, text="Reanudar", command=resume_file)
resume_button.pack(side=tk.LEFT)

# Iniciar el bucle principal de la ventana
window.mainloop()
