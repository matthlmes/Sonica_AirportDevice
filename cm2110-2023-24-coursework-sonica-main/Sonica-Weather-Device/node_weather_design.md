Leading Group Member: Stuart Keith

Node Functionality:
The role of the weather node is to detect and collect data on the surrounding areas current weather. This is conducted by using the SenseHat conponent for the raspberry pi along with the soil moisture meter which is used to help detect if water is building in the areas around the runway and gates. The data that is collected is the then displayed on the Adafruit dashboard and also sends the water detection to the runway/gate node so that incoming planes have plenty of warning of the conditions on the ground.

Other Usable Single Board Computers: 
Raspberry Pi - 4 Model B: The Arduino Uno Rev3 is another single board computer that could be used instead of the Raspberry Pi 4 Modle B, The Arduino is also cheaper and slightly smaller than the Rasberry Pi, it also works with better components that can be more easily set-up by using npm packages. 

Types of sensors:

    Soil Moisture Sensor
      - Uses the digital output to provide a simple "on" or "off" for when the soil moisture value is above certain value
      - Data is also sent via MQTT to the runway and gates device

    Temperature Sensor
      - Detects temperature in the near area and outputs float integer 

    Pressure Sensor
      - Once started in code it will monitor the pressure around the device and display data in the adafruit dashboard

    Humidity Sensor
      - Humidity sensor monitors the humidity in the area and displays on dashboard
