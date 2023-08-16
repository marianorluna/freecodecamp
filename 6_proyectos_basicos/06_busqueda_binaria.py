# Importar módulos
import random
import time


# Definimos la primera búsqueda (ingenua o inocente)
def busqueda_ingenua(lista, target):    # target = objetivo
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1   # se usa -1 porque no es un índice válido, indica que no existe


# Definimos la segunda búsqueda (binaria, eliminamos la mitad de las opciones)
# La lista debe estar ordenada en forma ascendente
def busqueda_binaria(lista, target, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # Inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista)-1  # Final de la lista
    # Comprobar que el intervalo es válido
    if limite_superior < limite_inferior:
        return -1   # Se termina la ejecución porque no es válido
    # Usamos la versión recursiva
    punto_medio = (limite_inferior + limite_superior) // 2  # Este operador // trunca lo decimales
    # Evaluamos el punto medio
    if lista[punto_medio] == target:
        return punto_medio
    elif target < lista[punto_medio]:
        return busqueda_binaria(lista, target, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, target, punto_medio+1, limite_superior)


# Esto lo escribimos cuando no queremos ejecutar por defecto el código
# Si importamos este módulo a otro lado
if __name__ == '__main__':
    # Creamos una lista ordenada con X números aleatorios
    # Cantidad BI hasta 10mil de números
    # Cantidad BB hasta 10millones de números
    cantidad = 10000
    conjunto_inicial = set()
    while len(conjunto_inicial) < cantidad:
        conjunto_inicial.add(random.randint(-3*cantidad, 3*cantidad))
    # Ordenamos la lista de forma ascendente
    lista_ordenada = sorted(list(conjunto_inicial))
    # Medir el tiempo de búsqueda ingenua
    inicio = time.time()
    for target in lista_ordenada:
        busqueda_ingenua(lista_ordenada, target)
    fin = time.time()
    print(f'Tiempo de búsqueda ingenua: {fin - inicio} segundos.')
    # Medir el tiempo de búsqueda binaria
    inicio = time.time()
    for target in lista_ordenada:
        busqueda_binaria(lista_ordenada, target)
    fin = time.time()
    print(f'Tiempo de búsqueda binaria: {fin - inicio} segundos.')