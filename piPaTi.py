import random

def juego():
    usuario = input('Por favor escoge tu arma piedra "pi", papel"pa", tijera "ti"').lower()
    computadora =random.choice(["pi", "pa", "ti"])
    
    if usuario==computadora:
        return print('Empataron')
    elif ((usuario == 'pa' and computadora =='pi')
        or (usuario == 'ti' and computadora =='pa')
        or (usuario == 'pi' and computadora =='ti')):
        print('La computador escogio: '+computadora)
        return print('Ganaste!')    
    return print('Ups la computadora ganó')


print(juego())