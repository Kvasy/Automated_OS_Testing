#Send to .txt file
#Still working to figure out how to guarentee this saves to an easy place every time.... maybe a dedicated USB, but will still need different code for Windows/Ubuntu
import os
import sys

def log_saver():
    Ubuntu_path = '/home/trenton/Desktop/OS_Test_Report'
    try:
        os.makedir(Ubuntu_path)
    except FileExistsError as exc:
        print('Directory exists. Continuing...')
    with open('OS_Report_Log.txt', 'a') as sys.stdout:
        sys.stdout.write()