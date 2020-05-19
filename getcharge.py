from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from influxdb import InfluxDBClient
import time
import datetime
import logging
#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

# Connect to the controller and get values
client = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', baudrate = 9600, stopbits = 1, bytesize = 8, parity = 'N')
client.connect()
SOC = client.read_holding_registers(0x100, 2, unit=1)
BatVolt = client.read_holding_registers(0x101, 1, unit=1)
#Temps = client.read_holding_registers(0x103, 2, unit=1)
PanelVolt = client.read_holding_registers(0x107, 1, unit=1)
PanelCurrent = client.read_holding_registers(0x108, 1, unit=1)
ChargeCurrent = client.read_holding_registers(0x102, 1, unit=1)
PanelWatts = client.read_holding_registers(0x109, 1, unit=1)
solarVoltage = float(PanelVolt.registers[0] * 0.1)
solarCurrent = float(PanelCurrent.registers[0] *0.1)
batteryVoltage = float(BatVolt.registers[0] * 0.1)
batteryCapacity = SOC.registers[0]
#controllerTemp = Temps.registers[0]
#batteryTemp = Temps.registers[1]
chrgCurrent = float(ChargeCurrent.registers[0] * 0.1)
chrgPower = PanelWatts.registers[0]
print "Solar Voltage", solarVoltage
print "Battery Voltage", batteryVoltage
print "Battery Capacity", batteryCapacity
print "Solar Current", solarCurrent
#print controllerTemp
#print batteryTemp
print "Charge Current", chrgCurrent
print "Charge Power", chrgPower
# Send the values to the influxdb
data_end_time = int(time.time() * 1000)
dbclient = InfluxDBClient(host='<IP>', port=8086)
dbclient.create_database('<DB Name>')
data = []
data.append("{measurement} solarVoltage={solarVoltage},solarCurrent={solarCurrent},batteryVoltage={batteryVoltage},chargeCurrent={chargeCurrent},chargePower={chargePower},batteryCapacity={batteryCapacity} {timestamp}"
	.format(measurement= 'solar',
		solarVoltage= solarVoltage,
		solarCurrent= solarCurrent,
		batteryVoltage= batteryVoltage,
		chargeCurrent= chrgCurrent,
		chargePower= chrgPower,
		batteryCapacity= batteryCapacity,
		timestamp=data_end_time))
dbclient.write_points(data, database='<DB Name>', time_precision='ms', protocol='line')

client.close()
