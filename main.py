import pyautogui
import time
from adb_shell.adb_device import AdbDeviceTcp
from utils.find import findAll, find
from utils.screenshot import screenshot
from utils.click import click
import os
import sys

claim = './images/claim.png'
leave = './images/leave.png'
pivot = './images/pivot.png'
repeat = './images/repeat.png'
stamina = './images/stamina.png'


if __name__ == "__main__":

    port = sys.argv[sys.argv.index('-p')+1]

    device = AdbDeviceTcp('localhost', port, default_transport_timeout_s=9.)
    device.connect(auth_timeout_s=0.1)
    total_found = 0
    total_runs = 0

    try:
        while True:
            time.sleep(1)
            os.system('cls')
            # Find window
            tw = pyautogui.getWindowsWithTitle('BlueStacks')[0]
            # Take a screenshot
            shot = screenshot(tw)

            print(f'Found {total_found} pivots in {total_runs} runs')
            pivots = findAll(pivot, shot)

            if pivots:
                for p in pivots:
                    click(p, tw, device)
                    total_found += 1
                click(find(claim, shot), tw, device)
            else:
                click(find(leave, shot), tw, device)
                shot = screenshot(tw)
                r = find(repeat, shot)
                if r:
                    total_runs += 1
                    click(find(repeat, shot), tw, device)

    except KeyboardInterrupt:
        pass
