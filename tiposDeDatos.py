'''
Formateo de strings: Se denomina formateo de strings a la
posibilidad de introducir variables dentro de un string.
nombre = “Ezequiel”
precio = 12.50
descuento = 0.8
comida = “lasagna”
“{} debe pagar ${}”.format(nombre,precio)
# Ezequiel debe pagar $12.50
“{} debe pagar ${}”.format(nombre,precio*descuento)
# Ezequiel debe pagar $10.00
“{} debe pagar ${}”.format(precio=precio, nombre=”Bob)
# Bob debe pagar $12.50 (En este caso no importa el orden)
Formateo de strings con f-Strings:
f’{nombre} quiere comer {comida}’
#Ezequiel quiere comer lasagna
'''
nombre = "Ezequiel"
precio = 12.50
descuento = 0.8
comida = "lasagna"

print("{} quiere comer alta {}",format(nombre,comida)) 
