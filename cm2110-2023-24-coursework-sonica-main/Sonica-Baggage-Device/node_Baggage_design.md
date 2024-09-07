Leading Group Member:
    Matthew Holmes

Node Functionalities:
    The Nodes role is to detect and scan baggage on a conveyor type system. This identifies where the
baggage needs to go and then will effect the conveyor with the appropriate response.
(In this current system the conveyor is only implied and hard coded using print statements.


Other Usuable Single Board Computers:
    - Raspberry Pi - 4 Model B: The upgraded version of the board we used
    - ASUS Tinker Board S: Same size as the board we used, slightly more expensive, more powerful GPU
                            This could be beneficial for a potentially better baggage detection system.
    - Le Potato(AML-S905X-CC): Has double the memory of the Pi 3 which could help with containing more scanners/sensors per board.
    - Arduino: Would work better for the scanners as it is a microcontroller which helps control the electrical components connecting to a systems circuit board.


Types Of Sensors:

    RFID/NFC Card Reader (RFID-RC522):
        - Reads tags on the 13.56MHz frequency
        - Outputs data in form (id, text)

    PIR Motion Sensor (HC-SR501):
        - Detects motion and once called in code will activate when motion detected and deactivate when motion isn't



Messaging Protocols / Technologies: 

    MQTT:
        - Server inside of uni used to subscribe to different topics, in this case this node is subscribed to sonica/baggage
    AdaFruit:
        - This is used for our dashboard, this node is connected to the baggage feed on it 
        and displays the feed of text from each different baggage scanned
