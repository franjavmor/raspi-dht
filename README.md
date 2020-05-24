# Raspberry Pi + DHT22

## Ambiente de prueba
 - Raspberry Pi 3 B+
 - Raspbian 4.19
 - Sensor DHT22

## Librería CircuitPython
Fuente: [Installing CircuitPython Libraries on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

### Instalación
    sudo apt-get update
    sudo apt-get upgrade
    sudo pip3 install --upgrade setuptools

    # If above doesn't work try
    sudo apt-get install python3-pip

    # Enable I2C
    # Enable SPI

    # Check I2C and SPI
    ls /dev/i2c* /dev/spi*

    pip3 install RPI.GPIO
    pip3 install adafruit-blinka

## Librería CircuitPython DHT
Fuente: [Installing the CircuitPython-DHT Library](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup)

### Instalación
    pip3 install adafruit-circuitpython-dht
    sudo apt-get install libgpiod2

## Script de prueba

Script `raspi-dht.py`.

    import time
    import board
    import adafruit_dht

    # Especifico el PIN15 (GPIO22)
    dhtDevice = adafruit_dht.DHT22(board.D22)

    # Obtengo los valores de temperatura y humedad
    temperatura = dhtDevice.temperature
    humedad = dhtDevice.humidity

    temperatura = round(temperatura,2)
    humedad = round(humedad,2)

    print ('Temperatura: ',temperatura,', Humedad: ',humedad)

Ejecutar: `python3 raspi-dht.py`

Output:

    pi@raspberry:~/Scripts $ python3 raspi-dht.py
    Temperatura:  19.8 , Humedad:  63.1
