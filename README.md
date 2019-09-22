# Brainy-Streets
This is a smart road concept whose hardware was done by my partner [Dev Savla](https://www.linkedin.com/in/devsavla "Dev Savla").

You can find it hosted here: [brainy-streets.herokuapp.com](https://brainy-streets.herokuapp.com)

## *INTRODUCTION*
Our System uses Arduino Mega and ESP 8266 Wifi module to create a smart road concept. Each road has one Arduino and wifi module connected to multiple sensors. We have daylight sensors to detect sunlight intensity, smog/fog sensors to detect Air Quality Index and Infrared/Ultraviolet (IR/UV) sensors to detect traffic. The system can connect directly to smart vehicles (vehicles with communications and networking capabilities) and autonomous vehicles, so vehicles can get realtime data from the road directly, even in spotty network conditions. The idea is to create an interconnected network of roads and vehicles sharing information with each other, to make mobility easier. 

The system is designed with energy efficiency in mind. We have implemented solar panels to power the street lights, sensor grid and hardware components and the system can actually be energy positive and give back to the grid. This also allows additional components to be added to the system in the future as we have excess electricity available to power them. Road safety camera systems and traffic lights can also possibly draw power from our system and even connect to our system for additional data and features. We have 3 major components, as described below:

*1. Smart Street Lighting System*
	a) During the day, when the sunlight intensity is above the visibility threshold and hence the street lights are not needed, the lights remain off. 
	b) At night or during otherwise dim conditions, when ambient light intensity is below the visibility threshold, our system kicks in. When an IR sensor detects a vehicle, it switches ON the next few lights automatically. Till the vehicle isn't detected crossing the next sensor, lights stay ON, so in case of emergency or breakdown, vehicles aren't left in darkness.
	c) In smog, fog or other low visibility conditions due to bad air quality, emergency high intensity lights are turned on.
	
*2. Interconnected Roads Concept*
  a) Roads connect to smart vehicles and autonomous vehicles to provide valuable information such as guidance, routing, traffic data etc. This works by making a "handshake" with the vehicle when it comes into range. This system is only a concept for now as we do not have access to such vehicles on our current scale.
	b) Roads also connect to their neighbouring roads if they have the system enabled, allowing smart routing without the need for a strong internet connection. For example, if a road is shut due to construction work, flooding or other roadblocks and the system has been updated with that information, then the adjacent roads can communicate that information to any incoming connected vehicles, so they know not to take that road.
	
*3. Master Slave model*
This is a system implemented to ensure data security and low cost. We do all data storage and analytics on a secure server (in the prototype it is simply a python Django server with fixed token authentication). Data is sent to the server by the hardware device (arduino) via the network. The data can be encrypted with a synced PRNG system in the future. Since the analytics is outsourced, the hardware on the road is simply a data collection, management and communication device, and requires low cost components.

## *Other Possible Uses of Data Collected*
  1) Any issues in roads causing traffic can be easily noticed and pointed out, such as a pothole slowing down vehicles can be seen as an increase of average traffic density or a breakdown can be seen as a spike in traffic. This gives us a lot of data to work on to improve road and vehicle designs.
  2) Live Air Quality Monitoring from the roads can help pin point any major air pollution sources by location and intensity. This data can also be used by patients of asthma and other respiratory ailments to avoid areas with bad air quality.
