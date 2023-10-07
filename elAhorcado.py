import random

from palabras import palabras


def obtenerPalabraValida ():
    palabra = obtenerPalabraValida(palabras)
    palabra=random.choice(palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra=random.choice(palabras)
    return palabra.upper()


def ahorcado():
    palabra=obtenerPalabraValida(palabras)
    letrasPorAdivinar= set (palabra)
    letrasAdivinadas=
    abecedario=
