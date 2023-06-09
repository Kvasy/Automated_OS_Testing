import psutil
from Line_Break import line_break

def Memory_Info():
    #Func. to convert Bytes to GB
    def bytes_to_GB(bytes):
        gb = bytes/(1024*1024*1024)
        gb = round(gb, 2)
        return gb
    #This will print the primary memory details
    print("\n\t\t\t Memory Information\n")

    virtual_memory = psutil.virtual_memory()
    print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
    line_break()