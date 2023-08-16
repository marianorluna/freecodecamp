# Importamos módulos
import random


# Definimos una función
def adivina_el_numero(x):
    # Mostrar mensaje de bienvenida
    print('================================')
    print('    ¡Bienvenido(a) al Juego!    ')
    print('================================')
    # Meta del juego
    print('Tu meta es adivinar el número generado por la computadora.')
    
    # Funcionalidad del juego
    # Definimos una variable con un número aleatorio entre 1 y x
    numero_aleatorio = random.randint(1, x)
    # Definimos la lógica principal del juego
    prediccion = 0
    # Creamos un ciclo para un número indeterminado de veces
    while prediccion != numero_aleatorio:
        # El usuario ingresa un número
        prediccion = int(input(f'Adivina un número entre 1 y {x}: '))
        # Usamos un condicional para las dos opciones posibles
        if prediccion < numero_aleatorio:
            print('Intenta otra vez. Este número es muy pequeño.')
        elif prediccion > numero_aleatorio:
            print('Intenta otra vez. Este número es muy grande.')
    print(f'¡Felicitaciones! Adivinaste el número {numero_aleatorio} secreto.')


#LLamamos a la función
adivina_el_numero(10)