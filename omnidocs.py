import webbrowser
import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)
for i in range(30):
    pag.click(x=604, y=866)
    time.sleep(10)
