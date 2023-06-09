import psutil
from Line_Break import line_break
import requests

def Network_Chk():
    print("\n\t\t\t Network Information\n")

    # gathering all network interfaces (virtual and physical) from the system
    if_addrs = psutil.net_if_addrs()
    # printing the information of eah network interfaces
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"Interface :", interface_name)
            if str(address.family) == 'AddressFamily.AF_INET':
                print("[+] IP Address :", address.address)
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print("[+] MAC Address :", address.address)
            line_break()

    request = requests.get('https://www.google.com')
    response = request.status_code
    if response == 200:
        print ('Network Connection Pass')
        print ('Successful ping to: Google.com')
    else:
        print ('Network Failure')
    line_break()