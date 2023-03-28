class Garage:
    def __init__(self):
        self.cars=[]

    def __len__(self):
        return len(self.cars)   

    def __getitem__(self,indx):
        return self.cars[indx]


my_car=Garage()
my_car.cars.append('BMW')
my_car.cars.append('Ferari')
print(len(my_car))
print(my_car[0])        