logCount = {"ERROR":0,"INFO":0,"DEBUG":0,"WARNING":0}
with open("log.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        if "ERROR" in line:
            logCount["ERROR"] += 1
        elif "INFO" in line:
            logCount["INFO"] += 1
        elif "DEBUG" in line:
            logCount["DEBUG"] += 1
        elif "WARNING" in line:
            logCount["WARNING"] += 1
    print(logCount)

with open("errorlog.txt","w") as errorfile:
    for line in lines:
        if "WARNING" in line:
            errorfile.write(line)