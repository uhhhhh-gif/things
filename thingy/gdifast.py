import win32gui
import win32con
import win32api
import random

def rainbow_invert_squares(hwnd):
    dc = win32gui.GetDC(hwnd)
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    while True:
        x = random.randint(1, width)
        y = random.randint(1, height)
        size = random.randint(10, 100000)
        color = random.randint(0, 0xFFFFFF)

        x = random.randint(2, width)
        y = random.randint(2, height)
        size = random.randint(100, 1000000)
        color = random.randint(0, 0xFFFFFF)

        x = random.randint(3, width)
        y = random.randint(3, height)
        size = random.randint(1000, 10000000)
        color = random.randint(0, 0xFFFFFF)

        x = random.randint(4, width)
        y = random.randint(4, height)
        size = random.randint(10000, 100000000)
        color = random.randint(0, 0xFFFFFF)

        x = random.randint(5, width)
        y = random.randint(5, height)
        size = random.randint(100000, 1000000000)
        color = random.randint(0, 0xFFFFFF)

        hbrush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(dc, hbrush)

        hbrush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(dc, hbrush)

        hbrush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(dc, hbrush)

        hbrush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(dc, hbrush)

        try:
          win32gui.PatBlt(dc, x, y, size, size, win32con.PATINVERT)
        except Exception as e:
           print(f"Error during PatBlt: {e}")

        win32gui.DeleteObject(hbrush)

if __name__ == '__main__':
    hwnd = win32gui.GetDesktopWindow() # Get the desktop window handle
    rainbow_invert_squares(hwnd)
