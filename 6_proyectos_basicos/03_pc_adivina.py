# Importamos módulos
import random


# Definimos la función
def adivina_el_numero_computadora(x):
    # Mostrar mensaje de bienvenida
    print('================================')
    print('    ¡Bienvenido(a) al Juego!    ')
    print('================================')
    # Meta del juego
    print(f'Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...')
    # Definimos los límites del intervalo
    limite_inferior = 1
    limite_superior = x
    respuesta = ''
    # Funcionalidad del juego
    # Iteremos las respuestas. Cantidad indefinida
    while respuesta != 'c':
        # Generar la prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior  # también podría ser el otro, porque son iguales
        # Obtener una respuesta del usuario en minúsculas
        respuesta = input(f'Mi predicción es {prediccion}. Si es muy alta, ingresa la letra A. Si es muy baja, ingresa la letra B. Si es correcta, ingresa la letra C: ').lower()
        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
    # Mensaje de felicitaciones
    print(f'¡Siii! La computadora adivinó tu número correctamente: {prediccion}')


# Llamamos a la función
adivina_el_numero_computadora(10)