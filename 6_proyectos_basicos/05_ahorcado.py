# Importamos módulos
import random
import string


# Importamos la lista de palabras de un archivo externo
from assets.palabras import palabras
from assets.ahorcado_diagramas import vidas_diccionario_visual


# Definimos función obtener palabra válida
def obtener_palabra_valida(palabras):
    # Selecionar una palabra al azar de la lista
    palabra = random.choice(palabras)
    # Verificar palabras
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


# Definimos la función principal
def ahorcado():
    # Mostrar mensaje de bienvenida
    print('\n================================')
    print('    ¡Bienvenido(a) al Juego!    ')
    print('================================\n')
    # Obtener una palabra válida
    palabra = obtener_palabra_valida(palabras)
    # Seguimiento de letras
    letras_por_adivinar = set(palabra) # convertimos a un conjunto, ya que no tiene elementos repetidos
    letras_adivinadas = set() # un par de llaves vacías crea un diccionario {}
    abecedario = set(string.ascii_uppercase) # este conjunto no contiene la Ñ
    # Definir número de vidas
    vidas = 7
    # Implementamos el proceso repetitivo
    while len(letras_por_adivinar) > 0 and vidas > 0:
        if vidas == 7 and len(letras_adivinadas) == 0:
            print(f'Te quedan {vidas} vidas y aún no has usado ninguna letra.')
        elif vidas == 7 and len(letras_adivinadas) > 0:
            print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')
        elif vidas == 1:
            print(f'Te queda {vidas} vida y has usado estas letras: {" ".join(letras_adivinadas)}')
        else:
            print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')
        # Mostrar el estado actual de la palabra con un List Comprehension
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]
        # Mostrar el estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f'\nPalabra: {" ".join(palabra_lista)}')
        # Lógica para escoger las letras
        letra_usuario = input('\nEscoge una letra: ').upper()
        # Si la letra escogida por el usuario está en el abecedario y no está en el
        # conjunto de letras que ya se han ingresado, se añade la letra al conjunto
        # de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # Si la letra está en la palabra, quitar la letra del conjunto de letras
            # pendientes por adivinar. Si no está en la palabra, quitar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\nTu letra, {letra_usuario} no está en la palabra.')
        # Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print(f'\nYa escogiste esa letra. Por favor escoge una letra nueva.')
        else:
            print(f'\nEsta letra no es válida.')
    # El juego llega a esta línea cuando se adivinan todas las letras de la palabra
    # o cuando se agotan las vidas
    if vidas == 0:
        return f'¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}.\n\n'
    else:
        return f'¡Ganaste! ¡Adivinaste la palabra {palabra}!\n\n'


# Llamamos a la función principal
print(ahorcado())