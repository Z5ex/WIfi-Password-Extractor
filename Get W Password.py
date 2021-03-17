#Module
import subprocess

Banner ="""
 /$$$$$$$$        /$$   /$$                                                                                                                                       
|_____ $$        | $$  | $$                                                                                                                                       
     /$$/$$    /$| $$  | $$ /$$$$$$                                                                                                                               
    /$$|  $$  /$$| $$$$$$$$/$$__  $$                                                                                                                              
   /$$/ \  $$/$$/|_____  $| $$$$$$$$                                                                                                                              
  /$$/   \  $$$/       | $| $$_____/                                                                                                                              
 /$$$$$$$$\  $/        | $|  $$$$$$$                                                                                                                              
|________/ \_/         |__/\_______/                                                                                                                              
 /$$$$$$$                                                               /$$       /$$$$$$$$           /$$                                /$$                      
| $$__  $$                                                             | $$      | $$_____/          | $$                               | $$                      
| $$  \ $$/$$$$$$  /$$$$$$$/$$$$$$$/$$  /$$  /$$ /$$$$$$  /$$$$$$  /$$$$$$$      | $$      /$$   /$$/$$$$$$   /$$$$$$ /$$$$$$  /$$$$$$$/$$$$$$   /$$$$$$  /$$$$$$ 
| $$$$$$$|____  $$/$$_____/$$_____| $$ | $$ | $$/$$__  $$/$$__  $$/$$__  $$      | $$$$$  |  $$ /$$|_  $$_/  /$$__  $|____  $$/$$_____|_  $$_/  /$$__  $$/$$__  $$
| $$____/ /$$$$$$|  $$$$$|  $$$$$$| $$ | $$ | $| $$  \ $| $$  \__| $$  | $$      | $$__/   \  $$$$/  | $$   | $$  \__//$$$$$$| $$       | $$   | $$  \ $| $$  \__/
| $$     /$$__  $$\____  $\____  $| $$ | $$ | $| $$  | $| $$     | $$  | $$      | $$       >$$  $$  | $$ /$| $$     /$$__  $| $$       | $$ /$| $$  | $| $$      
| $$    |  $$$$$$$/$$$$$$$/$$$$$$$|  $$$$$/$$$$|  $$$$$$| $$     |  $$$$$$$      | $$$$$$$$/$$/\  $$ |  $$$$| $$    |  $$$$$$|  $$$$$$$ |  $$$$|  $$$$$$| $$      
|__/     \_______|_______|_______/ \_____/\___/ \______/|__/      \_______/      |________|__/  \__/  \___/ |__/     \_______/\_______/  \___/  \______/|__/      
                                                                                                                                                                  
                                                                                                                                                                  
                                                                                                                                                                """


print(Banner)

# The Important
Cmdata = subprocess.check_output(["netsh","wlan","show","profiles"]).decode('utf-8',errors="backslashreplace").split("\n")
WifiProfiles = []
for i in Cmdata:
    if "All User Profile" in i:
        WifiProfiles.append(i.split(":")[1][1:-1])

for i in WifiProfiles:
    try:
        WiResults =subprocess.check_output(["netsh","wlan","show","profile",i,"key=clear"]).decode('utf-8',errors="backslashreplace").split("\n")
        Result = []
        for o in WiResults:
            if "Key Content" in o:
                Result.append(o.split(":")[1][1:-1])
        
        try:
            print("{:<30}: {:<}".format(i,Result[0]))
        except Exception as ex:
            print("{:<30}: {:<}".format(i,""))
    except Exception as e:
        print("{:<30}: {:<}".format(i,"ERORR OCCURED"))

