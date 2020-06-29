import subprocess
import ipaddress
from datetime import datetime


def defineNetwork(netAddr):

    networkAddress = netAddr
    ipNetwork = ipaddress.ip_network(networkAddress)
    allHosts = list(ipNetwork.hosts())
    print()
    return allHosts



def doPingdoCheck(allHosts):

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    SST = datetime.now()
    for host in range(len(allHosts)):

        outF = open("Inactive Hosts.txt", "a")
        outFOn = open("Active Hosts.txt", "a")
        output = subprocess.Popen(['ping', '-n', '1','-w', '500', str(allHosts[host])], stdout=subprocess.PIPE,
                                  startupinfo=info).communicate()[0]


        if "Destination host unreachable" in output.decode('utf-8'):
            outF.write(f'{str(allHosts[host])} \n')
            print(str(allHosts[host]), "> > > InActive (dest unreach)")
        elif "Request timed out" in output.decode('utf-8'):
            print(str(allHosts[host]), "> > > InActive (req timed out)")
            outF.write(f'{str(allHosts[host])} \n')
        else:
            outFOn.write(f'{str(allHosts[host])} \n')
            print(str(allHosts[host]), "> > > Active (succesful)")


        outF.close()
        outFOn.close()

    return SST



# For Main

networkAddress = input('Enter network address (192.168.1.0/24) : ')
hosts = defineNetwork(networkAddress)
print(f'Scanning for {networkAddress}')
print()

forscantime = doPingdoCheck(hosts)
EST = datetime.now()
TST = EST - forscantime


count = 0
activeHost = open('Active Hosts.txt','r')

actHosts = []
for i in activeHost:
    count += 1
    actHosts.append(i)
print()
print(f'Scanning Time : {TST}')
print(f'Number of Active Hosts: {count}')
print(f'Active Hosts: {actHosts}')