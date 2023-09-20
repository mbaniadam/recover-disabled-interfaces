from netmiko import ConnectHandler, ssh_exception
from time import sleep
import subprocess
import re

Network_Device_1 = {'host': '172.16.10.70',
                  'username': 'mori',
                  'password' : 'mori',
                  'device_type': 'cisco_ios'
    }
Network_Device_2 = {'host': '172.16.10.75',
                  'username': 'mori',
                  'password' : 'mori',
                  'device_type': 'cisco_ios'
    }
all_device = [Network_Device_1,Network_Device_2]
Connect_to_device = ConnectHandler(**all_device)
Connect_to_device.enable()
# Find Err-Disabled interfaces
try:
    find_err_ints = Connect_to_device.send_command('Show interface status err-disabled')
    print(find_err_ints)
except (ssh_exception.AuthenticationException, EOFError):
            print(f'Authentication Error Device: {host} . Authentication Error')
except ssh_exception.NetmikoTimeoutException:
            print(f'Could not connect to {host} . Reason: Connection Timeout')  

get_interface_name =  re.findall(r"\bFa.+[0-9]\b|\bGi.+[0-9]\b", find_err_ints)             
# Caused By MAC Address
get_reason= re.findall('psecure-violation',find_err_ints)
i = 0
if get_interface_name and get_reason:
    for item in get_interface_name:
        try:
            clearsticky = Connect_to_device.send_command('clear port-security sticky interface ' + get_interface_name[i])
            commands = ['interface '+ get_interface_name[i],'shut','no shut']
            To_Excecute = Connect_to_device.send_config_set(commands)
            print(To_Excecute)
            sleep(2)
            To_Excecute = Connect_to_device.send_command('show interfaces '+ get_interface_name[i] + ' status')
            print(To_Excecute)
            i += 1
        except:
            print('Something went wrong!')

else:
    print ('There is no err-disabled interface caused by MAC address')


print("All disabled interfaces has been recoverd!")
print("----------------- End -----------------")



    
