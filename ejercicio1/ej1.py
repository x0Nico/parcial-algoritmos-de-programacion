from tda_parcial import *
import random

m = Cola()

print("Turnos\n")

for i in range(10):
    m.encolar(i)
    print(f"Turno {i} otorgado")
    
print()
m.mostrar()

cajas = ['a','b','c']

print("\nSistema de Atenciòn al Cliente\n")

for j in range(10):
    m.desencolar()
    print(f"Nùmero {j} Caja {random.choice(cajas)}")
    
print()
m.mostrar()

