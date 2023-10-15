from datetime import date


class Usuario():
    def __init__(self, user_name: str,email:str,password:str) -> None:
        self.__user_name = user_name
        self.__state = True
        self.__email = email
        self.__password = password
        self.__name = None
        self.__surname = None
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
    
    @property
    def password(self):
        return self.__password
    
    @property
    def name(self):
        return self.__name
    
    @property
    def apellido(self):
        return self.__surname
    
    @property
    def email(self):
        return self.__email
    
    @property
    def user_name(self):
        return self.__user_name
    @property
    def fecha_alta(self):
        return self.__fecha_alta
    @property
    def fecha_baja(self):
        return self.__fecha_baja
        
    
    @password.setter
    def password(self,new_pass):
        self.__password  = new_pass

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @apellido.setter
    def surname(self, surname):
        self.__surname= surname

    @email.setter
    def email(self, email):
        self.__email = email

    @fecha_baja.setter
    def fecha_baja(self, fecha_baja):
        self.__fecha_baja= fecha_baja    

    def validar_credenciales(self, usuario:str, password: str) -> bool:
        return self.__user_name == usuario and self.__password == password
    
    def baja_usuario(self) -> None:
        self.__state= False
        self.__fecha_baja= date.today()

