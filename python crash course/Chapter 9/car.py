class Car:
    
    #object
    def __init__(self,make,model,year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    #method
    def drive(self):
        print("The "+self.make+" is driving")

    def stop(self):
        print("The "+self.make+" is stopping")    


    