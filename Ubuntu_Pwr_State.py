import subprocess
import time

def Power_State_Testing():

    def test_system_sleep():
        # Put the system to sleep
        subprocess.run(['systemctl', 'suspend'])
        
        # Wait for a few seconds to allow the system to enter sleep mode
        time.sleep(5)

        # Check if the system is awake
        result = subprocess.run(['systemctl', 'is-system-running'], capture_output=True, text=True)
        output = result.stdout.strip()
        if output == 'running':
            print("System wake-up successful!")
        else:
            print("System failed to wake up.")