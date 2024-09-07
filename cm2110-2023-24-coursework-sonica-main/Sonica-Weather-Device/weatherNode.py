#Imports for weather node
from sense_hat import SenseHat
import RPi.GPIO as GPIO
from Adafruit_IO import Client, RequestError, Data

#MQTT Imports
import paho.mqtt.client as mqttClient
import time
import ssl

def on_connect(client, userdata, flags, rc):
    
    if rc == 0:
        print("Connected to Broker")
        
        global Connected
        Connected = True
        
    else:
        print("Connection Failed")

Connected = False

broker_address = "soc-broker.rgu.ac.uk"
port = 8883
user_name = "sociot"
password = "s7ci7tRGU"

# set username and password
client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
client.username_pw_set("sociot", password="s7ci7tRGU")

# configure TLS connection
client.tls_set (cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set (False)

client.on_connect = on_connect
client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:
    time.sleep(0.1)   

#------- Main program --------
highPressure = "1022"
normalPressure = "1013"
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

ADAFRUIT_IO_USERNAME = "stuartiek"
ADAFRUIT_IO_KEY = "aio_Hhxu42f97gWUHDeZnBstULkjYp54"

sense = SenseHat()
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Asks user for devices locations
deviceLocation = input("Please input device location: ")

aio.create_data("location", Data(value=deviceLocation))

# Checks data input from soil moisture sensor and displays correct output for Adafruit dashboard
def callback(channel):
    time.sleep(5)
    if GPIO.input(channel):
        print("No Water")
        aio.create_data("soil-moisture", Data(value="No water"))
        client.publish("sonica/water","No water", retain=True) 
    else:
        aio.create_data("soil-moisture", Data(value="Water Detected"))
        print("Water detected")
        client.publish("sonica/water","Water detected", retain=True) 
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
try:
    while True:
        #Gets weather data from senseHat
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        #Formats weather data to 2 decimal places 
        roundPressure = format(pressure, ".2f")
        humidity_value = format(humidity, ".2f")
        roundTemp = format(temp, ".2f")
        
        #Pushs weather data to Adafruit dashboard
        aio.create_data("temperature", Data(value=roundTemp))
        aio.create_data("humidity", Data(value=humidity_value))
        aio.create_data("pressure", Data(value=roundPressure))
        
        
        #Checks pressure level and displays the correct text dependent on pressure level
        if roundPressure >= highPressure:  
            aio.create_data("pressure-warning", Data(value="High Pressure"))
        elif roundPressure >= normalPressure:
            aio.create_data("pressure-warning", Data(value="Normal Pressure"))
        else:
            aio.create_data("pressure-warning", Data(value="Low Pressure"))
        
        
        time.sleep(10)
        
        
        
except KeyboardInterrupt:
    exit()
