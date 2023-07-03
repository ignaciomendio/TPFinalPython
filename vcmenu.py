import os

ANCHO_MENU = 40

def mainMenu():
    while True:
        os.system("cls")
        print("╔"+ "═"*(ANCHO_MENU) + "╗" )
        print("║"+"MENU PRINCIPAL VIDEOCLUB".center(ANCHO_MENU-2)+"  ║")
        print("╠"*1 + "═"*(ANCHO_MENU - 1 ) + "═╣"*1)
        print("║"+"   0: Consulta de disponibilidad      "+"  ║")
        print("║"+"   1: Alquiler de Película            "+"  ║")
        print("║"+"   2: Gestión de Clientes             "+"  ║")
        print("║"+"   3: Gestión de Películas            "+"  ║")
        print("║"+"   X: Salir del Programa              "+"  ║")
        print("╚" + "═"*(ANCHO_MENU - 1) + "═╝")
        op = input(" Ingresar la opción deseada>> ")
        print("\n")
        if op in ("0", "1", "2", "3", "X", "x"):
            return op.upper()
        
def rentMenu():
    while True:
        os.system("cls")
        print("╔"+ "═"*(ANCHO_MENU) + "╗")
        print("║"+"MENU DE ALQUILER DE PELICULAS".center(ANCHO_MENU-2)+"  ║")
        print("╠"*1 + "═"*(ANCHO_MENU - 1 ) + "═╣"*1)
        print("║"+"   L: Listar títulos disponibles      "+"  ║")
        print("║"+"   R: Registrar Alquiler              "+"  ║")
        print("║"+"   D: Registrar devolución            "+"  ║")
        print("║"+"   X: Salir al menú Principal         "+"  ║")
        print("╚" + "═"*(ANCHO_MENU - 1) + "═╝")
        op = input(" Ingresar la opción deseada>> ")
        if op in ("L", "R", "D", "X", "l", "r", "d", "x"):
            return op.upper()

def clientMenu():
    while True:
        os.system("cls")
        print("╔"+ "═"*(ANCHO_MENU) + "╗")
        print("║"+"MENU DE GESTION DE CLIENTES".center(ANCHO_MENU-2)+"  ║")
        print("╠"*1 + "═"*(ANCHO_MENU - 1 ) + "═╣"*1)
        print("║"+"   A: Alta de Cliente                 "+"  ║")
        print("║"+"   C: Consulta estado de cliente      "+"  ║")
        print("║"+"   M: Modificar datos de cliente      "+"  ║")
        print("║"+"   E: Eliminar cliente                "+"  ║")
        print("║"+"   X: Salir al menú Principal         "+"  ║")
        print("╚" + "═"*(ANCHO_MENU - 1) + "═╝")
        op = input(" Ingresar la opción deseada>> ")
        if op in ("A", "C", "M", "E", "X", "a", "c", "m", "e", "x"):
            return op.upper()
        
def movieMenu():
    while True:
        os.system("cls")
        print("╔"+ "═"*(ANCHO_MENU) + "╗")
        print("║"+"MENU DE GESTION DE PELICULAS".center(ANCHO_MENU-2)+"  ║")
        print("╠"*1 + "═"*(ANCHO_MENU - 1 ) + "═╣"*1)
        print("║"+"   A: Alta de película                "+"  ║")
        print("║"+"   C: Consulta estado de película     "+"  ║")
        print("║"+"   M: Modificar datos de película     "+"  ║")
        print("║"+"   E: Eliminar película               "+"  ║")
        print("║"+"   X: Salir al menú Principal         "+"  ║")
        print("╚" + "═"*(ANCHO_MENU - 1) + "═╝")
        op = input(" Ingresar la opción deseada>> ")
        if op in ("A", "C", "M", "E", "X", "a", "c", "m", "e", "x"):
            return op.upper()
        
