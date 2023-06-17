import vcmenu, os, vcsearch, vccrud, vclist, vcquerys, vcforms, vcmisc


MAX_RENT = 3

salir = False
while not salir:
    os.system("cls")
    op = vcmenu.mainMenu()
    if op == "0": #Verificar disponibiliad de un titulo en particular
        movCode = vcsearch.videoSearch()
        if movCode != -1: #el usuario no canceló la busqueda
            movie = vccrud.getMovie(movCode)
            mensaje = "\nLa película: " + movie[2] + "Codigo:" + movie[0] + ", "
            if movie[4] == "":
                mensaje += "ESTA DISPONIBLE."
            else:
                mensaje += "NO ESTA DISPONIBLE, "
                cliente = vccrud.getClient(int(movie[4]))
                mensaje += " está alquilada por " + cliente[2] + ", Nro. de Socio: " + cliente[0] + ".\n"
            print(mensaje)
            vcmisc.esperar()
    elif op == "1": #Ingresar a Menu de alquiler
        subop = vcmenu.rentMenu()
        if subop == "L": #listar títulos disponibles
            vclist.lisMovies(list(filter(lambda mov: mov[4]=="", vccrud.getAllVideos())))
            vcmisc.esperar()
        elif subop == "R": #registrar alquiler
            movCode = vcsearch.videoSearch()
            if movCode != -1: #el usuario no canceló la busqueda
                if vccrud.movAvailable(movCode):
                    cliCode = vcsearch.clientSearch()
                    if cliCode != -1:#el usuario no cancelo tampoc la busqueda de cliente
                        rented = vcquerys.qtyRented(cliCode) 
                        if rented < MAX_RENT:
                            movie = vccrud.getMovie(movCode)
                            cliente = vccrud.getClient(cliCode)
                            conf=input("Confirma el alquiler de película {0} (código: {1}) al cliente {2} (Nro. socio: {3}), (S/N): ".format(movie[2], movie[0], cliente[2], cliente[0]))
                            if conf in ("s", "S"):
                                vccrud.movUpdate([movie[0], movie[1], movie[2], movie[3],str(cliCode)])
                        else:
                            print("El cliente ya alcanzó el límite de alquileres simultáneos, no se puede proceder con el alquiler")
                            vcmisc.esperar()
                else:
                    print("la película seleccionada no está disponible para alquiler")
                    vcmisc.esperar()
        elif subop == "D": #registrar devolucion
            movCode = vcsearch.videoSearch()
            if movCode != -1: #el usuario no canceló la busqueda
                if vccrud.movAvailable(movCode):
                    print("La pelicula seleccionada no está rentada")
                    vcmisc.esperar()
                else:
                    movie = vccrud.getMovie(movCode)
                    cliente = vccrud.getClient(int(movie[4]))
                    conf=input("Confirma la devolución de la película {0} (código: {1}) al cliente {2} (Nro. socio: {3}), (S/N): ".format(movie[2], movie[0], cliente[2], cliente[0]))
                    if conf in ("s", "S"):
                        vccrud.movUpdate([movie[0], movie[1], movie[2], movie[3],""])
                        print("Devolución registrada")
                        vcmisc.esperar()
                    else:
                        print("Devolución Cancelada")
                        vcmisc.esperar()
    elif op == "2": #Usuario selecciona Gestión de clientes
        subop = vcmenu.clientMenu()
        if subop == "A": #Usuario selecciona Alta de cliente
            newClient = vcforms.formNewClient()
            if newClient:
                print("Se ha agregado el nuevo cliente, Nro de Socio:",vccrud.cliNew(newClient))
                vcmisc.esperar()
        elif subop == "C": #Usuario selecciona consulta de cliente
            cliCode = vcsearch.clientSearch()
            if cliCode >= 0:
                vclist.fichaCliente(cliCode)
                vcmisc.esperar()
        elif subop == "M": #Usuario selecciona Modificacion de cliente
            cliCode = vcsearch.clientSearch()
            if cliCode >= 0:
                newClient = vcforms.formEditClient(cliCode)
                if newClient:
                    vccrud.cliUpdate(newClient)
        elif subop == "E": #Usuario selecciona Elimicación de cliente
            cliCode = vcsearch.clientSearch()
            if vcquerys.qtyRented(cliCode) > 0:
                print("El cliente no se puede eliminar, aún tiene películas sin devolver,")
                vcmisc.esperar()
            else:
                cli= vccrud.getClient(cliCode)
                conf = input("¿Está seguro de eliminar al cliente {0} (Nro de Socio: {1})?(S/N): ".format(cli[2], cli[0]))
                if conf in ("s", "S"):
                    vccrud.cliDelete(cliCode)
                    print("El cliente se ha eliminado")
                    vcmisc.esperar()
                else:
                    print("Eliminación Cancelada")
                    vcmisc.esperar()
    elif op == "3": #Usuario selecciona Gestión de películas
        subop = vcmenu.movieMenu()
        if subop == "A": #Usuario selecciona Alta de película
            newMov = vcforms.formNewMovie()
            if newMov:
                print("Se ha agregado la nueva película, Nro de película:",vccrud.movNew(newMov))
                vcmisc.esperar()
        elif subop == "C": #Usuario selecciona consulta de Película
            movCode = vcsearch.videoSearch()
            if movCode >= 0:
                vclist.fichaPelicula(movCode)
                vcmisc.esperar()
        elif subop == "M": #Usuario selecciona Modificacion de Película
            movCode = vcsearch.videoSearch()
            if movCode >= 0:
                newMov = vcforms.formEditMovie(movCode)
                if newMov:
                    vccrud.movUpdate(newMov)
        elif subop == "E": #Usuario selecciona Elimicación de Película
            movCode = vcsearch.videoSearch()
            if not vccrud.movAvailable(movCode):
                print("La pelicula no se puede eliminar, está alquilada.")
                vcmisc.esperar()
            else:
                mov= vccrud.getMovie(movCode)
                conf = input("¿Está seguro de eliminar la película: {0} (Nro de Socio: {1})?(S/N): ".format(mov[2], mov[0]))
                if conf in ("s", "S"):
                    vccrud.movDelete(movCode)
                    print("La Película se ha eliminado")
                    vcmisc.esperar()
                else:
                    print("Eliminación Cancelada")
                    vcmisc.esperar()
    else:
        salir = True
        print("Programa terminado.")