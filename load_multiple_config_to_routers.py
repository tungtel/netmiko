from netmiko import ConnectHandler

#Create a list of routers IP from file 
with open('devices.txt','r') as f:
    devices = f.readlines()
    devices = [device.strip() for device in devices]
    # print(devices)

#Create a list creds for 3 router 
router_list = list()

#iterate ip in device list , each IP is asigned for the host of router
for ip in devices: 
    router = {
        'device_type':'cisco_ios',
        'host':ip,
        'username':'u1',
        'password':'cisco',
        'port':22,
        'secret':'cisco',
        'verbose':True
    }
    #append router to router_list
    router_list.append(router)

print(router_list)
with open('config_filename.txt','r') as f:
    list_filename = f.readlines()
    list_filename = [filename.strip() for filename in list_filename]
    print(list_filename)

for router in router_list:
    #connect to router 
    connection = ConnectHandler(**router)

    #Enter enable mode 
    print('Entering enable mode ...')
    connection.enable()

    #User enter the name of config file , send command and show output 
    # file = input(f'Please enter the config file name for router {router["host"]}:')

    #find index of router seq "n"
    index = router_list.index(router)

    # from index , assign the file (r1-index0 - file1 , r2-index1-file2 , etc )
    file = list_filename[index]
    print(f'filename of router {router["host"]} is {file}')

    connection.send_config_from_file(file)
    output = connection.send_config_from_file(file)
    print(output)

    #Close connection
    print('Closing connection ...')
    connection.disconnect()
    print('#'*50)

