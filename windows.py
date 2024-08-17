import win32gui
import win32con

toplist = []
winlist = []


def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


win32gui.EnumWindows(enum_callback, toplist)
for hwnd, title in winlist:
    break
    # print(title)

w = [(hwnd, title) for hwnd, title in winlist if 'customstartpage' in title.lower()]
print(toplist)
# just grab the first window that matches
w = w[0]
print(w)
# use the window handle to set focus
win32gui.SetForegroundWindow(w[0])
