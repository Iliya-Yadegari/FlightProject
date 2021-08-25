import airplane as apn

class Flight:
    def __init__(self,flightNumber,origin,destination,distance):
        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.distance = distance
        
    def __str__(self):
        return f'Flight number {self.flightNumber} from {apn.self.origin} to {apn.self.destination} with distance {self.distance}km.'