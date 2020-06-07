from netmiko import ConnectHandler       # Devicelere ssh baglanmaq ConnectHandler funksiyasini import edirik
from datetime import datetime
from time import sleep

# Device-larimiz ucun credentiallari dictionary formatda mueyyen edirik

sw_1 = {'device_type': 'cisco_ios',
        'username': 'python',
        'password': 'python',
        'secret': 'P@ssw0rd',
        'ip': '172.16.140.208'}

sw_2 = {'device_type': 'cisco_ios',
        'username': 'python',
        'password': 'python',
        'secret': 'P@ssw0rd',
        'ip': '172.16.140.200'}

sw_3 = {'device_type': 'cisco_ios',
        'username': 'python',
        'password': 'P@ssw0rd',
        'ip': '172.16.140.201'}

sw_4 = {'device_type': 'cisco_ios',
        'username': 'python',
        'password': 'P@ssw0rd',
        'ip': '172.16.140.202'}

fw_01 = {'device_type': 'checkpoint',
         'username': 'admin',
         'password': 'Pa$$w0rd',
         'ip': '172.16.140.202'}

# Bugunku gunun tarixini elde edirik

date = datetime.now().day

# Butun devicelerimizi list formasina aliriq

all_devices = [sw_1, sw_2, sw_3, sw_4, fw_01]


# Log fayl yaratmaq ucun funksiya

def createLogFile(file_name, forLogResult):
    with open("/root/network_automation/pythonScripts/" + file_name, 'w', ) as log_line:
        output = log_line.write(forLogResult) # forLogResult,filename (func) funksiyasindan return olunur
        return output


# Hansi Device, Device Adi, Verilecek komandalar ucun funksiya

def sendCommandDeviceGetLog(device, command, deviceName):
    ssh_connect = ConnectHandler(**device)
    whichSw = '\nGetting Backup from ' + str(device['ip'] + ' ' + deviceName)
    file_name = f'backup_{str(device["ip"])} {date}.txt'
    ln = len(whichSw)
    char = ln * '_'
    print(char)
    print(whichSw, end='')
    for _ in range(3):
        print(' ! ', end='')
        sleep(3)
    ssh_connect.enable()
    forLogResult = ssh_connect.send_command(command) # hemin komanda send olunur forLogResult-da saxlanilir

    return [file_name, forLogResult]

# Her bir devicemize bir bir baglanmaq ucun loop qurulur

for device in all_devices:

    if device == fw_01:
        result = sendCommandDeviceGetLog(device, 'show configuration', 'Firewall')
        createLogFile(result[0], result[1])
    else:
        result = sendCommandDeviceGetLog(device, 'show startup-config', 'Switch')
        createLogFile(result[0], result[1])

    print()

print('Script is ended succesfully\n')
