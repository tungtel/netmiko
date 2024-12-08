from netmiko import ConnectHandler
import logging
import time 

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.123.2.1',
    'username': 'u1',  
    'password': 'cisco',
    'port' : 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
print('Entering eble mode:')
connection.enable()

connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)

print('Closing connection')
connection.disconnect()
