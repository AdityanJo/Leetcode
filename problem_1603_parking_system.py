class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_spots=big
        self.medium_spots=medium
        self.small_spots=small
        self.big=0
        self.medium=0
        self.small=0

    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>=self.big_spots:
                return False
            else:
                self.big+=1
        elif carType==2:
            if self.medium>=self.medium_spots:
                return False
            else:
                self.medium+=1
        elif carType==3:
            if self.small>=self.small_spots:
                return False
            else:
                self.small+=1
        else:
            return False
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
