import tarfile
import json
import datetime
from pathlib import Path

from InfoScrap import general_info
from InfoScrap import network_info
from InfoScrap import process_info

def saveScrapInfo():
    ct = datetime.datetime.now()
    FileName = str(ct) + "-DataExport"
    FileName = FileName.replace(" ", "-").replace(".", "-").replace("\\", "").replace(":", "-")

    RAM = general_info.getRAMInfo()
    DISK = general_info.getDiskInfo()
    InterfaceTrafficTAB = network_info.getTrafficInterface()
    InterfaceTraffic = {}
    AllProcessTAB = process_info.getProcess()
    AllProcess = {}

    for i in range(len(InterfaceTrafficTAB)):
        tempo = {
            "Received": InterfaceTrafficTAB[i][1],
            "Sent": InterfaceTrafficTAB[i][2]
        }

        InterfaceTraffic[InterfaceTrafficTAB[i][0]] = tempo

    for i in range(len(AllProcessTAB)):
        tempo = {
            "Pid": AllProcessTAB[i][0],
            "Name": AllProcessTAB[i][1],
            "Status": AllProcessTAB[i][2],
            "Ppid": AllProcessTAB[i][3],
            "CmdLine": AllProcessTAB[i][4]

        }

        AllProcess[AllProcessTAB[i][1]] = tempo


    AllInfo = {
        "GeneralInfo": {"OS_Version": general_info.getOSversion(),
                        "OS": general_info.getOS(),
                        "Uptime": general_info.uptime(),
                        "KernelVesion": general_info.getKernelVersion(),
                        "CPU": general_info.getCPUInfo(),
                        "Memory": {"Total": RAM[0],
                                "Free": RAM[1],
                                "Used": RAM[2]},

                        "Disk": {"Total": DISK[0],
                                "Free": DISK[1],
                                "Used": DISK[2]},
                        "OpenFileLimit": general_info.getOpenFileLimit(),
                        "OpenProsLimit": general_info.getOpenProsLimit(),
                        "InstallPakages": general_info.getAllPakage(),
                        },
        "NetworkInfo": {"IP": {"Intern": network_info.getIpInternAdress(),
                            "Extern": network_info.getIpExtAdress(), },
                        "ForwardPackages": network_info.getIpForward(),
                        "NetworkInterface": network_info.getInterfaces(),
                        "TrafficInterface": InterfaceTraffic,
                        "Routes": network_info.getRoutes(),
                        },
        "ProcessInfo": AllProcess,
    }

    # Serializing json
    json_object = json.dumps(AllInfo, indent=4)

    # Writing to sample.json
    with open(f"/www/{FileName}.json", "w") as outfile:
        outfile.write(json_object)

    tar = tarfile.open( f"/home/minitel/{FileName}.tar", "w")

    tar.add(f"/www/{FileName}.json",arcname=f"{FileName}.json" ,recursive=False)

    tar.close()