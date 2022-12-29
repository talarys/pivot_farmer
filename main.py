import pyautogui
import time
from adb_shell.adb_device import AdbDeviceTcp
from utils.find import find, findAll
from utils.screenshot import screenshot
from utils.click import click
import os
import sys


if __name__ == "__main__":

    port = sys.argv[sys.argv.index('-p')+1]

    device = AdbDeviceTcp('localhost', port, default_transport_timeout_s=9.)
    device.connect(auth_timeout_s=0.1)
    total_found = 0

    try:
        while True:
            time.sleep(1)
            os.system('cls')
            # Find window
            tw = pyautogui.getWindowsWithTitle('BlueStacks')[0]
            # Take a screenshot
            shot = screenshot(tw)

            print('Found ', total_found, ' pivots')
            # Find Pivots
            pivots = findAll('pivot', shot)

            if pivots != -1:
                for pivot in pivots:
                    click(pivot, tw, device)
                    total_found += 1
                # click(find('stamina', shot), tw, device)
                click(find('claim', shot), tw, device)
            else:
                click(find('leave', shot), tw, device)
                click(find('repeat', shot), tw, device)

    except KeyboardInterrupt:
        pass
