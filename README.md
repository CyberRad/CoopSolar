# CoopSolar
Communicate with Renogy Rover Elite over RS485 to Sparkfun 9822 connected to a Raspberry Pi using Python. Upload the data points to InfluxDB for display in Grafana. The script may work for other Renogy charge controllers that use RS485.

getcharge.py is ran every 5 minutes using cron. This script handles the communication to the controller and sends the data to InfluxDB.

Thanks to nsaspook on allaboutcircuits.com for mapping out the controller and helping me understand RS485. https://forum.allaboutcircuits.com/threads/project-solar-wind-pic-controlled-battery-array.32879/

**Dependencies** - Python 3 with pymodbus and InfluxDBClient

Pinouts for Rover Elite and Sparkfun 9822

**Rover Elite**

- 1 Not Used
- 2 Not Used
- 3 Not Used
- 4 Not Used
- 5 GND
- 6 A
- 7 B
- 8 5v (not needed)

**Sparkfun 9822 w/RJ45 Jack**

- 1 Not Used
- 2 Not Used
- 3 Not Used
- 4 GND
- 5 GND
- 6 Not Used
- 7 B
- 8 A

I had to reverse pins 7 and 8 on the cable to the Sparkfun 9822 to get communication to happen. Unsure if Sparkfun or Rover Evolve is documented correctly.

![Graph of data](https://raw.githubusercontent.com/CyberRad/CoopSolar/master/grafana.png)
