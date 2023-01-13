from mysensors import Accelometer,Gps,Gyro
import numpy as np
acc=Accelometer(
    name="Accelometer",
    location="Chennai",
    record_date="2023-01-10",
)
gyro=Gyro(
    name="Gyro",
    location="Chennai",
    record_date="2023-01-10",
)
gps=Gps(
    name="GPS",
    location="Chennai",
    record_date="2023-01-10",
    brand="espressfi"
)



#get all the dummy data
time=np.arange(10)
acc_data=np.random.randint(-10,10,10)
gyro_data=np.random.randint(-15,15,10)
gps_data=np.random.randint(-12,12,10)

#add data to the instences
print(acc.name)
print(acc.location)
print(acc.record_date)
acc.add_data(
    data=acc_data,
    time=time
)
print(gyro.name)
print(gyro.location)
print(gyro.record_date)
gyro.add_data(
    data=gyro_data,
    time=time
)
print(gps.name)
print(gps.location)
print(gps.record_date)
gps.add_data(
    data=gps_data,
    time=time
)