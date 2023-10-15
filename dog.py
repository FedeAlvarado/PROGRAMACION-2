from mascota import *

class Dog(Mascota):

    def __init__(self, name: str , age: str) -> None:
        super().__init__(name,age)

        self.__peso = float(10)

#getter
    @property
    def peso(self) -> float:
        return self.__peso
#setter
    @peso.setter
    def peso(self, new_peso: float) -> None:
        self.__peso = new_peso






