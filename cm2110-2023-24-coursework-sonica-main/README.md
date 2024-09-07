                                        Sonica
Members:
-  Matthew Holmes
-  Stuart Keith
-  William Drummond

System Description:

The SDG problem we have chose is SDG 9: Industry, Innovation & Infrastructure.
    
our node aims so create a more sustainable environment within aviation, by making instructions quicker and giving more precise directions to aircraft reducing taxi times and through our baggage system making turnaround times quicker which all in turn, reduces the amount of fuel aircraft use on the airfeild. We also look to get rid of paper baggage tags by using reusable chips that can be scanned when sending baggage to a plane and then reissued at the destination airport if they use our system. this also helps the infrastructure of the airport and the aviation industry and also imporves the  infrastructure of any countries who decide to sue our system.
    
The system we have designed and produced is a system to help with numerous airport operations, from weather and baggage, to managing the airfield. the system is aimed to aid in helping airport workers reduce their stress and make their jobs easier as well as make baggage processing faster and more stress free for passengers. The system also aims to make navigating an aircraft so much easier with automated instructions on where to go and what they should do. The baggage system uses a series of scanners to make sure a bag gets send to the right plane and the weather system helps to detect flooding and water levels so we can predict wether the airfield is liable to a flood or not.

System Design:

  - Types of IoT Nodes and Role:
      
      - Baggage Device, Programming Sink Node: Subscribes to MQTT (sonica/baggage) to recieve messages published and forwards data to Adafruit where it is stored. This device is used to scan baggage tags and direct the baggage to the appropriate gate.
      
      - Weather Device, Sensor/Actuator Node: Pushes to MQTT (sonica/Water) to send messages about the water detection, all the data collected by the weather node is also pushed to the Adafruit dashboard which allows the user to have a overall view of the airports sensors.

      - AirTraffic Device, sensor node, to detect aircraft and guide them to where they need to be or go. This data is then sent to a 3rd aprty service, in           this case we have used adafruit to create a dashboard with all the information. this node uses a total of 3 motions sensors and uses the lights on the          sense hat.

  - Topology and Computer paradigm
      - Edge Computing paradigm should be used to upscale this project as this will use a centralised on-site server, this will be more secure, lower processing power and all data is kept local on devices allowing fast access for quick analysis.

  - Messaging Protocols and Technologies
      - MQTT
      - Adafruit


  - User Control
      - User decides location of sensors via input and can change name of topics/feeds via changing the code

System Guide:
