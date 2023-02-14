# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.constants import Defaults as ModbusDefaults

import logging
FORMAT = ('%(message)-15s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# declaration of client and connexion

reading = 0
client = ModbusSerialClient(method='rtu', port = '/dev/ttyCLIENT', stopbits=1, bytesize=8, parity='N', baudrate=9600)

connexion = client.connect()
print(client)
print("\033[92m-------------------client connected----------------------\033[0m")


# log.debug("client started")

def responseReceived(response):
    print("connected")
#     log.debug("server has send data")


while True:
    
    if connexion == True:
        messageToSend = input("what do you want to write ?\n")
        client.write_registers(0, messageToSend.encode('ascii'),0x01)
        result = client.read_holding_registers(0,messageToSend.__sizeof__(), 0x01)
        # print(result)