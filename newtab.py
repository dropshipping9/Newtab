import time
import pyautogui
import subprocess

# Function to open CMD and run commands
def open_cmd_and_run():
    # Open CMD using the Win + R shortcut
    pyautogui.hotkey('win', 'r')
    time.sleep(1)  # Wait for Run window to open

    # Type 'cmd' and press Enter to open CMD
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for CMD to open

    # Type the command to start Firefox and press Enter
    pyautogui.write('start firefox')
    pyautogui.press('enter')
    time.sleep(15)  # Wait a bit for Firefox to fully open
    # After Firefox opens, navigate to google.com
    pyautogui.write('https://www.google.com')
    pyautogui.press('enter')

# Run the function
open_cmd_and_run()
