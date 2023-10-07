'''
number = int(input('Ingrese un numero: '))
result = number %2
if (result == 0):
    print('Es par')
else:
    print('Es impar')
'''

user_option = input('elige entre piedra, papel o tijera: ')
computer_option ='papel'

if user_option==computer_option:
    print('Estan empatados')
elif user_option =='piedra' :
    if computer_option=='tijera':
        print('Has ganado')
    if computer_option=='papel':
        print('La computadora ha ganado')
elif user_option=='papel':
    if computer_option=='piedra':
        print('Has ganado')
    if computer_option=='tijera':
        print('La computadora ha ganado')
elif user_option=='tijera':
    if computer_option=='papel':
        print('Has ganado')
    if computer_option=='piedra':
        print('La computadora ha ganado')
else:
    print('No es una opción valida')
