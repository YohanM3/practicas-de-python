# Definir las funciones de las operaciones básicas
def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  return a / b

# Pedir al usuario que elija una operación
print("Elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación (1/2/3/4): ")

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la operación elegida y mostrar el resultado
if opcion == "1":
  print(num1, "+", num2, "=", suma(num1, num2))
elif opcion == "2":
  print(num1, "-", num2, "=", resta(num1, num2))
elif opcion == "3":
  print(num1, "*", num2, "=", multiplicacion(num1, num2))
elif opcion == "4":
  print(num1, "/", num2, "=", division(num1, num2))
else:
  print("Opción inválida")
