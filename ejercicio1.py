"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

numero=0
numero1=0
def max(numero, numero1):
    if numero>numero1:
        return numero
    else:
        return numero1
print(max(1,2))
