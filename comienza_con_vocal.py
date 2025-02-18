"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
#Pedir palabra
#Pedir upper de la primera letra igual a 

# Entradas
entrada = input("Escribe una palabra ")

# Proceso
valor0 = (entrada).upper()

valor = ord(valor0[0])
si = "'" + entrada + "'" + " comienza con vocal"
no =  "'" + entrada + "'" + " no comienza con vocal"

if valor == ord("A") or valor == ord("E") or valor == ord("I") or valor == ord("O") or valor == ord("U"):
    salida = si

elif valor == ord("Á") or valor == ord("É") or valor == ord("Í") or valor == ord("Ó") or valor == ord("Ú") or valor == ord("Ü"):
    salida = si

else:
    salida = no    

# Salidas
print(salida)
