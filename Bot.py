from pyautogui import *
import pyautogui
import time
import keyboard
from win32api import GetSystemMetrics
import win32api, win32con
import auto_chrome

# open site and do basic setup
auto_chrome.open_browser()
time.sleep(5)  

# Using win32api because it's faster than pyautogui
def click(x,y):
    win32api.SetCursorPos((x,y)) # Move to x and y position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)# click on that position
    time.sleep(0.01)# press for 0.01 sec,
    #the delay is just because sometimes click fails to execute if it's too fast
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)# release the click
  
# Get the screen resolution
w = GetSystemMetrics(0)
h = GetSystemMetrics(1) 

# Get center of the screen
cx = int(w/2)
cy = int(h/2)

# Get a random position all the four rows
row_1_x = cx-160
row_1_y = cy-30

row_2_x = cx-70
row_2_y = cx-330

row_3_x = cx + 70
row_3_y = cx - 330

row_4_x = cx + 140
row_4_y = cx - 330

time.sleep(50)

while keyboard.is_pressed('q') == False: # checks if key q is not pressed, if pressed stop the program
    if pyautogui.pixel(row_1_x,row_1_y)[0] == 0: # check for black color in the specific x and y position
        click(row_1_x,row_1_y) # if true click 

    if pyautogui.pixel(row_2_x,row_2_y)[0] == 0:
        click(row_2_x,row_2_y) 

    if pyautogui.pixel(row_3_x,row_3_y)[0] == 0: 
        click(row_3_x,row_3_y)

    if pyautogui.pixel(row_4_x,row_4_y)[0] == 0:
        click(row_4_x,row_4_y)
