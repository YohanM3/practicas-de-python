import secrets
import string

# Definir el alfabeto de los caracteres posibles para la contraseña
alfabeto = string.ascii_letters + string.digits + string.punctuation

# Pedir al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Generar la contraseña usando el módulo secrets
contraseña = "".join(secrets.choice(alfabeto) for i in range(longitud))

# Mostrar la contraseña generada
print(f"Su contraseña es: {contraseña}")
