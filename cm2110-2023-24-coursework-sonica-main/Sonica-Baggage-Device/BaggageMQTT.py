#MQTT Imports
import paho.mqtt.client as mqttClient
import time
import ssl

#Baggage Imports
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import MotionSensor
from Adafruit_IO import Client, RequestError, Data

#------------- MQTT Connection -------------------
def on_connect(client, userdata, flags, rc):
    
    if rc == 0:
        print("Connected to Broker")
        
        global Connected
        Connected = True
        
    else:
        print("Connection Failed")
        
def on_message(client, userdata, message):
    global payload
    payload = str(message.payload.decode("utf-8"))
    print(payload)

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

#Attaching functions to callbacks
client.on_connect = on_connect
client.on_message = on_message


client.connect(broker_address, port=port)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
    
client.subscribe("sonica/gate")

#------------- Baggage Device --------------------
#AdaFruit Details
ADAFRUIT_TO_KEY = "aio_Hhxu42f97gWUHDeZnBstULkjYp54"
ADAFRUIT_TO_USERNAME = "stuartiek"

aio = Client(ADAFRUIT_TO_USERNAME, ADAFRUIT_TO_KEY)
pir = MotionSensor(4)
reader = SimpleMFRC522()

#Assigning whether a plane is at a gate
Gate1Plane = payload.split(',')[0]
Gate2Plane = payload.split(',')[1]

#Checks if at least one of the gates has a Plane
while Gate1Plane == "False" or Gate2Plane == "False":
    pir.wait_for_motion()
    try:
        print("Scan Bag")
        id, text = reader.read()        #Reads RFID tag
        print(text)
        
        aio.create_data("baggage", Data(value=text))        #Sends bag scan data to Adafruit

        if text.strip() == "Gate 1" and Gate1Plane == 'False':
            print("Sending to Gate 1 Plane Area")
        elif text.strip() == "Gate 1" and Gate1Plane == 'True':
            print("Sending to Gate 1 Baggage Hold")
        elif text.strip() == "Gate 2" and Gate2Plane == 'False':
            print("Sending to Gate 2 Plane Area")
        elif text.strip() == "Gate 2" and Gate2Plane == 'True':
            print("Sending to Gate 2 Baggage Hold")
        else:
            print("Error calling for assistance")
            
    finally:
        pir.wait_for_no_motion()
        print("No Motion - Start Conveyor")
