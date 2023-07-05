import vccrud, vclist

#Función para pedirle al usuario que seleccione una película, la funcion devuelve 
#el código de la película seleccionada o -1 si se canceló la búsqueda
#la función incluye buscadores para facilitar la ubicacion del código
def videoSearch():
    while True:
        print("Ingrese el código del video o:")
        print("   E: Para buscar por EAN")
        print("   N: Para buscar por Nombre")
        print("   X: Para Para cancelar y volver al menú") 
        op = input("Ingrese código de video o la opción deseada: ")
        if op == "e" or op == "E":
            ean = input("Ingrese el EAN (o parte de él) para Buscar: ")
            searchRes = list(filter(lambda vid: vid[1].find(ean)!=-1,vccrud.getAllVideos()))
            print("Resultados de búsqueda de {0} en EAN.\n".format(ean))
            vclist.lisMovies(searchRes)
        elif op == "n" or op == "N":
            nom = input("Ingrese el nombre de la película (o parte de él) para Buscar: ")
            searchRes = list(filter(lambda vid: vid[2].lower().find(nom.lower())!=-1,vccrud.getAllVideos()))
            print("Resultados de búsqueda de {0} en Nombre.\n".format(nom))
            vclist.lisMovies(searchRes)
        elif op == "x" or op == "X":
            return -1
        else:
            try:
                cod = int(op)
                if list(filter(lambda vid: int(vid[0])==cod,vccrud.getAllVideos())):
                    return(cod)
                else:
                    print("El código ingresado no pertenece a un video en el catálogo.\n")
            except ValueError:
                print("La opción ingresada no es un número, ni es una de las opciones admitidas. Reintente por favor. \n")

#Función para pedirle al usuario que seleccione un cliente, la funcion devuelve 
#el código de la película seleccionada o -1 si se canceló la búsqueda
#la función incluye buscadores para facilitar la ubicacion del código
def clientSearch():
    while True:
        print("Ingrese el número de socio o:")
        print("   D: Para buscar por DNI")
        print("   N: Para buscar por Nombre")
        print("   X: Para Para cancelar y volver al menú") 
        op = input("Ingrese número de socio o la opción deseada: ")
        if op == "D" or op == "d":
            dni = input("Ingrese el DNI para Buscar: ")
            searchRes = list(filter(lambda cli: cli[1]==dni,vccrud.getAllClients()))
            print("Resultados de búsqueda de {0} en DNI.\n".format(dni))
            print("-"*83)
            print("{0:^6}{1:^15}{2:^50}{3:^12}".format("Socio", "DNI", "Nombre y Apellido", "Teléfono"))
            print("-"*83)
            for res in searchRes:
                print("{0:>6}{1:^15}{2:<50}{3:<12}".format(res[0], res[1], res[2], res[4]))
            print("Encontradas", len(searchRes), "coincidencias")
            print("-"*83)
            print("\n")
        elif op == "n" or op == "N":
            nom = input("Ingrese el nombre del cliente (o parte de él) para Buscar: ")
            searchRes = list(filter(lambda cli: cli[2].lower().find(nom.lower())!=-1,vccrud.getAllClients()))
            print("Resultados de búsqueda de {0} en Nombre.\n".format(nom))
            print("-"*83)
            print("{0:^6}{1:^15}{2:^50}{3:^12}".format("Socio", "DNI", "Nombre y Apellido", "Teléfono"))
            print("-"*83)
            for res in searchRes:
                print("{0:>6}{1:^15}{2:<50}{3:<12}".format(res[0], res[1], res[2], res[4]))
            print("Encontradas", len(searchRes), "coincidencias")
            print("-"*83)
            print("\n")
        elif op == "x" or op == "X":
            return -1
        else:
            try:
                cod = int(op)
                if list(filter(lambda vid: int(vid[0])==cod,vccrud.getAllClients())):
                    return(cod)
                else:
                    print("El nro. de socio ingresado no pertenece a un cliente registrado.\n")
            except ValueError:
                print("La opción ingresada no es un número, ni es una de las opciones admitidas. Reintente por favor. \n")
