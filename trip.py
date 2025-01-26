def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Toronto " == city:
        return 183
    elif "Brampton" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40*days