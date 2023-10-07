import random

def adivinaElNumero(x):
    print('==========================================')
    print('Bienvenido al juego de adivinar el número')
    print('==========================================')

    numeroAleatorio = random.randint(1, x)    

    prediccion =0

    while prediccion!= numeroAleatorio:
        prediccion=int(input(f'Adivina el numero entre 1 y {x}: '))
        
        if prediccion <numeroAleatorio:
            print('Intenta otra vez. Este numero es muy pequeño.')
        elif prediccion > numeroAleatorio:
            print('Intenta otra vez. Este numero es muy grande.')
    print(F'Felicidades adivinaste el número {numeroAleatorio}')      


adivinaElNumero(10)