import vccrud, vcmisc, vclist

#Fromulario para Cargar un nuevo cliente, la función devuelve una lista con los datos del nuevo cliente
def formNewClient():
    print("╔"+ "═"*80 + "╗" )
    print("║"+ "{0:^80}".format("FORMULARIO PARA ALTA CLIENTE") + "║")
    print("╚" + "═"*80 + "╝")
    #Carga de los datos del cliente
    valido = False
    while not valido:
        dni = input("{0:>20}: ".format("DNI"))
        valido = dni.isnumeric() and len(dni) <= 8 and len(dni) >= 7
        if not valido:
            print("El Nro de documento debe ser numérico, de entre 7 y 8 dígitos. Ingrese nuevamente.")
    nom = input("{0:>20}: ".format("Nombre y Apellido"))
    dir = input("{0:>20}: ".format("Dirección"))
    tel = input("{0:>20}: ".format("Teléfono"))
    clients = vccrud.getAllClients()
    #Verifica que el DNI ingresado no pertenzca a un cliente ya existente
    dniexist = False
    for cli in clients:
        dniexist = dniexist or cli[1]==dni
    if dniexist:
        print("No se puede agregar el cliente, ya existe un cliente con el mismo DNI")
        vcmisc.esperar()
        return []
    else:
        conf = input("¿Está seguro de agregar a {0} como socio? (S/N): ".format(nom))
        if conf in ("S", "s"):
            return [str(int(clients[-1][0])+1), dni, nom, dir, tel]
        else:
            return []
    
# Formulario para editar un nuevo cliente existente
#El formulario devuelve una lista con los datos del cliente modificados
def formEditClient(cliCode):
    print("╔"+ "═"*80 + "╗")
    print("║"+ "{0:^80}".format("FORMULARIO PARA EDICION DEL CLIENTE:")+ "║")
    print("╚" + "═"*80 + "╝")
    vclist.fichaCliente(cliCode)
    print("{0:^80}".format("Ingrese los nuevos valores o..."))
    print("{0:^80}".format("presione ENTER para mantener los valores actuales"))
    print("═"*82)
    # Se ingresan los datos, si no se ingresa nada se asume que se quiere mantener el valor sin modificar
    valido = False
    while not valido:
        dni = input("{0:>20}: ".format("DNI"))
        valido = (dni.isnumeric() and len(dni) <= 8 and len(dni) >= 7) or dni ==""
        if not valido:
            print("El Nro de documento debe ser numérico, de entre 7 y 8 dígitos. Ingrese nuevamente.")
    nom = input("{0:>20}: ".format("Nombre y Apellido"))
    dir = input("{0:>20}: ".format("Dirección"))
    tel = input("{0:>20}: ".format("Teléfono"))
    clients = vccrud.getAllClients()
    dniexist = False
    for cli in clients:
        dniexist = dniexist or (cli[1]==dni and int(cli[0])!=cliCode)
    if dniexist:
        print("No se puede modificar el cliente, ya existe un cliente con el mismo DNI")
        vcmisc.esperar()
        return []
    else:
        oldClient = vccrud.getClient(cliCode)
        if not dni:
            dni = oldClient[1]
        if not nom:
            nom = oldClient[2]
        if not dir:
            dir = oldClient[3]
        if not tel:
            tel = oldClient[4]
        print("Está punto de reemplar información del socio nro.", cliCode)
        print("   Información Anterior: {0}, DNI: {1}, Dir: {2}, Tel: {3}.".format(oldClient[2], oldClient[1], oldClient[3],oldClient[4]))
        print("      Información nueva: {0}, DNI: {1}, Dir: {2}, Tel: {3}.".format(nom, dni, dir, tel))
        conf = input("¿Está seguro de reemplazar?(S/N): ")
        if conf in ("S", "s"):
            return [str(cliCode), dni, nom, dir, tel]
        else:
            return []

#Formulario para Cargar un nuevo videp, la función devuelve una lista con los datos del nuevo video
def formNewMovie():
    print("╔"+ "═"*80 + "╗")
    print("║" + "{0:^80}".format("FORMULARIO PARA ALTA PELICULA") + "║")
    print("╚" + "═"*80 + "╝")
    valid = False
    while not valid:
        ean = input("{0:>20}: ".format("EAN"))
        if not ean.isnumeric() or len(ean)!=13:
            print("El código EAN debe ser numérico y tener 13 dígitos, por favor verifique e ingrese nuevamente.")
        else:
            valid = True
    nom = input("{0:>20}: ".format("Nombre de Película"))
    gen = input("{0:>20}: ".format("Género"))
    movies = vccrud.getAllVideos()
    eanexist = False
    for mov in movies:
        eanexist = eanexist or mov[1]==ean
    if eanexist:
        print("No se puede agregar la película, ya existe una película con el mismo EAN")
        vcmisc.esperar()
        return []
    else:
        conf = input("¿Está seguro de agregar la película {0}? (S/N): ".format(nom))
        if conf in ("S", "s"):
            return [str(int(movies[-1][0])+1), ean, nom, gen, ""]
        else:
            return []

# Formulario para editar un nuevo cliente existente
#El formulario devuelve una lista con los datos del cliente modificado   
def formEditMovie(movCode):
    print(("╔"+ "═"*80 + "╗"))
    print("║" + "{0:^80}".format("FORMULARIO PARA EDICION DE PELICULAS") + "║")
    print(("╚"+ "═"*80 + "╝"))
    vclist.fichaPelicula(movCode)
    print("{0:^80}".format("Ingrese los nuevos valores o..."))
    print("{0:^80}".format("presione ENTER para mantener los valores actuales"))
    print("═"*82)
    valid = False
    while not valid:
        ean = input("{0:>20}: ".format("EAN"))
        if ean != "" and (not ean.isnumeric() or len(ean)!=13):
            print("El código EAN debe ser numérico y tener 13 dígitos, por favor verifique e ingrese nuevamente.")
        else:
            valid = True
    nom = input("{0:>20}: ".format("Nombre"))
    gen = input("{0:>20}: ".format("Género"))
    movies = vccrud.getAllVideos()
    eanexist = False
    for mov in movies:
        eanexist = eanexist or (mov[1]==ean and int(mov[0])!=movCode)
    if eanexist:
        print("No se puede modificar la película, ya existe una película con el mismo EAN")
        vcmisc.esperar()
        return []
    else:
        oldMovie = vccrud.getMovie(movCode)
        if not ean:
            ean = oldMovie[1]
        if not nom:
            nom = oldMovie[2]
        if not gen:
            gen = oldMovie[3]
        print("Está punto de reemplar información de la película nro.", movCode)
        print("   Información Anterior: {0}, EAN: {1}, Género: {2}.".format(oldMovie[2], oldMovie[1], oldMovie[3]))
        print("      Información nueva: {0}, EAN: {1}, Género: {2}.".format(nom, ean, gen))
        conf = input("¿Está seguro de reemplazar?(S/N): ")
        if conf in ("S", "s"):
            return [str(movCode), ean, nom, gen, oldMovie[4]]
        else:
            return []
