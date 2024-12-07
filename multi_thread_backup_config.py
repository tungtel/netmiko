from netmiko import ConnectHandler
from datetime import datetime
import threading
import time

start = time.time()

#Create a function to backup config , only one argument is router_creds 
def backup(router_creds):
    #Step 1. Create instance of object connect 
    connect = ConnectHandler(**router_creds)

    #Step 2. Enable mode 
    print('Entering enable mode...')
    connect.enable()

    #Step 3. Send command "show run" & print output 
    connect.send_command('show run')
    output = connect.send_command('show run')

    #Step 4a. find the hostname and create the backup filename from host name 
    prompt = connect.find_prompt()
    hostname = prompt[0:-1]
    #Step 4b. Find date/month/year from class datetime
    now = datetime.now() #now is an object returned by function "now" in module datetime
    year = now.year #call year atrribute of now 
    month = now.month #call month attribute of now 
    day = now.day #call day attribute of now 
    hour = now.hour #call hour attribute of now 
    #Step 4c. Form the filename
    filename = f'{hostname}-{hour}_{day}_{month}_{year}-backup.txt'

    #Step 5. Save the backup config
    with open(filename ,'w') as f: 
        f.write(output)
        print(f'back up of {hostname} is created succesfully')
        print("#" * 30)

    #Step final : closing conneciton
    print('closing connection')
    connect.disconnect()

#create a list of routers
with open('devices.txt','r') as f:
    routers = f.readlines()
    routers = [r.strip() for r in routers]
    print(routers)

#create a empty list of threads
threads = []

#Create a list of thread processess to be run for all routers
for r in routers:
    router_creds = {
        'device_type':'cisco_ios',
        'host':r,
        'username':'u1',
        'password':'cisco',
        'port':22,
        'secret':'cisco',
        'verbose':True
    }  
    th = threading.Thread(target = backup, args = (router_creds,))
    threads.append(th)

#start the process
for th in threads:
    th.start()

#wait for all threads complete before continue 
for th in threads: 
    th.join()


print('Backup configuration is completed')
end = time.time()
print(f'total time of running backup config is {end - start}')
