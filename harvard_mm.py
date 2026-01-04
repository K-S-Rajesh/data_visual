import webbrowser
import pyautogui as pag
import time
import os

pag.hotkey('alt','tab')
time.sleep(1)

for i in range(20):
    pag.press('down')
    time.sleep(600)
