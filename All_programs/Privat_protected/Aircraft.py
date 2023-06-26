class Aircraft:
    def __init__(self, model, mass, speed, top):
        number = (int, float)
        if not isinstance(model, str) and not (type(mass) in (int, float)) and not mass > 0:
            self._model = model
            self._mass = mass
            self._speed = speed
            self._top = top


class PassengerAircraft:
    def __init__(self, model, mass, speed, top, chairs):
        pass


class WarPlane:
    def __init__(self, model, mass, speed, top, weapons):
        pass




