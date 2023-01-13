from mainsensor import Sensor
class Accelometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")
class Gyro(Accelometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")
class Gps(Sensor):
    def __init__(self, name, location, record_date,brand):
        super().__init__(name,location,record_date)
        self.brand=brand