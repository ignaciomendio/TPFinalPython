def getAllVideos():
    videoList = []
    videoFile = open("movies.csv", "r")
    for video in videoFile.readlines():
        videoList.append(video.strip("\n").split(";"))
    videoFile.close()
    return videoList

def getAllClients():
    clientList = []
    clientFile = open("clientes.csv", "r")
    for client in clientFile.readlines():
        clientList.append(client.strip("\n").split(";"))
    clientFile.close()
    return clientList

def getMovie(cod):
    for mov in getAllVideos():
        if int(mov[0])==cod:
            return mov
    return []

def getClient(soc):
    for cli in getAllClients():
        if int(cli[0])==soc:
            return cli
    return []

def movAvailable(cod):
    return getMovie(cod)[4]==""

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

def movNew(nuevo):
    movFile = open("movies.csv", "a")
    movFile.write(nuevo[0]+";"+nuevo[1]+";"+nuevo[2]+";"+nuevo[3]+";"+nuevo[4]+"\n")
    movFile.close()
    return int(nuevo[0])

def cliNew(nuevo):
    cliFile = open("clientes.csv", "a")
    cliFile.write(nuevo[0]+";"+nuevo[1]+";"+nuevo[2]+";"+nuevo[3]+";"+nuevo[4]+"\n")
    cliFile.close()
    return int(nuevo[0])

def movDelete(cod):
    movies = getAllVideos()
    movFile = open("movies.csv", "w")
    for mov in movies:
        if cod!=int(mov[0]):
            movFile.write(mov[0]+";"+mov[1]+";"+mov[2]+";"+mov[3]+";"+mov[4]+"\n")
    movFile.close()

def cliDelete(cod):
    clients = getAllClients()
    cliFile = open("clientes.csv", "w")
    for cli in clients:
        if cod!=int(cli[0]):
            cliFile.write(cli[0]+";"+cli[1]+";"+cli[2]+";"+cli[3]+";"+cli[4]+"\n")
    cliFile.close()