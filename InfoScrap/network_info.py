import subprocess
import os


def getIpExtAdress():
    try:
        return subprocess.check_output("curl -s ifconfig.me", shell=True, universal_newlines=True)
    except:
        return "no internet"


def getIpInternAdress():
    output = subprocess.check_output(
        "ip addr $1 | grep \"inet\|inet6\" | awk -F' ' '{print $2}' | awk '{print $1}'", shell=True, universal_newlines=True).split('\n')
    return output[2].replace("/24", "")


def getInterfaces():
    return os.listdir('/sys/class/net/')


def getTrafficInterface():
    interfaces = getInterfaces()
    traffic = []
    interface = []
    for i in range(len(interfaces)):
        interface = []
        interface.append(interfaces[i])

        tempoT = "cat /sys/class/net/" + \
            interfaces[i] + "/statistics/tx_packets"
        tempoR = "cat /sys/class/net/" + \
            interfaces[i] + "/statistics/rx_packets"

        paquetT = subprocess.check_output(
            tempoT, shell=True, universal_newlines=True).replace("\n", "")
        paquetR = subprocess.check_output(
            tempoR, shell=True, universal_newlines=True).replace("\n", "")

        interface.append(paquetR)
        interface.append(paquetT)
        traffic.append(interface)

    return traffic


def getRoutes():
    return subprocess.check_output("ip route", shell=True, universal_newlines=True).strip().split("\n")


def getIpForward():
    IpForward = subprocess.check_output(
        "cat /proc/sys/net/ipv4/ip_forward", shell=True, universal_newlines=True).strip().replace("\n", "")

    if IpForward == "0":
        return False
    else:
        return True

def printInfo():

    print(f"Adresse IP:")
    print(f"    Exter: {getIpExtAdress()}")
    print(f"    Intern: {getIpInternAdress()}")
    print(f"Interfaces: {getInterfaces()}")
    print(
        f"Paquets interfaces: nom interface / paquets reçu / paquets envoyés\n{getTrafficInterface()}")
    print(f"Routes: {getRoutes()}")
    print(f"Forward paquet: {getIpForward()}")
