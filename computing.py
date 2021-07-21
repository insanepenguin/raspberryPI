from sense_hat import SenseHat
import threading
import time

sense = SenseHat()

humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

# alternatives
print(sense.humidity)

sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

# alternatives
print(sense.temp)
print(sense.temperature)

temp = sense.get_temperature_from_humidity()
print("Temperature: %s C" % temp)

#temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)