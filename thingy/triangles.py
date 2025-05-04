import win32gui
import win32con
import win32api
import random

def draw_random_triangles():
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetDC(hwnd)

    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    while True:
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        x3 = random.randint(0, width)
        y3 = random.randint(0, height)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = win32api.RGB(r, g, b)

        hbrush = win32gui.CreateSolidBrush(color)
        old_brush = win32gui.SelectObject(hdc, hbrush)

        points = [(x1, y1), (x2, y2), (x3, y3)]
        win32gui.Polygon(hdc, points)

        win32gui.SelectObject(hdc, old_brush)
        win32gui.DeleteObject(hbrush)

    win32gui.ReleaseDC(hwnd, hdc)

if __name__ == '__main__':
    draw_random_triangles()