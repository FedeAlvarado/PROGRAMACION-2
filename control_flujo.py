variable=5

if variable>10:
    print("Esta variable es mayor a 10")
else:
    print("La variable es menor a 10")

if variable % 2 == 0:
    print("El valor es par")
elif variable==10:
    print("La variable es 10")  #ELIF
else:
    print("Es menor a 10")

edad=26

mayor_de_edad= "Si" if edad >= 18 else "No" #AL SI O AL NO, LE PODES ASIGNAR EL VALOR QUE VOS QUIERAS

print(mayor_de_edad)

#BUCLE FOR

animales=["perro","gato","loro"]

for animal in animales:
    print(f"{animal} es un zoo")

#FUNCION ENUMERATE

for indice,animales in enumerate(animales):
    print(f"{indice} - {animales}")


#WHILE

x=0
y=0

while x<4:
    print(x)
    x+=1
while True:
    y+=1
    if y>0:  
        print(y)
        break

try:
    a=1/0
except ZeroDivisionError as exception:
    print("Error")