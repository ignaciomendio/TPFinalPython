# Obtiene todas las películas con sus datos, las carga en una lista de listas y la devuelve
def getAllVideos():
    videoList = []
    videoFile = open("movies.csv", "r")
    for video in videoFile.readlines():
        videoList.append(video.strip("\n").split(";"))
    videoFile.close()
    return videoList

# Obtiene todos los clientes con sus datos, , las carga en una lista de listas y la devuelve
def getAllClients():
    clientList = []
    clientFile = open("clientes.csv", "r")
    for client in clientFile.readlines():
        clientList.append(client.strip("\n").split(";"))
    clientFile.close()
    return clientList

# Obtiene en una lista los datos de la película cuyo código se pasa por parámetro
def getMovie(cod):
    for mov in getAllVideos():
        if int(mov[0])==cod:
            return mov
    return []

# Obtiene en una lista los datos del cliente cuyo código se pasa por parámetro
def getClient(soc):
    for cli in getAllClients():
        if int(cli[0])==soc:
            return cli
    return []

# Devuelve true si la pelicula cuyo código se psa por parámetro no está alquilada (no tiene el código del cliente)
def movAvailable(cod):
    return getMovie(cod)[4]==""

# lee todas las peliculas, reemplaza la que corresponda al código y vuelve a generar el archivo
def movUpdate(modificado):
    movies = getAllVideos()
    movFile = open("movies.csv", "w")
    for mov in movies:
        if modificado[0]==mov[0]:
            movFile.write(modificado[0]+";"+modificado[1]+";"+modificado[2]+";"+modificado[3]+";"+modificado[4]+"\n")
        else:
            movFile.write(mov[0]+";"+mov[1]+";"+mov[2]+";"+mov[3]+";"+mov[4]+"\n")
    movFile.close()
    return int(modificado[0])

# lee todas los clientes, reemplaza la que corresponda al código y vuelve a generar el archivo
def cliUpdate(modificado):
    clients = getAllClients()
    cliFile = open("clientes.csv", "w")
    for cli in clients:
        if modificado[0]==cli[0]:
            cliFile.write(modificado[0]+";"+modificado[1]+";"+modificado[2]+";"+modificado[3]+";"+modificado[4]+"\n")
        else:
            cliFile.write(cli[0]+";"+cli[1]+";"+cli[2]+";"+cli[3]+";"+cli[4]+"\n")
    cliFile.close()
    return int(modificado[0])

# Agrega la nueva pelicula pasada como una lista como parámetro al archivo
def movNew(nuevo):
    movFile = open("movies.csv", "a")
    movFile.write(nuevo[0]+";"+nuevo[1]+";"+nuevo[2]+";"+nuevo[3]+";"+nuevo[4]+"\n")
    movFile.close()
    return int(nuevo[0])

# Agrega el nuevo cliente pasado como una lista como parámetro al archivo
def cliNew(nuevo):
    cliFile = open("clientes.csv", "a")
    cliFile.write(nuevo[0]+";"+nuevo[1]+";"+nuevo[2]+";"+nuevo[3]+";"+nuevo[4]+"\n")
    cliFile.close()
    return int(nuevo[0])

# carga todos los videos a una lista, busca y elimina el que tiene el codigo pasado
#como parámetro y luego regenera el archivo
def movDelete(cod):
    movies = getAllVideos()
    movFile = open("movies.csv", "w")
    for mov in movies:
        if cod!=int(mov[0]):
            movFile.write(mov[0]+";"+mov[1]+";"+mov[2]+";"+mov[3]+";"+mov[4]+"\n")
    movFile.close()

# carga todos los clientes a una lista, busca y elimina el que tiene el codigo pasado
#como parámetro y luego regenera el archivo
def cliDelete(cod):
    clients = getAllClients()
    cliFile = open("clientes.csv", "w")
    for cli in clients:
        if cod!=int(cli[0]):
            cliFile.write(cli[0]+";"+cli[1]+";"+cli[2]+";"+cli[3]+";"+cli[4]+"\n")
    cliFile.close()