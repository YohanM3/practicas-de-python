"""
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""
num1=0
num2 = 0
num3 = 0

def max(num1, num2, num3):
    if num1> num2 and num1>num3:
        return "num1"
    elif num2>num1 and num2>num3:
        return "num2"
    elif num3>num1 and num3>num2:
        return "num3"
    
print(max(4,3,5))

