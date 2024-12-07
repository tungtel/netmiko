from netmiko import ConnectHandler

linux = {
    'device_type':'linux',
    'host':'10.123.2.10',
    'username':'root',
    'password':'root',
    'port':22,
    'secret':'cisco', #sudo password
    'verbose':True
    }

connect = ConnectHandler(**linux)
connect.enable() #sudo su 
output = connect.send_command('ip addr')
print(output)

print('Closing connection')
connect.disconnect()
