#programa para generar un número aleatorio 

import random

#La función input captura la información desde el tyeclado como si fuera una cadena de texto (string)
a=input("Limite inferior: ")
b=input("Limite superior: ")

#convertir una cadena de texto en un texto
a=int(a)
b=int(b)
respuesta=random.randint(a,b)
print(respuesta)

