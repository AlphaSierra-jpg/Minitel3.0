import psutil
import os
import signal

def getProcess():
    process = []
    processInfo = []
    
    for p in psutil.process_iter():
        processInfo.append(p.pid)
        processInfo.append(p.name())
        processInfo.append(p.status())
        processInfo.append(p.ppid())
        processInfo.append(p.cmdline())
        process.append(processInfo)
        processInfo = []

    return process


def isSoftStopProcess(process, isSoft):

    if isSoft == True:
        try:
             os.kill(process, signal.SIGTERM)
        except:
            return "Process dont exist"
    else:
        try:
            os.kill(process, signal.SIGKILL)
        except:
            return "Process dont exist"

    return "Process " + str(process) + " stoped sucessfully"

def printInfo():

    print(getProcess())
    print(isSoftStopProcess(29180, False))


