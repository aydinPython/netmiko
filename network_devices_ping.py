import platform
import os
from datetime import datetime
from rich.console import Console
from multiprocessing import Process, Pool
import multiprocessing as mp


def scanning():
    networkAddress = input("Enter network address: ")
    net1 = networkAddress.split(
        "."
    )  # daxil etdiyimiz network addresini noqtelerden ayirarag her birini listin icine string kimi elave edir


    startRange = int(
        input("Enter starting number: ")
    )  # network range araliginin bashladigi ip
    endedRange = int(
        input("Enter last number: ")
    )  # network range araliginin bitdiyi ip

    ping1 = "ping"  # ping ucun istifade olunacaq komanda

    print("Scanning in Progress")

    newIpAddr = net1[0:3]
    newIp = ".".join(newIpAddr)
    temp = []
    ping_count = 3
    if platform.system().lower() == "windows":
        argument = "-n"
    else:
        argument = "-c"
    for ip in range(startRange, endedRange):
        addr = f"{newIp}.{ip}"  # startRange de olan ilk address net2den elde olunan adresin son oktetine elave olunur ve endedRange bitene qeder davam edir
        comm = f"{ping1} {argument} {ping_count} {addr}"
        temp.append(comm)
    return temp


def check_result(command):
    address = command.split()[-1]
    response = os.popen(command)
    # print(response)
    for line in response.readlines():
        # print(line)
        if "TTL=64".lower() in line.lower() or "TTL=128".lower() in line.lower():
            # print(address, " active")
            return (address, " active")

        elif "Destination host unreachable".lower() in line.lower():
            # print(address, " inactive")
            return (address, " inactive")


if __name__ == "__main__":
    if platform.system().lower() == "windows":
        mp.set_start_method("spawn")

    t1 = datetime.now()
    print(t1)
    ip_list = scanning()
    console = Console()

    with Pool() as pool:
        result = pool.map(check_result, ip_list)
        pool.close()

    for ip, res in result:
        console.print(f"Scanning result {ip} --> {res}", style="bold red")
    t2 = datetime.now()
    print(t2)

    total = t2 - t1
    print("Scanning complete in ", total)
    print("Scanned ip count: ", len(result))
