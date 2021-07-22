from win32api import GetSystemMetrics
import win32api
import time
import pyautogui as pa

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)

cx = int(w/2)
cy = int(h/2)



row_1_x = cx-160
row_1_y = cy-30

row_2_x = cx-70
row_2_y = cx-330

row_3_x = cx + 70
row_3_y = cx - 330

row_4_x = cx + 140
row_4_y = cx - 330

time.sleep(10)
win32api.SetCursorPos((row_1_x,row_1_y))
time.sleep(3)
win32api.SetCursorPos((row_2_x,row_2_y))
time.sleep(3)
win32api.SetCursorPos((row_3_x,row_3_y))
time.sleep(3)
win32api.SetCursorPos((row_4_x,row_4_y))

# print(pa.displayMousePosition(row_2_x,row_2_y))
# print(row_2_x,row_2_y)

# import wmi
# obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)

# displays = [x for x in obj if 'DISPLAY' in str(x)]
# lst = []
# for item in displays:
#    lst.append(item.Caption)
   
# print(len(lst))
