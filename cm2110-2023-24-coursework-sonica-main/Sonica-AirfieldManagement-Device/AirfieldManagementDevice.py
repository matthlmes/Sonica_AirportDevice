import RPi.GPIO as GPIO
import time
from CourseworkFile import ledOn
from sense_hat import SenseHat
from Adafruit_IO import Client, RequestError, Data


#set-up mqtt
import paho.mqtt.client as mqttClient
import ssl

def on_connect(client, userdata, flags, rc):
    if rc ==0:
        print("connected to broker")
        
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

client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
client.username_pw_set("sociot", password = "s7ci7tRGU")

client.tls_set (cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set (False)

client.on_connect = on_connect
client.connect(broker_address, port=port)

client.on_message = on_message


client.loop_start()

while Connected != True:
    time.sleep(0.1)


client.subscribe("sonica/water")



#setup sensors
sensor = 4
sensortwo = 17
sensorthree = 27
gate01 = True
gate02 = True
gates = ""
sense = SenseHat()

#setup sensehat colors
red = (255,0,0)
green = (0,255,0)


#setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(sensortwo,GPIO.IN)
GPIO.setup(sensorthree,GPIO.IN)

# Connect adafruit 
ADAFRUIT_IO_USERNAME = "stuartiek"
ADAFRUIT_IO_KEY = "aio_Hhxu42f97gWUHDeZnBstULkjYp54"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#main program
try:
    while True:
        if GPIO.input(sensor):
            print("motion 1 detected")
            aio.create_data("runway-1", Data(value="Plane on Runway"))
            sense.clear(red)
            while GPIO.input(sensor):
                time.sleep(10)
                
                
        else:
            print("motion 1 not detected")
            aio.create_data("runway-1", Data(value="Runway clear for approach"))
            sense.clear(green)
            
            time.sleep(2)
             
        
        if GPIO.input(sensortwo):
            if gate01 == True:
                print("gate 1 occupied")
                aio.create_data("gate-1", Data(value="Gate in use"))
                gate01 = not gate01
                gates = str(gate01) + "," + str(gate02)
                continue
            if gate01 == False:
                print("Plane leaving gate 1")
                aio.create_data("gate-1", Data(value="Gate Free"))
                gate01 = not gate01
                gates = str(gate01) + "," + str(gate02)
            time.sleep(5)
            
                 
                
        else:
            print("gate 1 nmo")
            time.sleep(1)
            
        if GPIO.input(sensorthree):
            if gate02 == True:
                print("gate 2 occupied")
                aio.create_data("gate-2", Data(value="Gate in use"))
                gate02 = not gate02
                gates = str(gate01) + "," + str(gate02)
                continue
            if gate02 == False:
                print("Plane leaving gate 2")
                aio.create_data("gate-2", Data(value="Gate Free"))
                gate02 = not gate02
                gates = str(gate01) + "," + str(gate02)
            time.sleep(5)
            
                 
                
        else:
            print("gate2 nomo")
            print(gates)
            client.publish("sonica/gate", gates, retain = True)
            time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
