from netmiko import ConnectHandler

r1 = {
    'device_type':'cisco_ios',
    'ip':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}

#connect to router 
connect = ConnectHandler(**r1)

#check enable mode 
prompter = connect.find_prompt()
if '>' in prompter:
    connect.enable()

#using while loop to verify if interface-id is correct
while True:
    interface = input ('Enter the interface you want to check:')
    output = connect.send_command('show ip interface ' + interface)
    print(output)
    if 'Invalid input detected' in output:
        print('Entered invalid interface , please re-enter interface')
        continue
    else:
        break

#check first line of the output 
first_line = output.splitlines()[0]
print(first_line)

#if interface is down --> enable interface 
if 'up' not in first_line:
    print('The interface is down. Enabling interface')
    commands = ['interface ' + interface, 'no shut', 'exit']
    output = connect.send_config_set(commands)
    print(output)
    print('#' * 30 )
#if interface is up , send notification 
else:
    print('The interface is already up ')

#Closing connection
print('closing the connection')
connect.disconnect()
