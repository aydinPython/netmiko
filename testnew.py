import subprocess
import ipaddress
from datetime import datetime


StartTime = datetime.now()

def defineNetwork(netAddr):

    networkAddress = netAddr
    ipNetwork = ipaddress.ip_network(networkAddress)
    allHosts = list(ipNetwork.hosts())
    print()
    return allHosts

def forSubProcess():

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE


def doPingdoCheck(allHosts,subPro):




    for host in range(len(allHosts) + 1):
        outF = open("Inactive Hosts.txt", "a")
        outFOn = open("Active Hosts.txt", "a")
        output = subprocess.Popen(['ping', '-n', '1','-w', '500', str(allHosts[host])], stdout=subprocess.PIPE,
                                  startupinfo=subPro).communicate()[0]
        print(output)

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



# For Main

networkAddress = input('Enter network address (192.168.1.0/24) : ')
hosts = defineNetwork(networkAddress)
subPro = forSubProcess()
print(f'Scanning for {networkAddress}')
print()
doScanHost = doPingdoCheck(hosts,subPro)


