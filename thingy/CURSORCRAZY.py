import pyautogui
import keyboard
import random
import time

def crazy_cursor():
    try:
        while not keyboard.is_pressed('f7'):
            x = random.randint(0, pyautogui.size()[0])
            y = random.randint(0, pyautogui.size()[1])
            pyautogui.moveTo(x, y, duration=0.001)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print("Press F7 to stop the crazy cursor.")
    crazy_cursor()
    print("Crazy cursor stopped.")