import threading
import socket
import time, os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
class bcolors:
    OKPURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN + """
 [#] Domain to IP
 [#] Coded by @willygoid
 [#] www.haxor.id
""" + bcolors.ENDC)

sitelist = input("Sitelist : ")
threadp = input("Thread (default: 100): ")
if threadp == '' or type(threadp) != int:
    threadp = 100
    
#url_list = open(sitelist,"r").read().splitlines()

def resolveDns(hostnames):
    
    for host in hostnames:
        try:
            checkHost = host.replace("https://", "").replace("http://", "").replace("www.", "")
            ip = socket.gethostbyname(checkHost)
            if ip is not None or ip != "":
		print(f"{bcolors.OKGREEN}{checkHost}{bcolors.ENDC} --> {ip}")
                with open("ips.txt","a") as f:
                    f.write(ip + "\n")
        except Exception as e:
            print(f"{bcolors.FAIL}{checkHost}{bcolors.ENDC}: Failed, domain inactive!")
            continue

if __name__ == "__main__":
    
    with open(sitelist) as file:
        hostnames = file.readlines()
        hostnames = [line.rstrip() for line in hostnames]
    
    print(bcolors.OKPURPLE + "===[ Start Work ]==="+ bcolors.ENDC)
    start = time.time()
    
    threads = list()

    chunksize = threadp

    chunks = [hostnames[i:i + chunksize] for i in range(0, len(hostnames), chunksize)]
    for chunk in chunks:
        x = threading.Thread(target=resolveDns, args=(chunk,))
        threads.append(x)
        x.start()

    for chunk, thread in enumerate(threads):
        thread.join()

    end = time.time()
    duration = end - start
    print(" ")
    print(f'{bcolors.OKCYAN}Finished {len(sitelist)} links in {duration} seconds {bcolors.ENDC}')
