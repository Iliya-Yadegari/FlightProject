class Passenger:
    def __init__(self,name,passportNumber):
        self.name = name
        self.passportNumber = passportNumber
        self.flights = []
    
    def calculatePoints(self):
        
        p = 0
        
        for f in self.flights:
            if f.origin.country == f.destination.country:
                
                p += 1
                
            
            else:
                
                p += 3
        
        return p
