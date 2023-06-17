import vccrud

#devuelve la cantidad de videos que tiene alquilado el cliente cuyo codigo se pasa por parámetro
def qtyRented (cliCode):
    movies = vccrud.getAllVideos()
    qty = 0
    for mov in movies:
        if mov[4] != "" and cliCode == int(mov[4]):
            qty += 1
    return qty

#devuelve la lista de videos alquilados por el cliente que se pasa por código
def rented (cliCode):
    movies = vccrud.getAllVideos()
    ren = []
    for mov in movies:
        if mov[4] != "" and cliCode == int(mov[4]):
            ren.append(mov)
    return ren

