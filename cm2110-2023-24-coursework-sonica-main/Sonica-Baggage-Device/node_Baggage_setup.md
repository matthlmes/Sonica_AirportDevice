Third Party Libraries / Software:
  - MFRC522 Library: "pip install mfrc522"
  - Paho MQTT: "pip install paho-mqtt"


Hardware Used:
  - RIFD/NFC Scanner (RFID-RC522)
  - PIR Motion Sensor (HC-SR501)
  - Raspberry Pi 3 Model B
  - Micro SD Card
  - Breadboard Wire x 7 (Female to Female)


Hardware Configuration:
  - RFID-RC522:
      - 3.3V - 3.3V(Pin 1)
      - RST  - GPIO25(Pin 22)
      - GND  - Ground(Pin 6)
      - IRQ  - N/A
      - MISO - GPIO9(Pin 21)
      - MOSI - GPIO10(Pin 19)
      - SCK  - GPIO11(Pin 23)
      - SDA  - GPIO8(Pin 24)

      - (https://pimylifeup.com/raspberry-pi-rfid-rc522/)

  - HC-SR501:
      - VCC - 5V(Pin 2)
      - GND - GND(Pin 9)
      - OUT - GPIO4(Pin 7)

      - (https://projects.raspberrypi.org/en/projects/physical-computing/11)



MQTT Login Credentials:
  • Address: soc-broker.rgu.ac.uk
  • Port: 8883
  • User_name: sociot
  • password: s7ci7tRGU

  - (Only available in uni)

Extra:
  - To pre-write to the NFC/RFID tags for "Gate 1" or "Gate 2" etc use the write.py file alongisde the wiring of only the RFID reader.
  - (This would be done at baggage check-in and therefore isn't accounted for in the final system)
