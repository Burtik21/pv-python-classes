class Bottle:

    def __init__(self, capacity:float, volume:float, opened:bool  ):
        if type(capacity) != float or type(volume) != float:
            raise TypeError("capacity must be float")



        self.check_capacity()
        self.check_volume()


        self.opened = opened
        self.capacity = capacity
        self.volume = 0



    def check_bottle_opened(self):
        if self.opened:
            return True
        else:
            raise ValueError("lahev je zavrena")

    def open_close_bottle(self, opened:bool):
        self.opened = opened

    def bottle_empty(self):
        self.check_bottle_opened()
        self.volume = 0

    def get_volume(self):
        return self.volume

    def set_volume(self, set_volume:float):
        self.check_bottle_opened()
        if set_volume > 100:
            self.volume = set_volume / 1000

        self.check_volume()




    def check_capacity(self):
        if 10 < self.capacity < 0.1:
            raise ValueError("capacity must be 0.1 - 10")

    def check_volume(self):
        if self.volume > self.capacity:
            raise ValueError("volume must be less than capacity")








