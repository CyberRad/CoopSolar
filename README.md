# CoopSolar
Communicate with Renogy Rover Elite over RS485 to Sparkfun 9822 connected to a Raspberry Pi using Python. Upload the data points to InfluxDB for display in Grafana.

getcharge.py is ran every minute using cron. This script handles the communication to the controller and sends the data to InfluxDB.

Thanks to nsaspook on allaboutcircuits.com for mapping out the controller and helping me understand RS485. https://forum.allaboutcircuits.com/threads/project-solar-wind-pic-controlled-battery-array.32879/
