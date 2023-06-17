import vccrud

def qtyRented (cliCode):
    movies = vccrud.getAllVideos()
    qty = 0
    for mov in movies:
        if mov[4] != "" and cliCode == int(mov[4]):
            qty += 1
    return qty

def rented (cliCode):
    movies = vccrud.getAllVideos()
    ren = []
    for mov in movies:
        if mov[4] != "" and cliCode == int(mov[4]):
            ren.append(mov)
    return ren

