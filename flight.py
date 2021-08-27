class Flight:
    def __init__(self,flightNumber,origin,destination,distance):

        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.passengers = []
        
    def __str__(self):
        return f'Flight number {self.flightNumber} from {self.origin.code} to {self.destination.code} with distance {self.distance}km.'
    
    def addPassenger(self,newP):
        self.passengers.append(newP)
        newP.flights.append(self)