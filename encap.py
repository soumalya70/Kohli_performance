class Sensor():
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.__record_date="2023-01-10"
        self.__version="0.012"

    def get_record_date(self):
        print(f"The date is {self.__record_date}")
    def get_version(self):
        print(f"The version is {self.__version}")
    def set_version(self,version):
        self.__version=version
        print(f"The updated version is {self.__version}")
    
sensor1=Sensor(
    name="Sensor",location="haldia"
)
print(sensor1.name)
print(sensor1.location)
sensor1.get_record_date()
sensor1.get_version()
sensor1.set_version(version="0.312")
sensor1.get_version

# print(sensor1._record_date)
# print(sensor1._version)
