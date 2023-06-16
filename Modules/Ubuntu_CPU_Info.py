from Line_Break import line_break
import psutil

#Get CPU Info (Linux Only Var)
def CPU_Info():
    #Read CPUINFO file to print name of CPU
    try:
        with open('/proc/cpuinfo', 'r') as f:
            file_info = f.readlines()
        cpuinfo = [x.strip().split(':')[1] for x in file_info if 'model name' in x]
        for index, item in enumerate(cpuinfo):
            print('[+] Processor ' + str(index) + ' : ' + item)
    except:
        if FileNotFoundError:
            print(FileNotFoundError)
            pass
    
    # This code will print the number of CPU cores present
    print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
    print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
    line_break()
    
    # This will print the maximum, minimum and current CPU frequency
    cpu_frequency = psutil.cpu_freq()
    print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
    print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
    line_break()
