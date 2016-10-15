from math import pi


class Coordinate:
    def __init__(self,lat,lon):
        self.lon = lon
        self.lat = lat

    @staticmethod
    def _deg2rad(degree):
        return degree * (pi / 180)

    def latAsRad(self):
        return self._deg2rad(self.lat)

    def lonAsRad(self):
        return self._deg2rad(self.lon)
