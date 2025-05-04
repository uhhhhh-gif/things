import win32gui, win32ui, win32con, win32api
import time
import random

def screen_train_effect(duration=100000, intensity=5):
    hwnd = win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hdesktop = win32gui.GetDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hdesktop)
    memdc = srcdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)

    start_time = time.time()
    while time.time() - start_time < duration:
        x_offset = random.randint(-intensity, intensity)
        y_offset = random.randint(-intensity, intensity)

        memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)
        srcdc.BitBlt((0, 0), (width, height), memdc, (x_offset, y_offset), win32con.SRCCOPY)

        time.sleep(0.01) # Adjust for speed
        
    # Restore original screen
    memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)
    srcdc.BitBlt((0, 0), (width, height), memdc, (0, 0), win32con.SRCCOPY)

    # Clean up
    win32gui.ReleaseDC(hwnd, hdesktop)
    srcdc.DeleteDC()
    memdc.DeleteDC()
    bmp.DeleteObject()

if __name__ == '__main__':
    screen_train_effect()