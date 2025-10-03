import random
# El programa elige un numero entre 1 y 25
numero = random.randit (1, 100)
print ("Elige numero entre 1 y 100")
intentos = 0
adivinado = False 
while not adivinado:
  intento = int(input("tu mumero): "))
  intentos += 1
  if intento <numero:
    print ("es mas grande")
  elif intento > numero:
    print ("es mas pequeñp")
  else:
    print ("Correcto)", intentos, "intentos")
    adivinado = True 
