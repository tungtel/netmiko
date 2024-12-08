from netmiko import ConnectHandler
from netmiko import file_transfer

r1 = {
    'device_type':'cisco_ios',
    'ip':'10.123.2.1',
    'username':'scpuser',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}

#Connect to r1 
connect = ConnectHandler(**r1)

#Call the file_transfer functon and passing the parameters
transfer_output = file_transfer(connect, source_file = 'ospf.txt',dest_file = 'ospf1.txt',
file_system = 'flash0:' , direction = 'put', overwrite_file = True )

print(transfer_output)
connect.disconnect()
