from math import sin, cos, atan2, sqrt
from Distance.Coordinate import Coordinate


def getDistanceFromLatLonInKm(coordinate1: Coordinate, coordinate2: Coordinate):
    """
    Calculates the distance between two Coordinates in km

    Earth's radius from https://rechneronline.de/earth-radius/

    Haversine formula from:
    http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula


    :param coordinate1: one coordinate
    :param coordinate2: other coordinate
    :return: distance in km
    """
    R = 6375.51  # Radius of the earth in km at lat -23.5505199 and sea height of 763m, calculated at

    dLat = coordinate2.latAsRad() - coordinate1.latAsRad()

    dLon = coordinate2.lonAsRad() - coordinate1.lonAsRad()

    a1 = sin(dLat / 2) * sin(dLat * 2)

    a2 = cos(coordinate1.latAsRad()) * cos(coordinate2.latAsRad()) * sin(dLon / 2) * sin(dLon / 2)

    a = a1 + a2

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
