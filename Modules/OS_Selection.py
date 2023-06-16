import platform
from Line_Break import line_break

def OS_Info():
    OS_INFO = platform.uname()
    print ('OS: ', OS_INFO[0])
    print ('Release / Kernel: ', OS_INFO[2])
    print ('Version: ', OS_INFO[3])
    print ('CPU Info: ', OS_INFO[5])
    line_break()

    #if OS_INFO ==
     #   x == 
     #   return
