import win32gui
import win32con
import win32api
import random
import time

def rainbow_invert_squares(hwnd):
    dc = win32gui.GetDC(hwnd)
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    while True:
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(10, 1000)
        color = random.randint(0, 0xFFFFFF)

        hbrush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(dc, hbrush)

        try:
          win32gui.PatBlt(dc, x, y, size, size, win32con.PATINVERT)
        except Exception as e:
           print(f"Error during PatBlt: {e}")

        win32gui.DeleteObject(hbrush)
        time.sleep(0.0001) # Adjust sleep time for speed

if __name__ == '__main__':
    hwnd = win32gui.GetDesktopWindow() # Get the desktop window handle
    rainbow_invert_squares(hwnd)