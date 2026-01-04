import subprocess
import webbrowser
import pyautogui as pag
import time



pag.hotkey('alt','tab')
time.sleep(3)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)

for i in range(21):
    pag.hotkey('shift','tab')
    time.sleep(0.3)

time.sleep(0.5)
pag.press('space')
time.sleep(0.5)
for i in range(2):
    pag.hotkey('shift','tab')
    time.sleep(0.3)


time.sleep(0.5)
pag.press('space')
time.sleep(0.5)
