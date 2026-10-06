class parkingSpace:

    def __init__(self , occupied):
        self.occupied = occupied

    def park(self):
        self.occupied=True

    def leave(self):
        self.occupied=False

    def is_available(self):
        return not self.occupied
 
class ParkingLot:

    def __init__(self , spaces):
        self.spaces = spaces

    def park_car(self , row , col):
        if self.spaces[row][col].is_available():
            self.spaces[row][col].park()
        else:
             print("this parking space is already occupued.")

    def remove_car(self , row , col):
        self.spaces[row][col].leave()

    def available_spaces(self):
        count = 0
        for row in self.spaces:
            for space in row:
                if space.is_available():
                    count+=1
        return count


