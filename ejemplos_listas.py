marcas_autos=["ford","chevrolet","fiat"]
print(marcas_autos)
print(marcas_autos[2]) 

'''MISMAS POSICIONES DE C, ARRANCA EN 0 '''

mensaje=f"El auto que mas me gusta es {marcas_autos[0].title()}" #APLICO TITLE (QUE ES UN METODO), PORQUE ES UN STR

print(mensaje)

'''MODIFICACION DE ELEMENTOS'''

marcas_autos[1]="peugeot"

print(marcas_autos[1])

'''AGREGAR ELEMENTOS A UNA LISTA '''
#AL FINAL DE LA LISTA
marcas_autos.append("citroen")
mensaje=f"El auto que mas me gusta es {marcas_autos[3].title()}"
print(mensaje) 

#AL PRINCIPIO O EN EL MEDIO DE LA LISTA
marcas_autos.insert(0,"Honda")
mensaje=f"El auto que mas me gusta es {marcas_autos[0].title()}"
print(mensaje)

print(marcas_autos)

'''ELIMINAR ELEMENTOS Y LIMPIARLO DE LA MEMORIA'''

del marcas_autos[2]
print(marcas_autos)
print(marcas_autos[2])

'''---------------------'''

elemento_eliminado =  marcas_autos.pop() #SI LE PONES EL NUMERO SELECCIONA LA POSICION.
print(f"Se elimino correctamente el elemento {elemento_eliminado}") #OTRA FORMA ES REEMPLAZAR EL ELEMENTO ELIMINADO POR EL POP
print(f"Las marcas que quedan son {marcas_autos}")

'''REMOVEMOS UN ELEMENTO EN ESPECIAL'''

marcas_autos.remove("ford")

print(marcas_autos)
