def has_exoplanet(readings):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    levels = range(36)
    star_map = dict(zip(chars,levels))
    numerical_readings = []
    for char in readings:
        numerical_readings.append(star_map[char])
    threshold = (sum(numerical_readings)/len(numerical_readings)) * 0.8
    if min(numerical_readings) <= threshold:
        return True
    else:
        return False