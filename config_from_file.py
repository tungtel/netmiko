from netmiko import ConnectHandler
#netmiko is a module and ConnecHandler is a fuction 

#Create a dictionary r1 to store router information 
r1 = {
    'device_type':'cisco_ios',
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose': True
}

#object connection is created/returned by function ConnectHandler
#ConnectHandler is called with r1 as its argument

connection = ConnectHandler(**r1)

#Entering eable mode.
#Method enable is called on object connection
print('Enter enable mode ... ')
connection.enable()

#method send_config_from_file is called , arguments is the file 
#it returns a string which is result of the command executed 
print('Sending command from file')
connection.send_config_from_file('ospf.txt')
output = connection.send_config_from_file('ospf.txt')
print(output)

#Closing connection 
#Method disconnect is called on object connection 
print('closing connection ... ')
connection.disconnect()
