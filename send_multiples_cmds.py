# from netmiko import Netmiko

# connection = Netmiko(host = '10.123.2.1', port = '22', username = 'u1',password = 'cisco', device_type = 'cisco_ios')

from netmiko import ConnectHandler
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
print('Entering enable mode')
connection.enable()

cmds = [
    'int loopback  0',
    'ip address 10.0.0.1 255.255.255.255',
    'exit',
    'username u5 password cisco'
]

connection.send_config_set(cmds)

output = connection.send_config_set(cmds)
print(output)

print(connection.find_prompt())

connection.send_command('wr')

print('Closing connection')
connection.disconnect()
