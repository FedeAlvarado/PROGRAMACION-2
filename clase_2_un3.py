#Clase
#Constructores
#Variables de instancia
#Variables de clase
#Metodo de instancia
#Metodos de clase
#Properties

class Automovil:

    __iva=0.21 #Variable de clase

    def __init__(self,marca,modelo,precio,nacionalidad='N/A'): # Constructor
        self.marca=marca  #Variable de instancia
        self.modelo=modelo
        self.precio=precio
        self.nacionalidad=nacionalidad

    def mostrar(self): #Metodo de instancia
        print(self.marca)
        print(self.modelo)
        print(self.precio)
        print(self.nacionalidad)

    @classmethod # Metodo de clase
    def mostrar_iva(cls):
        print(cls.__iva)

    @classmethod  # Metodo de clase
    def cambiar_iva(cls,iva_nuevo):
        __iva=iva_nuevo
        print(__iva)

    @property
    def precio_con_iva(self):
        precio_final=self.precio+self.precio*self.__iva
        return precio_final
        
automovil_fiat=Automovil("fiat","palio",10000,"Argentina") #Llamar al constructor
#print("Automovil Fiat")
#automovil_fiat.mostrar() 
#automovil_peugeot=Automovil("peugeot",'207',15000)
#print("Automovil Peugeot")
#automovil_peugeot.mostrar()
#print('iva viejo :')
#Automovil.mostrar_iva()
#print('Iva Nuevo')
#Automovil.cambiar_iva(0.25)
print(automovil_fiat.precio) # Atributo de instancia - precio
print(automovil_fiat.precio_con_iva) # Property precio con iva