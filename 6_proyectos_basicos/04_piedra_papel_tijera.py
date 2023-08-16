# Importamos módulos
import random


# Definimos la función principal
def jugar():
    # Preguntamos al usuario. Con \n hacemos un salto de línea.
    usuario = input(f'Escoge una opción: "pi" para piedra, "pa" para papel, "ti" para tijera.\n').lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    # Analizamos las opciones
    if usuario == computadora:
        return f'¡Empate!\nLa computadora también eligió {computadora}'
    if gano_el_jugador(usuario, computadora):
        return f'¡Ganaste!\nLa computadora eligió {computadora}'
    return f'¡Perdiste!\nLa computadora eligió {computadora}'


def gano_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra gana a Tijera (pi > ti)
    # Tijera gana a Papel (ti > pa)
    # Papel gana a Piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


# Llamamos a la función
print(jugar())