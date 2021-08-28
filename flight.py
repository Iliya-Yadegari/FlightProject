class Flight:
    def __init__(self,flightNumber,origin,destination,distance):

        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.passengers = []
        self.airPlane = ''
        
    def __str__(self):
        return f'Flight number {self.flightNumber} from {self.origin.code} to {self.destination.code} with distance {self.distance}km.'
    
    def addPassenger(self,newP):
        self.passengers.append(newP)
        newP.flights.append(self)
    
    def setPlane(self,airPlaneObj):
        if airPlaneObj.airplanRange >= self.distance:
            self.airPlane = airPlaneObj
            return True
        else:
            return False
    
    def overBooked(self):
        numberOfPass = len(self.passengers)
        numberOfSeats = self.airPlane.seats
        
        if numberOfPass > numberOfSeats:
            return numberOfPass - numberOfSeats
        else:
            return 0
    
    def isInternational(self):
        if self.origin.country == self.destination.country:
            
            return False
        
        else:
            
            return True
    
    def noPassports(self):
        
        noPass = []
        
        for p in self.passengers:
            if p.passportNumber == 0:
                noPass.append(p)
        
        return noPass