#First load all custom modules and functions:

from modules.Date_Time_End import Date_Time_End
from modules.Date_Time_Start import Date_Time_Start
from modules.Pip_Installs import Pip_Installs
from modules.OS_Selection import OS_Info
from modules.Ubuntu_CPU_Info import CPU_Info

#MAIN:

def main():
        Date_Time_Start()
        Pip_Installs()
        OS_Info()
        CPU_Info()
        Memory_Info()
        check_internet_connection()
        Package_Installation()
        Setup_Snapd()
        Reminders()
#        Sys_Update()
#        Package_Cleanup()
#        Burn_Linux()
        Power_State_Testing()
        Date_Time_End()

#MAIN
if __name__ == '__main__':
    main()