Leading Group Member: William Drummond

Node Functionalities: This nodes role is to detect, instruct and navigate different aircraft within the airspace and airfield. The node identifies where the given Aircraft needs to go and then will send an instruction to the aircraft telling it where to go. 
The system can automatically detect what gates are open or taken and direct an aircraft to an open gate. The system also detects wether there is an Aircraft on the runway and in the case that there is, the system will automatically tell an approaching aircraft that the runway is unnavailable, meaning that the plane will automatically eb told to go around. This node will help to take some stress off of air traffic controllers. This system has real potential to become an amazing part of innovation in the future and within aviation itself.

For this node to be made practically on a larger scale large custom spec pc's and servers would have to be made to handle the large scale requests and process information in realtime. The reason for this is on the scale of an airport, your looking at dealing with up to 40+ aircraft in the airspace at 1 given time which is a lot for a raspberry pi or an arduino to handle.

something like the LattePanda 3 Delta would be a very good single board computer to be used for this device on a small scale airport such as edinburgh airport or aberdeen international.



Types Of Sensors:

PIR sensors:
	- these are used to detect the aircraft and give instructions upon detection

Messaging Protocols / Technologies:

MQTT:
    - Server inside of uni used to retrieve information from the weather node, to detect wether the airport is flooded

AdaFruit:
    - This is used for the dashboard where the user can see what gates are open and can also see wetehr the runway is in use or not.
