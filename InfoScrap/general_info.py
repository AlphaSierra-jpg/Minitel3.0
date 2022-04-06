import subprocess
import psutil


def getOSversion():
    release = subprocess.check_output(
        'cat /etc/os-release', shell=True, universal_newlines=True).split("\n")
    return release[3].replace("VERSION=", "").replace('"', "")


def getOS():
    release = subprocess.check_output(
        'cat /etc/os-release', shell=True, universal_newlines=True).split("\n")
    return release[1].replace("NAME=", "").replace('"', "")


def uptime():
    tempo = subprocess.check_output(['uptime']).decode(
        'utf-8').replace("\n", "").split(",")
    return tempo[0]


def getKernelVersion():
    return subprocess.check_output('uname -v', shell=True, universal_newlines=True).replace("\n", "")


def getCPUInfo():
    lscpu = subprocess.check_output(
        'lscpu', shell=True, universal_newlines=True).split("\n")
    return lscpu[13].replace("Model name:                      ", "")


def getRAMInfo():
    RAM = subprocess.check_output(
        'free -ht', shell=True, universal_newlines=True).split("\n")
    RAM = RAM[1].strip().replace("Mem:", "").replace(" ", "").split("i")
    for i in range(0, 4):
        RAM.pop()

    for i in range(len(RAM)):
        RAM[i] = RAM[i] + "o"

    return RAM


def getDiskInfo():
    output = []
    hdd = psutil.disk_usage('/')
    output.append(round(hdd.total / (2**30), 2))
    output.append(round(hdd.free / (2**30), 2))
    output.append(round(hdd.used / (2**30), 2))
    return output


def getOpenFileLimit():
    return subprocess.check_output('ulimit -n', shell=True, universal_newlines=True).replace("\n", "")


def getOpenProsLimit():
    open_pros_limit = subprocess.check_output(
        'ulimit -a', shell=True, universal_newlines=True).split("\n")
    return open_pros_limit[7].replace("process              ", "")


def getAllPakage():
    all_pakage = []

    all_pakage_raw = subprocess.check_output(
        'sudo apt list --installed 2>/dev/null', shell=True, universal_newlines=True).split("\n")

    for i in range(1, len(all_pakage_raw)-1):
        tempo = all_pakage_raw[i].split("/")
        all_pakage.append(tempo[0])
    return all_pakage

def printInfo():

    print(f"Version du système d'exploitation: {getOSversion()}")
    print(f'Operating system: {getOS()}')
    print(f"Uptime: {uptime()}")
    print(f"Version du Kernel: {getKernelVersion()}")
    print(f"CPU: {getCPUInfo()}")
    print(f"Mémoire: total        used        free")
    print(f"{ getRAMInfo() }")
    print(f"disque dur capacité en Go / espace dispo en Go / espace utilise en Go )")
    print(f"{ getDiskInfo() }")
    print(f"Limite de fichiers ouverts: {getOpenFileLimit()}")
    print(f"Limite de processus ouverts: {getOpenProsLimit()}")
    print(f"liste des paquets installés: {getAllPakage()}")
