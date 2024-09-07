Third Party Libraries / Software:

    Adafruit_IO: "from Adafruit_IO import Client, RequestError, Data"
    Paho MQTT: "pip install paho-mqtt"
`   GPIO : "import RPi.GPIO as GPIO"

Hardware Used:

    
    PIR Motion Sensor (HC-SR501) x 3
    Raspberry Pi 3 Model B
    Micro SD Card
    Breadboard Wire x 6 (male to female)
    Breadboard Wire x 3 (female to female)


Hardware Configuration:

   
     HC-SR501 (runway):

        VCC - 5V(Pin 4)

        GND - GND(Pin 9(via breadboard))

        OUT - GPIO4(Pin 7(via breadboard))


     HC-SR501 (gate01):

        VCC - 5V(Pin 17)

        GND - GND(Pin 9(via breadboard))

        OUT - GPIO4(Pin 7(via breadboard))

     HC-SR501 (gate01):

        VCC - 5V(Pin 27)

        GND - GND(Pin 9(via breadboard))

        OUT - GPIO4(Pin 7(via breadboard))

        (https://projects.raspberrypi.org/en/projects/physical-computing/11)

        

MQTT Login Credentials: • Address: soc-broker.rgu.ac.uk • Port: 8883 • User_name: sociot • password: s7ci7tRGU

    (Only available in uni)



