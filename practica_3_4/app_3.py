from usuario import *  

fedito = Usuario("FedeCapo","Fede@fede.com", "ElFede")
    
print(fedito.user_name)
print(fedito.email)

pepe = Usuario("pepito123", "asdsad","elfede")

pepe.nombre = "Pepito"
print(pepe.nombre)
pepe.email = "safdasf"
print(pepe.email)

pepe.password = "1234"

print(pepe.validar_credenciales("pepito123", "12"))

#print(pepe.state)
print(pepe.fecha_alta)
pepe.baja_usuario()
#print(pepe.state)
print(pepe.fecha_baja)

import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Imprimir la fecha y hora actual
print(fecha_hora_actual)
        