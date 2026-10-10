def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start_zone = round((luminosity ** 0.5) * 0.95, 2)
    end_zone = round((luminosity ** 0.5) * 1.37,2)
    distances = [start_zone,end_zone]
    return distances