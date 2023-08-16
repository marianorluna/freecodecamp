# Concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ______________.

# Creamos una variable con el texto a rellenar
# organizacion = 'freeCodeCamp'

# Lo imprimimos por pantalla concatenando
# print('Aprende a programar con ' + organizacion)
# Lo imprimimos por pantalla con el método format
# print('Aprende a programar con {}'.format(organizacion))
# Lo imprimimos con f-string
# print(f'Aprende a programar con {organizacion}')

# Mad Libs (Historias Locas)
# Guardamos el párrafo en una variable
adjetivo = input('Ingresa un adjetivo: ')
verbo1 = input('Ingresa un verbo: ')
verbo2 = input('Ingresa otro verbo: ')
sustantivo_plural = input('Ingresa un sustantivo en plural: ')

madlib = f'¡Programar es tan {adjetivo}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!'

print(madlib)