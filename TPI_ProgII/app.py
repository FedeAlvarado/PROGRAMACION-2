from usuario import *

def menu_principal():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_profesor():
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3 - Volver al menu principal")

def menu_alumno():
    print("1 - Matricularse a un curso")
    print("2 - Ver curso")
    print("3 - Volver al menu principal")

while True:
    menu_principal()
    opt = input("Ingrese una opción: ")
    if opt == "1":
        pass
    if opt == "2":
        pass
    if opt == "3":
        pass
    if opt == "4":
        print("Saludos!.")
        break