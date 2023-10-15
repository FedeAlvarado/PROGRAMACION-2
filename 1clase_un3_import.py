from dog import *
from cat import *


#name = input("pone el nombre: ")
#edad = int(input("cuantos años tiene: "))
#mascota_1 = Dog(name,edad)
mascota = Dog("Thelma",15)
#mascota_1.comer()
#mascota_1.comer()


mascota.set_age(5)
print(mascota.get_age())

mascota.peso= input("Ingrese el peso de la mascota: ")
print(mascota.peso)


#-----------------------------------------------------------
#HERENCIA

mascota = Gato("Henry",205)
print(mascota.name)
print(mascota.age)
