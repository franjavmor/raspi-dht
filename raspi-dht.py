import time
import board
import adafruit_dht

# Especifico el PIN 15 (GPIO22)
dhtDevice = adafruit_dht.DHT22(board.D22)

# Obtengo los valores de temperatura y humedad
temperatura = dhtDevice.temperature
humedad = dhtDevice.humidity

temperatura = round(temperatura,2)
humedad = round(humedad,2)

print ('Temperatura: ',temperatura,', Humedad: ',humedad)
