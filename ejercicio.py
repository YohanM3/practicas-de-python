resultado=""
resultado = input('Introduce el primer numero a operar: ')
while True:
    if resultado == "salir":
        break
    
    ope = input('Introduce un operador "suma", "resta", "multi", "division"').lower()
    if ope == "salir":
        break
    resultado=int(resultado)
    
    num1= input("Introduce un  numero: ").lower()
    if num1=="salir":
        break
    num1 = int(num1)
        
    if ope == "suma":
        resultado+=num1
    elif ope == "resta":
        resultado -= num1
    elif ope == "multi":
        resultado *= num1
    elif ope == "division":
        resultado/=num1
    print(f"El resultado de la {ope} es {resultado}")
print('Haz Salido')
