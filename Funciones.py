#Primero creamos un codigo y despues funciones
print("Presiona un numero y luego ENTER: ")
n1 = float(input())
print("Presiona otro numero y luego ENTER: ")
n2 = float(input())
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2
print("La suma es; ", suma)
print("La resta es; ", resta)
print("La multiplicacion es; ", multi)
print("La division es; ", divi)

def sumando_libros(libros):
  if libros >= 12:
    print("Los libros son menos")
  else:
    print("Los libros son mas")


def buscando_dinero(billetes):
  dinero = n1 + n2
  if n2 > n1:
    print("No hay dinero")
  else:
    print("si hay dinero")
    print(f"Hay {dinero + billetes} billetes!")
buscando_dinero(2)      
print(f"Sumando libros y dinero da {buscando_dinero(2)}")

sumando_libros(n1)

def activar_hora():
  print("hay que hacer la tarea")