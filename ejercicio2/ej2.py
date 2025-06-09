from ListaORDENADA_parcial  import *
import random

lista = ListaOrdenada()

acombinar = ['CUATRO', 'CINCO', 'SEIS', 'NUEVE', 'DOS', 'CERO', 'TRES', 'SIETE' 'UNO', 'OCHO']

for i in acombinar:
    lista.agregar(i)
    
lista.ver()
print()
for i in range(10):
    nums = random.randint(100,200)
    lista.agregar((str(nums))) 
    
lista.ver()

print(f"\nEl largo de la lista es: {lista.tamano()}\n")

print("Nro     Elementos")
for i in range(lista.tamano()):
    print(f"{i}         {lista.metodo_nuevo(i)}")

numNuevo = random.randint(0,lista.tamano())
for j in range(1):
    print(f"en el indice {numNuevo} se encuentra el elemento {lista.metodo_nuevo(j)}")
