class Flight:
    def __init__(self,flightNumber,origin,destination,distance,passengers):

        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.passengers = []
        
    def __str__(self):
        return f'Flight number {self.flightNumber} from YYZ to FRA with distance {self.distance}km.'
    
    def addPassenger(self,p):
        self.passengers.append(p)