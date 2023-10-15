list_socio = [{'nombre': '', 'numero_socio': int, 'deportes': [], 'edad': int}]
import deportes

def nuevo_socio()-> dict:
    soc={}

    nombre = input("ingrese el nombre")
    numero_socio = input("ingrese numero de socio")
    while True:
        edad_str = input("Ingrese la edad: ")
        if edad_str.isnumeric():
            edad = int(edad_str)
            if edad < 30:
                soc['nombre'] = nombre
                soc['numero_socio'] = numero_socio
                soc['edad'] = edad
                soc['deportes'] = []
                return soc
            else:
                print("La edad debe ser menor a 30 años.")
        else:
            print("La edad debe ser un número entero válido.") 

def agregar_deporte(numero: int ):
    socios = [socio for socio in list_socio if socio['numero_socio'] == numero]

    if not socios:
        print("El socio con el número {} no existe.".format(numero))
        return

    socio = socios[0]  # Obtén el primer socio de la lista (debería ser único)
    deportes.agregar_deporte(socio)
    return None

def ordenar_socios_por_deportes():
    # Ordena la lista de socios en función de la cantidad de deportes (de mayor a menor)
    socios_ordenados = sorted(list_socio, key=lambda x: len(x['deportes']), reverse=True)
    return socios_ordenados
respuesta = True
while respuesta:
    print(
        ''' Ingrese:
        1: Nuevo Empleado
        2: Sumar falta Empleado
        3: Liquidar Salarios
        4: Salir
        '''
    )

    opt = int(input("Opción: "))

    if opt == 1:
        list_socio.append(nuevo_socio())
        
    elif opt == 2:
        numero_s= input("ingrese el numero del socio para buscarlo: ")
        agregar_deporte(numero_s)
        
    elif opt == 3: 
        socios_ordenados = ordenar_socios_por_deportes()
        for socio in socios_ordenados:
           print("Nombre: " , socio['nombre'] , "Número de Socio: " , socio['numero_socio'] , "Cantidad de Deportes: " , str(len(socio['deportes'])))
    elif opt == 4: 
        respuesta = False
    else: 
        print("Error, ingrese una opción correcta.")


print("Hasta luego!.")
