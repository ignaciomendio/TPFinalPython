import vccrud, vcquerys

def lisMovies(movies):
    print("-"*83)
    print("{0:^6}{1:^15}{2:^50}{3:^12}".format("Código", "EAN", "Nombre Película", "Género"))
    print("-"*83)
    for res in movies:
        print("{0:>6}{1:^15}{2:<50}{3:<12}".format(res[0], res[1], res[2], res[3]))
    print(len(movies), "registros listados")
    print("-"*83)
    print("\n")

def listClients(clients):
    print("-"*95)
    print("{0:^9}{1:^12}{2:^30}{3:^30}{4:^14}".format("N°Socio", "DNI", "Nombre y Apellido", "Dirección", "Teléfono"))
    print("-"*95)
    for cli in clients:
        print("{0:>9}{1:^12}{2:<30}{3:<30}{4:<14}".format(cli[0], cli[1], cli[2], cli[3], cli[4]))
    print(len(clients), "registros listados")
    print("-"*95)
    print("\n")

def fichaCliente(cod):
    client = vccrud.getClient(cod)
    print("-"*83)
    print("FICHA DE CLIENTE")
    print("-"*83)
    print("       Nro. de Socio: ", client[0])
    print("   Nombre y Apellido: ", client[2])
    print("                 DNI: ", client[1])
    print("           Dirección: ", client[3])
    print("            Telefono: ", client[4])
    print("-"*83)
    print("Películas rentadas Actualmente")
    lisMovies(vcquerys.rented(cod))

def fichaPelicula(cod):
    mov = vccrud.getMovie(cod)
    print("-"*83)
    print("FICHA DE PELICULA")
    print("-"*83)
    print("    Nro. de Película: ", mov[0])
    print("          Código EAN: ", mov[2])
    print("              Nombre: ", mov[1])
    print("              Género: ", mov[3])
    print("-"*83)
    if mov[4]:
        cli = vccrud.getClient(int(mov[4]))
        print("Esta película está Alquilada en este momento por {0}, Nro de Socio: {1}".format(cli[2], cli[0]))
    else:
        print("Esta película está DISPONIBLE paa Alquiler")
    
    
    