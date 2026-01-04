import os
import tkinter as tk
import time
import pyautogui as pag




pag.hotkey('alt','tab')
time.sleep(2)

pag.press('tab',presses=7)
time.sleep(2)
pag.hotkey('alt','down')
time.sleep(1)
pag.press('down')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('enter')


